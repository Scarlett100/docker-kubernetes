from application import db
from datetime import datetime
from sqlalchemy import ForeignKey


class Aeroplanes(db.Model):
     
    aeroplane_id = db.Column(db.Integer, primary_key=True) 
    model_number = db.Column(db.Integer, nullable=False)
    number_of_seats = db.Column(db.Integer, nullable=False)
    company_owned_by = db.Column(db.String(30), nullable=False)
    flights = db.relationship('Flights', backref='aeroplane', lazy=True)

    def __repr__(self):
        return f"Aeroplanes('{self.model_number}','{self.number_of_seats}','{self.company_owned_by}'')"
        #return '<Aeroplanes%r>' % self.id
        #return
    

class Flights(db.Model):
    flight_id = db.Column(db.Integer, primary_key=True) 
    departure_date_time = db.Column(db.DateTime, nullable=False)
    arrival_date_time = db.Column(db.DateTime, nullable=False)
    arrival_destination = db.Column(db.String(20), nullable=False)
    direct_flight = db.Column(db.Boolean, default=True)
    flight_price = db.Column(db.Float, nullable=False)
    fk_aeroplane_id = db.Column(db.Integer, db.ForeignKey('aeroplanes.aeroplane_id'), nullable=False) 
   
    def __repr__(self):
        return f"Flights('{self.departure_date}', '{self.arrival_date_time}', '{self.arrival_destination}','{self.direct_flight}')"
        
       # '<Flights%r>' % self.id
        
        #would i return fk relational fk eg '{self.fk_aeroplane_id} in flights?