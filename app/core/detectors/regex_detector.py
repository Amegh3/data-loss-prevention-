import re
from typing import List

SENSITIVE_PATTERNS = {
    "credit_card": r"\b(?:\d[ -]*?){13,16}\b",
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone": r"\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b",
    "password": r"(?i)password\s*[:=]\s*[\S]+"
}

def detect_sensitive_regex(text: str) -> List[str]:
    findings = []
    for key, pattern in SENSITIVE_PATTERNS.items():
        matches = re.findall(pattern, text)
        findings.extend(matches)
    return findings
