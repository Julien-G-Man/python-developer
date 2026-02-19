import requests
from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Drink(db.Model):
    __tablename__ = "drinks"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'<Drink: {self.name} - {self.description}>'
    
with app.app_context():
    db.create_all()
    
@app.route('/')
def greet():
    return {'response': 'Hello'}

@app.get('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = [{"name": drink.name, "description": drink.description} for drink in drinks]
    return {"drinks": output}  

@app.get('/drinks/<id>')
def get_a_drink(id):
    drink = Drink.query.get_or_404(id)
    return jsonify({"name": drink.name, "description": drink.description})

@app.post('/drinks/<int:id>')
def add_drink():
    data = request.json
    name = data['name']
    description = data['description']
    
    drink = Drink.query.filter_by(name=name).first()
    if drink:
        return {"message": f"drink {data['name']} already exists"}, 400
    
    try:     
        new_drink = Drink(name=name, description=description)
        db.session.add(new_drink)
        db.session.commit()
        return {"message": f"New drink {name} created", 'id': new_drink.id}, 201
    
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
    
@app.delete('/drinks/delete/<int:id>')    
def delete_drink(id):
    drink = Drink.query.get(id)
    if not drink:
        return {"message": "drink not found"}
    
    db.session.delete(drink)
    db.session.commit()
    return {"message": f"drink {id} deleted successfully!"}