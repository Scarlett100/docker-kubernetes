from application import app, db
from application.models import Flights

@app.route('/add')
def add():
    new_flight = Flights(departure_date_time= "Enter desired date", arrival_date_time ="Enter desired date", arrival_destination ="Enter destination", direct_flight = "choose", flight_price = "Enter budget")#would I add foreign key? aeroplane ID?
    db.session.add(new_flight)
    db.session.commit()
    return "Congratulations! you have added a dream flight"

@app.route('/read')
def read():
    all_flights = Flights.query.all()
    flights_string = ""
    for flight in all_flights:
        flights_string += "<br>"+ flight.arrival_destination
    return flights_string

@app.route('/update/<flight_price>')
def update(flight_price):
    first_flight = Flights.query.first()
    first_flight.flight_price = flight_price
    db.session.commit()
    return first_flight.flight_price

@app.route('/delete')
def delete():
    flight_to_delete = Flights.query.first()
    db.session.delete(flight_to_delete)
    db.session.commit()
    return "You have deleted a flight"


#ja = Flights(departure_date_time = )
#flight_id = db.Column(db.Integer, Primary_key=True) #QUESTION is a primary key naturally unique?
    #departure_date_time = db.Column(db.DateTime, nullable=False)
    #arrival_date_time = db.Column(db.DateTime, nullable=False)
    #arrival_destination = db.Column(db.String(20), nullable=False)
    #direct_flight = db.Column(db.Boolean, default=True)
    #flight_price = db.Column(db.Decimal, nullable=False)
    #aeroplane_id = db.Column(db.String(30), db.ForeignKey('aeroplane.id'), nullable=False)




@app.route('/')
@app.route('/home')
def home():
    return "Welcome, are you ready to make your dream flight to the caribbean?!"

@app.route('/about')
def about():
   return 'On this website you can make a flight scheduele for a flight you would like to take'