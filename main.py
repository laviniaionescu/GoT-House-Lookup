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




