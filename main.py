import requests
import json

response = requests.get("https://anapioficeandfire.com/api/houses")
houses = json.loads(response.text)

for house in houses:
    print("House:", house['name'])

    if house['currentLord']:
        current_lord = requests.get(house['currentLord'])
        current_lord_data = json.loads(current_lord.text)
        lord = current_lord_data['name']
        print("The current lord is", lord)
    else:
        print("Current lord: Unknown.")


# houses is a list of dictionaries now


# leader = houses[1]['currentLord']
# print(leader)

# leader = response.json()[1]['currentLord']
# print(leader)


# for item in houses:
#     leader_link = item['currentLord']
#     response2 = requests.get(leader_link)
#     res = json.loads(response2.text)
#     print(response2.text)


