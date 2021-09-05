from app import db, Aeroplanes, Flights

db.create_all()

boeing_747= Aeroplanes(model_number = 5674538, number_of_seats = 102, company_owned_by ="Emirates")
db.session.add(boeing_747)
db.session.commit()


