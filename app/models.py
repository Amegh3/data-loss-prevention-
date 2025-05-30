from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class ScanRequest(BaseModel):
    filename: str
    content: str  # Base64 or raw text content of file

class ScanResponse(BaseModel):
    filename: str
    detected_data: Optional[List[str]]
    scanned_at: datetime
