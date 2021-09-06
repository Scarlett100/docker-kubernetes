from application import db

class Aeroplanes(db.Model):
    aeroplane_id = db.Column(db.Integer, primary_key=True) 
    model_number = db.Column(db.Integer, nullable=False)
    number_of_seats = db.Column(db.Integer, nullable=False)
    company_owned_by = db.Column(db.String(30), nullable=False)
    flights = db.relationship('Flights', backref='aeroplane')

    

class Flights(db.Model):
    flight_id = db.Column(db.Integer, primary_key=True) 
    departure_date_time = db.Column(db.DateTime, nullable=False)
    arrival_date_time = db.Column(db.DateTime, nullable=False)
    arrival_destination = db.Column(db.String(20), nullable=False)
    direct_flight = db.Column(db.Boolean, default=True)
    flight_price = db.Column(db.Float, nullable=False)
    fk_aeroplane_id = db.Column(db.Integer, db.ForeignKey('aeroplanes.aeroplane_id'), nullable=False) 
    #hello