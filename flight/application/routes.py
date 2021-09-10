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
    
    aeroplane = Aeroplanes.query.all()
    for fk_aeroplane_id in aeroplane:
        form.fk_aeroplane_id.choices.append((fk_aeroplane_id.aeroplane_id,fk_aeroplane_id.aeroplane_id))


    if request.method == 'POST':
        if form.validate_on_submit():
            departure_date = form.departure_date.data
            arrival_date = form.arrival_date.data
            arrival_destination = form.arrival_destination.data
            direct_flight = form.direct_flight.data
            flight_price = form.flight_price.data
            fk_aeroplane_id = form.fk_aeroplane_id.data
            
            flights= Flights(departure_date = departure_date, arrival_date=arrival_date, arrival_destination =  arrival_destination, direct_flight = direct_flight, flight_price = flight_price, fk_aeroplane_id = fk_aeroplane_id)

            

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


@app.route('/update_plane/<int:id>', methods=['GET' , 'POST'])
def updatePlane(id):
    form =AeroplanesForm()
    update_aeroplane = Aeroplanes.query.filter_by(aeroplane_id=id).first()

    if request.method == 'POST':
        if form.validate_on_submit():
            update_aeroplane.model_number = form.model_number.data
            update_aeroplane.number_of_seats = form.number_of_seats.data
            update_aeroplane.company_owned_by = form.company_owned_by.data
            
             
            db.session.commit()
            return redirect(url_for('AllAeroplanes'))
            

    elif request.method == 'GET':
        
        form.model_number.data = update_aeroplane.model_number
        form.number_of_seats.data = update_aeroplane.number_of_seats
        form.company_owned_by.data = update_aeroplane.company_owned_by
    
    return render_template('update_plane.html', form=form )


@app.route('/update_flights/<int:id>', methods=['GET' , 'POST'])
def updateFlights(id):
    message =""
    form =FlightsForm()
    update_flight = Flights.query.filter_by(flight_id=id).first()
    aeroplane = Aeroplanes.query.all()
    for fk_aeroplane_id in aeroplane:
        form.fk_aeroplane_id.choices.append((fk_aeroplane_id.aeroplane_id,fk_aeroplane_id.aeroplane_id))

    if request.method == 'POST':
        if form.validate_on_submit():
            update_flight.departure_date = form.departure_date.data
            update_flight.arrival_date = form.arrival_date.data
            update_flight.arrival_destination = form.arrival_destination.data
            update_flight.direct_flight = form.direct_flight.data
            update_flight.flight_price = form.flight_price.data
            update_flight.fk_aeroplane_id = form.fk_aeroplane_id.data

             if fk_aeroplane_id == 0
             return message(" please create aeroplane first, as no aeroplane has yet been created. " message=message)
             
            db.session.commit()
            return redirect(url_for('AllFlights'))
            

    elif request.method == 'GET':
      
            form.departure_date.data = update_flight.departure_date  
            form.arrival_date.data = update_flight.arrival_date 
            form.arrival_destination.data = update_flight.arrival_destination 
            form.direct_flight.data = update_flight.direct_flight 
            form.flight_price.data = update_flight.flight_price 
            form.fk_aeroplane_id = update_flight.fk_aeroplane_id
    
    return render_template('update_flights.html',form=form )


@app.route('/delete_flight/<int:id>', methods=['GET', 'POST']) #deletes                         flight +aeroplane
def delete_flight(id):
    
    flight_to_delete = Flights.query.get(id)
    if request.method =='POST':
        if flight_to_delete:
            db.session.delete(flight_to_delete)
            db.session.commit()
            return redirect(url_for('AllFlights'))
    return render_template('delete_flight.html')

@app.route('/delete_aeroplane/<int:id>', methods=['GET', 'POST'])
def delete_plane(id):
    plane_to_delete = Aeroplanes.query.get(id)
    if request.method =='POST':
        if plane_to_delete:
            db.session.delete(plane_to_delete)
            db.session.commit()
            return redirect(url_for('AllAeroplanes'))
    return render_template('delete_aeroplane.html')




@app.route('/')
@app.route('/home')
def home():
    #postData= Flights.query.all()
    return render_template('home.html', )

#@app.route('/about')
#def about():
 #flights=postData