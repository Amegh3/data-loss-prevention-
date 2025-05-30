from celery import Celery
from app.core.scanner import scan_text_for_sensitive_data
from app.core.alerting import send_alert_email

celery_app = Celery(
    "dlp_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def async_scan_and_alert(user_email: str, filename: str, content: str):
    findings = scan_text_for_sensitive_data(content)
    if findings:
        subject = f"DLP Alert: Sensitive data found in {filename}"
        body = f"The following sensitive data was detected:\n\n" + "\n".join(findings)
        send_alert_email(user_email, subject, body)
    return findings
