from app.core.detectors.regex_detector import detect_sensitive_regex
from app.core.detectors.ml_detector import detect_sensitive_ml

def scan_text_for_sensitive_data(text: str):
    findings = detect_sensitive_regex(text)
    ml_findings = detect_sensitive_ml(text)
    all_findings = findings + ml_findings
    return all_findings
