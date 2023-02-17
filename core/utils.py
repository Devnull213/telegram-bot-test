"""Various utilities"""
from datetime import datetime


def message() -> str:
    """Returns a custom message"""
    days_left = datetime(2023, 6, 8, 16, 25) - datetime.now()
    msg = f"\nQuedan {days_left.days} días para viajar a Deutschland prros!!"
    return msg
