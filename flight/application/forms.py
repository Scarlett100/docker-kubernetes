from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError

from application.models import Aeroplanes
from application.models import Flights

class AeroplanesForm(FlaskForm):
    model_number = SelectField("model", choices=[("747"),
    ("812"),
    ("989")
    })
    number_of_seats = SelectField("number of seats", choices=[
        ("40"),
        ("90"), 
        ("173")
    ])
    company_owned_by = SelectField("owner", choices=[
        ("Emirates"), 
        ("British Airways"), 
        ("Virgin Atlantic"), 
        ("Air France")
        })
    #flights? #relational database

    submit = SubmitField('Submit')


class FlightsForm(FlaskForm):
    departure_date_time = DateTimeField("departure date & time")
    arrival_date_time = DateTimeField("arrival date & time")
    arrival_destination = StringField("arrival")
    direct_flight = BooleanField("direct flight") #selectfield? yes or no
    flight_price = DecimalField()("budget")
    #fk_aeroplane_id #fk needed?
    submit = SubmitField("Submit")

