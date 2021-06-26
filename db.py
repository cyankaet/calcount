from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
class Meal(db.Model):
    __tablename__="meal"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    foods = db.relationship("Foods", back_populates="meal")

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.time = kwargs.get('time')

class Food(db.Model):
    __tablename__:"food"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'))
    meal = db.relationship("Meal", back_populates="foods")

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.calories = kwargs('calories')

