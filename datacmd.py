from db import Meal, Food, db
from datetime import date, datetime, timedelta

from flask import Flask, request
import json

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(error, code=404):
    return json.dumps({"success": False, "error": error}), code

def calculate_calories(date): #reusing the method
    meals = Meal.query.filter_by(date=date)
    calories = 0
    for meal in meals:
        calories += meal["calories"]
    return calories

@app.route("/")
@app.route("/meal/", methods=['POST'])
def new_meal():
    body = json.loads(request.data)
    name = body.get('name')
    if name is None:
        return failure_response("Name missing from meal creation")
    meal = Meal(name=name, date=date.today())
    db.session.add(meal)
    db.session.commit()
    return success_response(meal.serialize())

@app.route("/food/", methods=['POST'])
def new_food():
    body = json.loads(request.data)
    meal_name = body.get('meal_name')
    calories = body.get('calories')
    name = body.get('name')
    if meal_name is None or calories is None or name is None:
        return failure_response("One or more food creation elements is missing")
    meal = Meal.query.filter_by(name= meal_name, date=date.today()).first()
    food = Food(name = name, calories=calories)
    db.session.add(meal)
    meal.foods.append(food)
    db.session.commit()
    return success_response(meal.serialize())

@app.route("/recent/")
def recent_day_calories():
    cals = {}
    for i in range(7):
        cals[datetime.today().strftime('%A')]=calculate_calories(timedelta(-7 + i))
    return success_response(cals)

@app.route("/calculate/")
def get_day_cals():
    # body = json.loads(request.data)
    # print(body)
    # date = body.get('date')
    # if date is None:
    #     return failure_response("Missing calculation date")
    # success_response(calculate_calories(date))
    success_response(calculate_calories(date.today()))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
