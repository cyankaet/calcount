from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Day(db.Model):
    __tablename__="day"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    meals = db.relationship("Meals", back_populates="day")
    
class Meal(db.Model):
    __tablename__="meal"
    id = db.Column(db.Integer, primary_key=True)
    calories = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Time, nullable=False) #just use time?
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))
    day = db.relationship("Day", back_populates="meals")
    foods = db.relationship("Foods", back_populates="meal")

    def __init__(self, **kwargs):
        self.calories = kwargs.get('calories')
        self.time = kwargs.get('time')

class Food(db.Model):
    __tablename__:"food"
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'))
    meal = db.relationship("Meal", back_populates="foods")
