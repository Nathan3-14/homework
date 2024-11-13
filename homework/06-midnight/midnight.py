from datetime import datetime, timedelta, time


now = datetime.now()
midnight = datetime.combine(now + timedelta(days=1), time())
split_time = str((midnight-now)).split(":")
split_time.pop(-1)
print(f"Hrs: {split_time[0]}, Mins: {split_time[1]}")