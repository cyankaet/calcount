from db import Meal, Food, db
from datetime import date

def new_meal(name):
    meal = Meal(name=name, date=date.today())
    db.session.add(meal)
    db.commit()
    return meal.serialize()

def new_food(meal_name, calories, name):
    meal = Meal.query.filter_by(name= meal_name, date=date.today()).first()
    food = Food(name = name, calories=calories)
    db.session.add(meal)
    meal.foods.append(food)
    db.session.commit()
    return meal.serialize()

def calculate_calories_today():
    meals = Meal.query.filter_by(date=date.today())
    calories = 0
    for meal in meals:
        calories += meal["calories"]
    return calories