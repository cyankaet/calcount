from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Meal(db.Model):
    __tablename__="meals"
    id = db.Column(db.Integer, primary_key=True)
    calories = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    def __init__(self, kwargs**):
        self.calories = kwargs.get('calories')
        self.time = kwargs.get('time')

    