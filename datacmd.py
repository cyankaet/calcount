from db import Day, Meal, Food, db

def new_meal(name, time, date):
    day = Day.query.filter_by(date=date).first()
    if day is None:
        day = Day(date=date)
        db.session.add(day)
    meal = Meal(name=name, time=time)
    db.session.add(meal)
    day.meals.append(meal)
    db.commit()
    return meal