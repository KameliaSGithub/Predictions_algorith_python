import random
from datetime import datetime, timedelta
days_ahead = random.randint(1, 30)
future_date = datetime.now() + timedelta(days=days_ahead)
formatted_future_date = future_date.strftime("%Y-%m-%d")
print(formatted_future_date)
