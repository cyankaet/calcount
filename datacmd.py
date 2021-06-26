from db import Meal, Food, db
from datetime import date

def new_meal(name):
    meal = Meal(name=name, date=date.today())
    db.session.add(meal)
    db.commit()
    return meal

def new_food(meal_name, calories, name):
    meal = Meal.query.filter_by(name= meal_name, date=date.today()).first()