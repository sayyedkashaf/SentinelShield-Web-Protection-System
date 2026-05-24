import re

ATTACK_PATTERNS = {
    "SQL Injection": [
        r"(\bor\b|\band\b).*=.*",
        r"union\s+select",
        r"drop\s+table",
        r"'--"
    ],

    "XSS": [
        r"<script.*?>",
        r"javascript:",
        r"onerror="
    ],

    "Directory Traversal": [
        r"\.\./",
        r"\.\.\\"
    ],

    "Command Injection": [
        r";",
        r"\|",
        r"&&"
    ]
}


def detect_attack(text):

    for attack_type, patterns in ATTACK_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text, re.IGNORECASE):
                return attack_type

    return None