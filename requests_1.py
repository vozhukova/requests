import requests

TOKEN = "2619421814940190"
BASE_URL = "https://superheroapi.com/api/"

res_dict = {}
list_heroes = ["Hulk", "Captain America", "Thanos"]

# Вариант для заполнения списка героев пользователем:
# list_heroes = []
# while True:
#     command = input("Введите команду: ").lower()
#     if command == "add":
#         hero = input("Введите героя: ")
#         list_heroes.append(hero)
#     else:
#         break

for hero in list_heroes:
    url = BASE_URL + TOKEN + "/search/" + hero
    resp = requests.get(url)
    intelligence = int(resp.json()["results"][0]["powerstats"]["intelligence"])
    res_dict[intelligence] = hero

values = list(res_dict.keys())
max_num = max(values)

print(f"Cамый умный супергерой - {res_dict[max_num]}")




