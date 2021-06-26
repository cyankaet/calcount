# import db
import requests
import json

def add():
    print("i'm adding!")

def graph():
    print("i'm graphing!")



PARAMS = {'query': "  hot wings"}
base_url = "https://api.nal.usda.gov/fdc/v1"
function = "/foods/search"
with open('apiKey.json', "r") as f:
    api_key = json.load(f)["key"]
url = base_url + function + "?api_key=" + api_key
response = requests.get(url = url, params = PARAMS)
data = response.json()

print(len(data['foods']))
print([x['description'] for x in data['foods']])
if data['foods']:
    for x in data['foods'][0]["foodNutrients"]:
        if x["unitName"] == "KCAL":
            print(x["value"])
else:
    print("Food item: " + PARAMS["query"] + " not found")