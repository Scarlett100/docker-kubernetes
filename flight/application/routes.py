from application import app, db
from application.models import Flights
from application.models import Aeroplanes
from flask import Flask, render_template, request, redirect, url_for,flash
from application.forms import FlightsForm, AeroplanesForm



@app.route('/create_aeroplane', methods = ['GET', 'POST'])
def create_aeroplane():
    message = ""
    form =AeroplanesForm() 
    
    if request.method == 'POST':
        if form.validate_on_submit():
            
            model_number = form.model_number.data
            number_of_seats = form.number_of_seats.data
            company_owned_by = form.company_owned_by.data

            aeroplane = Aeroplanes(model_number = model_number, number_of_seats = number_of_seats, company_owned_by = company_owned_by)  
            db.session.add(aeroplane)
            db.session.commit()
   
        message=(f"you have created aeroplane {model_number} owned by {company_owned_by}, with a capacity of {number_of_seats} seats ")
            
        return render_template('home.html', message=message) 
    return render_template('create_aeroplane.html', form=form) 

@app.route('/create_flight', methods = ['GET', 'POST'])
def create_flight():
    message = "abc"
    form =FlightsForm() 
    
    if request.method == 'POST':
        if form.validate_on_submit():
            departure_date_time = form.departure_date_time.data
            arrival_date_time= form.arrival_date_time.data
            arrival_destination = form.arrival_destination.data
            direct_flight = form.direct_flight.data
            flight_price = form.flight_price.data
            fk_aeroplane_id = form.fk_aeroplane_id.data

            flights= Flights(departure_date_time = departure_date_time, arrival_date_time=arrival_date_time, arrival_destination =  arrival_destination, direct_flight = direct_flight, flight_price = flight_price, fk_aeroplane_id = fk_aeroplane_id)  

            db.session.add(flights)
            db.session.commit()

            message=(f"you have created a flight from London on {departure_date_time} arriving at {arrival_date_time} in {arrival_destination} and are on a budget of {flight_price} on aeroplane {fk_aeroplane_id}")
        return render_template('home.html', message=message) 
    return render_template('create_flight.html', form=form) 
            


@app.route('/read')
def read():
    all_flights = Flights.query.all()
    flights_string = ''
    return flights_string

#i'd like to read second flight &count flights

@app.route('/update/<int:aeroplane>')
def update(aeroplane_id):
    form =FlightsForm
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
    aeroplane = Aeroplanes.query.all()
    return render_template('home.html',aeroplane=aeroplane)

#@app.route('/about')
#def about():
 #  return 'On this website you can make a flight scheduele for a flight you would like to take'