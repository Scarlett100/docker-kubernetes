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
            #aeroplane_id = form.aeroplane_id.data
            model_number = form.model_number.data
            number_of_seats = form.number_of_seats.data
            company_owned_by = form.company_owned_by.data

            aeroplane = Aeroplanes(model_number = model_number, number_of_seats = number_of_seats, company_owned_by = company_owned_by)  
            db.session.add(aeroplane)
            db.session.commit()
   
        message=(f"you have created aeroplane ,model number {model_number} owned by {company_owned_by}, with a capacity of {number_of_seats} seats ")
            
           # {aeroplane_id}
        return render_template('home.html', message=message) 
    return render_template('create_aeroplane.html', title='create aeroplane', form=form) 

@app.route('/create_flight', methods = ['GET', 'POST'])
def create_flight():
    message = ""
    form =FlightsForm() 
    #allFlights=Flights.query.filter_by(fk_aeroplane_id=id)

    if request.method == 'POST':
        if form.validate_on_submit():
            departure_date = form.departure_date.data
            arrival_date = form.arrival_date.data
            arrival_destination = form.arrival_destination.data
            direct_flight = form.direct_flight.data
            flight_price = form.flight_price.data
            fk_aeroplane_id = form.fk_aeroplane_id.data

            flights= Flights(departure_date = departure_date, arrival_date=arrival_date, arrival_destination =  arrival_destination, direct_flight = direct_flight, flight_price = flight_price, fk_aeroplane_id = fk_aeroplane_id)

            #for fk_aeroplane_id in allFlights:

            db.session.add(flights)
            db.session.commit()
        
            message=(f"you have created a flight from London on {departure_date} arriving at {arrival_date} in {arrival_destination} and are on a budget of £{flight_price} on aeroplane {fk_aeroplane_id}")
        return render_template('home.html', message=message) 
    return render_template('create_flight.html', form=form) 
            


@app.route('/all_flights') #read methods=[GET]if request.method == [GET]:
def AllFlights():
    all_flights = Flights.query.all()
    return render_template('all_flights.html', all_flights=all_flights)

@app.route('/all_aeroplanes') #read methods=[GET] if request.method == [GET]:
def AllAeroplanes(): 
    all_aeroplanes = Aeroplanes.query.all()
    return render_template('all_aeroplanes.html', all_aeroplanes=all_aeroplanes)


@app.route('/update/<int:id>', methods=['GET' , 'POST'])
def update(id):
    form =AeroplanesForm()
    update_aeroplane = Aeroplanes.query.filter_by(aeroplane_id=id).first()

    if request.method == 'POST':
        if form.validate_on_submit():
            model_number = form.model_number.data
            number_of_seats = form.number_of_seats.data
            company_owned_by = form.company_owned_by.data
            
            aeroplane = Aeroplanes(model_number = model_number, number_of_seats = number_of_seats, company_owned_by = company_owned_by) 
            db.session.commit()
            return redirect(url_for('AllAeroplanes'))
            #return redirect(url_for('home'))

    elif request.method == 'GET':
        print(update_aeroplane)
        form.model_number.data = update_aeroplane.model_number
        form.number_of_seats.data = update_aeroplane.number_of_seats
        form.company_owned_by.data = update_aeroplane.company_owned_by
        
    return render_template('update.html', form=form )




@app.route('/delete_flight/<int:id>', methods=['GET', 'POST']) #deletes flight +aeroplane
def delete_flight(id):
    
    flight_to_delete = Flights.query.first()
    if request.method =='POST':
        if flight_to_delete:
    
            db.session.delete(flight_to_delete)
            db.session.commit()
        return "You have deleted a flight"
    return render_template('delete_flight.html')

@app.route('/delete_aeroplane/<int:id>', methods=['GET', 'POST'])
def delete_plane(id):
    plane_to_delete = Aeroplanes.query.first()
    if request.method =='POST':
        if plane_to_delete:
            db.session.delete(plane_to_delete)
            db.session.commit()
        return "You have deleted an aeroplane"
    return render_template('delete_aeroplane.html')




@app.route('/')
@app.route('/home')
def home():
    postData= Flights.query.all()
    #postData= Flights.query.all(all)
    return render_template('home.html', flights=postData)

#@app.route('/about')
#def about():
 #  return 'On this website you can make a flight scheduele for a flight you would like to take'