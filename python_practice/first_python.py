from datetime import datetime
#from ZoneInfo import ZoneInfo
from zoneinfo import ZoneInfo


print("Hello World")

nc_time = datetime.now(ZoneInfo("America/New_York"))

india_time = datetime.now(ZoneInfo("Asia/Kolkata"))

time_format = "%Y-%m-%d %I:%M:%S %p (%Z)"

print("--- Current Times ---")
print(f"Greensboro, NC: {nc_time.strftime(time_format)}")
print(f"Hyderabad, IN:  {india_time.strftime(time_format)}")
