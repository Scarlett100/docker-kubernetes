#import modules needed
from flask import url_for
from flask_testing import TestCase
#import applications classes and objects (which is object which is class)
from application import app, db
from application.models import Flights
from application.models import Aeroplanes   

#base class
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='Test_SECRET_KEY',
                Debug=True,
                WTF_CSRF_ENABLED=False
                
                )
        return app
    def setUp(self)
        """
        Will be called before every test
        """
        db.session.commit() #clears any date and creates table
        db.drop_all()
        db.create_all()

        first_aeroplane = Aeroplanes(
            model_number = "818"
            number_of_seats =  "22"
            company_owned_by = "Vueling"
       
        db.session.add(first_aeroplane) #adds to database
        db.session.commit()

        first_flight = Flights(
            departure_date = "2021-05-09"
            arrival_date = " 2022-04-07"
            arrival_destination = "Malta"
            direct_flight = "True"
            flight_price = "555.98"
            fk_aeroplane_id = "1"
        db.session.add(first_flight)
        db.session.commit()

        )

    def tearDown(self): #closes database session
        db.session.remove()
        db.drop_all()

class TestViews(TestBase)    #testing homepage loads
    def testing_home(self):
        response = self.client.get(url_for 'home')
        self.assertEqual(response.status_code, 200)

class TestViewingCreateFlight(TestBase) #Get request for adding/creating a flight.
    def testing_create_flight_get(self)
        response = self.client.get(url_for('create_flight'))
        self.assertIn(b'2021-05-09', response.data)


class TestAddingFlight #tests CREATEting flight (post)
    def test_add_flight_post(self)
        response = self.client.post(url_for('create_flight'))
        data = dict( departure_date = "2021-05-09"
            arrival_date = " 2021-05-10"
            arrival_destination = "Miami"
            direct_flight = "False"
            flight_price = "567.98"
            fk_aeroplane_id = "6" 
        ),
        
    )
        self.assertIn(b"2021-05-09", response.data) 

# Test CREATEting CREATING aeroplane (GET)

class TestViewingCreateAeroplane(TestBase)
    def testing_create_aeroplane_get(self)
        response = self.client.get(url_for('create_aeroplane'))
        self.assertIn(b'Vueling', response.data) #do i need to add the airplane dictionary  

# tests CREATEting flight (post)
class TestAddingFlight #tests CREATEting Aeroplane (post)
    def test_add_flight_post(self)
        response = self.client.post(url_for('create_flight'))
        data = dict(  model_number = "818"
                    number_of_seats =  "22"
                    company_owned_by = "Vueling"
        ),
        
    )
        self.assertIn(b"818", response.data) 


       
class TestViewAeroplane(TestBase)     #testing aeroplane page loads (get) not sure itwill work still need to determine method 
    def testing_Aeroplane_view(self):
        response = self.client.get(url_for 'AllAeroplanes')
        self.assertEqual(response.status_code, 200) 

class TestViewFlights(TestBase)    #testing flight page loads (get)
    def testing_Flights_view(self):
        response = self.client.get(url_for 'AllFlights')
        self.assertEqual(response.status_code, 200) 


    class TestViewUpdateFlight(TestBase)     #testing Flight page loads(GET)
    def testing_updating_Flight_view(self):
        response = self.client.get(url_for 'updateFlights')
        self.assertEqual(response.status_code, 200)     

class Test_Updating_Flight(TestBase):  #Test updating an flight (POST)
    def testUpdateFlight(self):
        response=self.client.post(
            url_for('updateFlights', id=1),
            data = dict (  departure_date = "2021-05-09"
            arrival_date = " 2021-05-10"
            arrival_destination = "Miami"
            direct_flight = "False"
            flight_price = "567.98"
            fk_aeroplane_id = "6" 

            ),
            follow_redirects =True
        )
        self.assertIn(b'6', response.data)



class TestViewUpdateAeroplane(TestBase)     #testing aeroplane page loads (get)
    def testing_updating_Aeroplane_view(self):
        response = self.client.get(url_for 'updatePlane')
        self.assertEqual(response.status_code, 200)     



class Test_Updating_aeroplane(TestBase): #Test update an aeroplane (POST)
    def testUpdateAeroplane(self):
        response=self.client.post(
            url_for('updatePlane', id=1),
            data = dict (  model_number = "818"
                    number_of_seats =  "22"
                    company_owned_by = "Vueling"

            ),
            follow_redirects =True
        )
        self.assertIn(b'818', response.data)



#deleting a flight GET

class Test_delete_flight(TestBase):
    def test_delete_flight(self):
        response = self.client.get(url_for('delete_flight, id=')
        self.assertEqual(response.status_code, 200)

 #for delete will be GET

#deleting a aeroplane GET
class Test_delete_aeroplane(TestBase):
    def test_delete_aeroplane(self):
        response = self.client.get(url_for('delete_aeroplane, id=')
        self.assertEqual(response.status_code, 200)



