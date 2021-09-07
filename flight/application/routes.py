from application import app, db
from application.models import Flights
from application.models import Aeroplanes
from flask import Flask, render_template, request
from application.forms import FlightsForm, AeroplanesForm



@app.route('/create_aeroplane', methods = ['GET', 'POST'])
def create_aeroplane():

    form =AeroplanesForm() 
    message = ""
     
    if request.method == 'POST':
        if form.validate_on_submit():
            aeroplanes = Aeroplanes(
                model_number = form.model_number.data,
                number_of_seats = form.number_of_seats.data,
                company_owned_by = form.company_owned_by.data
            )    message = f" you have created an aeroplane owned by {company_owned_by},"

            db.session.add(aeroplanes)
            db.session.commit()

    return render_template('create_aeroplane.html', form=form, message=message)

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



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#@app.route('/about')
#def about():
 #  return 'On this website you can make a flight scheduele for a flight you would like to take'