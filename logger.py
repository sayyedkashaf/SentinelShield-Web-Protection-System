import csv
import os
from datetime import datetime

LOG_FILE = "logs/security_logs.csv"


def log_event(ip, attack, action):

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "IP Address",
                "Attack Type",
                "Action"
            ])

        writer.writerow([
            datetime.now(),
            ip,
            attack,
            action
        ])