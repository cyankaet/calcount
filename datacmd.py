from db import Day, Meal, Food, db

def new_meal(name, datetime):
    meal = Meal(name=name, time=datetime)
    db.session.add(meal)
    db.commit()
    return meal

def new_food(meal_name, calories, date, name):
    meal = Meal.query.filter_by(name)