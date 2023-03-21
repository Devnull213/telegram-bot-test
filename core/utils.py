"""Various utilities"""
from datetime import datetime
from core.eur_price import GetEurData

eur_data = GetEurData()
uno, dos = eur_data.convert_price()

def message() -> tuple:
    """Returns a custom message"""
    days_left = datetime(2023, 6, 8, 16, 25) - datetime.now()
    msg = f"\nQuedan {days_left.days} días para viajar a Deutschland prros!!"
    msg2 = f"Precio Euro: {uno}\nNo podemos bajar de {dos} pesos"
    return msg, msg2

