import requests
import datetime as dt

r = requests.get("https://api.github.com")

now = dt.datetime.now()
if r.status_code == 200:
    print(f"The time is {str(now)}")
