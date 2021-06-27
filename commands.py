from datacmd import *
from math import *
import requests
import json
from ascii_graph import Pyasciigraph
from datetime import date
import os

os.environ['NO_PROXY'] = '127.0.0.1'

PARAMS = {'query': ""}
base_url = "https://api.nal.usda.gov/fdc/v1"
function = "/foods/search"
with open('apiKey.json', "r") as f:
    api_key = json.load(f)["key"]
url = base_url + function + "?api_key=" + api_key

def add():
    print("Add mode \n")
    mealName = input("Name this meal: ")
    params = {'name': mealName}
    print(json.dumps(params))
    requests.post('http://localhost:5000/meal/', json = {'name': mealName})
    foodList = input("Please enter the food you've eaten for the meal as a comma-separated list (ex: orange chicken, soda, cookie): ").split(", ")
    mealCals = 0
    for food in foodList:
        PARAMS["query"] = food
        response = requests.get(url = url, params = PARAMS)
        data = response.json()
        if data['foods']:
            batches = len(data['foods']) // 5
            indexPicked = 0
            
            i = 0
            while True:
                tempI = i
                print(str(len(data['foods'])) + " results for " + food + "\n")
                for j in range(5*i, min((5*i + 5), len(data['foods']))):
                    print(str(j + 1) + ": " + data['foods'][j]['description'])
                indexQuery = ""
                print("\n")
                if (i == 0 and batches == 0):
                    indexQuery = "Please select the index of the food item you want: "
                elif i == 0:
                    indexQuery = "Please select the index of the food item you want (Enter n to go to the next page): "
                elif i == batches:
                    indexQuery = "Please select the index of the food item you want (Enter p to go to the previous page): "
                else:
                    indexQuery = "Please select the index of the food item you want (Enter p to go to the previous page and n to go to the next page): "
                indexPicked = input(indexQuery)
                if indexPicked == "p":
                    i -= 1
                elif indexPicked == "n":
                    i += 1
                else:
                    try:
                        indexPicked = int(indexPicked) - 1
                        if indexPicked in range(5*i, min((5*i + 5), len(data['foods']))):
                            break
                        else:
                            raise ValueError
                    except:
                        print("Invalid index, please select again")
                if (i < 0 or i > batches):
                    print("Invalid operation, please try again")
                    i = tempI
            for x in data['foods'][indexPicked]["foodNutrients"]:
                if x["unitName"] == "KCAL":
                    print(food + " has " + str(x["value"]) + " calories per serving")
                    while True:
                        try:
                            numServings = int(input("How many servings did you have? "))
                            mealCals += (int(x["value"]) * numServings) 
                            params = {'meal_name': mealName, 'calories': mealCals, 'name': food}
                            requests.post('http://localhost:5000/food/', json = {'meal_name': mealName, 'calories': mealCals, 'name': food})
                            break
                        except:
                            print("Invalid amount, please try again")
        else:
            print("Food item: " + PARAMS["query"] + " not found")
    print("This meal has " + str(mealCals) + " calories.")

def graph():
    j = requests.get('http://localhost:5000/recent/')
    stuff = j.json().get('data')
    #print(stuff)
    weekcals = [('Sunday', 1892), ('Monday', 1456), ('Tuesday', 1203), ('Wednesday', 1234), ('Thursday', 1531),
            ('Friday', 2000), ('Saturday', 1834)]
    graph = Pyasciigraph()
    for line in graph.graph('Calories per day for the last week', weekcals):
        print(line)
    #print("i'm graphing!")


def track(cal_needs):
    # params= {'date': json.dumps(date.today().isoformat())}
    # numCaloriesToday = requests.get('http://localhost:5000/calculate/', json = params)
    #params= {'date': date.today()}
<<<<<<< HEAD
    j = requests.post('http://localhost:5000/calculate/')
    print("Out of the suggested " + str(cal_needs) + " daily calories, you have eaten " + str(j.json()["data"]["calories"]) + " calories.")
=======
    j = requests.get('http://localhost:5000/calculate/')
    numCaloriesToday = j.json().get('data')
    print("Out of the suggested " + str(cal_needs) + " daily calories, you have eaten " + str(numCaloriesToday) + " calories.")
>>>>>>> 0ccca28716cd727f45c48c65946e3019c53249ba

