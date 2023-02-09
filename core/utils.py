from datetime import datetime

def message() -> str:
    days_left = datetime(2023, 6, 8, 16, 25) - datetime.now()
    message = f"\nQuedan {days_left.days} días para viajar a Deutschland prros!!"
    return message
