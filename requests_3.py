import requests
from pprint import pprint
import datetime

day_1 = datetime.date.today()
print(day_1)
day_2 = day_1 - datetime.timedelta(days=1)
print(day_2)

questions = {}
BASE_URL = "https://api.stackexchange.com/"
params = {
    "fromdate": day_2,
    "todate": day_1,
    "order": "desc",
    "sort": "creation",
    "tagged": "python",
    "filter": "default",
    "site": "stackoverflow"
}

response = requests.get(BASE_URL + "2.3/questions", params=params)

r = response.json()

for item in r["items"]:
    questions[item["title"]] = item["link"]

pprint(questions)
