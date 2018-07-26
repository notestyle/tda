from datetime import datetime
from forex_python.converter import get_rate

t = datetime(2018, 6, 17)
t = t.replace(minute=9, hour=16, second=10)

rate = get_rate("EUR", "USD", t)
print(t, " - ",rate)

t = datetime(2018, 7, 18)
t = t.replace(minute=5, hour=16, second=10)

rate = get_rate("USD", "EUR", t)
print(t, " - ",rate)