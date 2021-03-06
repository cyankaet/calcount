from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
    
class Meal(db.Model):
    __tablename__="meal"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    foods = db.relationship("Food", back_populates="meal")

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.date = kwargs.get('date')
        
    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "foods": [f.serialize() for f in self.foods]}

class Food(db.Model):
    __tablename__ = "food"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'))
    meal = db.relationship("Meal", back_populates="foods")

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.calories = kwargs.get('calories')

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "calories": self.calories
                }
