from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_current_user, get_db
from app.models import UserOut, UserCreate, Token, ScanRequest, ScanResponse
from app.db.models import User, ScanRecord
from app.core.auth import verify_password, get_password_hash, create_access_token
from datetime import timedelta
from app.core.tasks import async_scan_and_alert
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    q = await db.execute(
        "SELECT * FROM users WHERE email = :email",
        {"email": user_in.email}
    )
    existing_user = q.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = get_password_hash(user_in.password)
    new_user = User(email=user_in.email, hashed_password=hashed)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    q = await db.execute(
        "SELECT * FROM users WHERE email = :email",
        {"email": form_data.username}
    )
    user = q.scalar_one_or_none()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(data={"sub": str(user.id)}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/scan", response_model=ScanResponse)
async def scan_file(scan_req: ScanRequest, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    # Asynchronously scan content via Celery
    task = async_scan_and_alert.delay(current_user.email, scan_req.filename, scan_req.content)
    findings = task.get(timeout=10)  # wait synchronously here (adjust as needed)

    # Save record
    record = ScanRecord(filename=scan_req.filename, detected_data="\n".join(findings), user_id=current_user.id)
    db.add(record)
    await db.commit()
    await db.refresh(record)

    return ScanResponse(filename=scan_req.filename, detected_data=findings, scanned_at=record.scanned_at)
