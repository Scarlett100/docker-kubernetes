from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return "Welcome, are you ready to make your dream flight to the caribbean?!"

@app.route('/about')
def about():
   return 'On this website you can make a flight scheduele for a flight you would like to take'

class Aeroplanes(db.model):
    aeroplane_id = db.Column(db.String(30), primary_key=True) #does this need to be call just id instead of aeroplane.id (database layer relationships)
    model_number = db.Column(db.Integer, nullable=False)
    number_of_seats = db.Column(db.Integer, nullable=False)
    company_owned_by = db.Column(db.String(30, nullable=False)
    flights = db.relationship('flight', backref='aeroplane')


class Flights(db.model):
    flight_id = db.Column(db.Integer, Primary_key=True) #QUESTION is a primary key naturally unique?
    departure_date_time = db.Column(db.DateTime, nullable=False)
    arrival_date_time = db.Column(db.DateTime, nullable=False)
    departure_origin = db.Column(db.String(20), nullable=False
    arrival_destination = db.Column(db.String(20), nullable=False)
    direct_flight = db.Column(db.Boolean, default=True)
    flight_price = db.Column(db.Decimal, nullable=False)
    aeroplane_id = db.Column(db.String(30), db.ForeignKey('aeroplane.id'), nullable=False)

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
