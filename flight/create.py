from application import db #, Aeroplanes, Flights
db.drop_all()
db.create_all()

boeing_747= Aeroplanes(model_number = 5674538, number_of_seats = 102, company_owned_by ="Emirates")
db.session.add(boeing_747)
db.session.commit()

#ja = Flights(depature_date_time = )
#flight_id = db.Column(db.Integer, Primary_key=True) #QUESTION is a primary key naturally unique?
    #departure_date_time = db.Column(db.DateTime, nullable=False)
    #arrival_date_time = db.Column(db.DateTime, nullable=False)
    #arrival_destination = db.Column(db.String(20), nullable=False)
    #direct_flight = db.Column(db.Boolean, default=True)
    #flight_price = db.Column(db.Decimal, nullable=False)
    #aeroplane_id = db.Column(db.String(30), db.ForeignKey('aeroplane.id'), nullable=False)



