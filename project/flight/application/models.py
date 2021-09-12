from application import db
from datetime import datetime
from sqlalchemy import ForeignKey


class Aeroplanes(db.Model):
     
    aeroplane_id = db.Column(db.Integer, primary_key=True) 
    model_number = db.Column(db.Integer, nullable=False)
    number_of_seats = db.Column(db.Integer, nullable=False)
    company_owned_by = db.Column(db.String(30), nullable=False)
    flights = db.relationship('Flights', backref='aeroplane', lazy=True)

    #def __repr__(self):
#return f"Aeroplanes('{self.model_number}','{self.number_of_seats}','{self.company_owned_by}'')"
        
    

class Flights(db.Model):
    flight_id = db.Column(db.Integer, primary_key=True) 
    departure_date = db.Column(db.Date, nullable=False)
    arrival_date = db.Column(db.Date, nullable=False)
    arrival_destination = db.Column(db.String(20), nullable=False)
    direct_flight = db.Column(db.Boolean, default=True)
    flight_price = db.Column(db.Float, nullable=False)
    fk_aeroplane_id = db.Column(db.Integer, db.ForeignKey('aeroplanes.aeroplane_id'), nullable=False                                                                                   ) 
   
    #def __repr__(self):
        #return f"Flights('{self.departure_date}', '{self.arrival_date}', '{self.arrival_destination}','{self.direct_flight}')"
        
      