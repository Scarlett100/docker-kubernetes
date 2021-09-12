#import modules needed
from flask import url_for
from flask_testing import TestCase
#import applications classes and objects (which is object which is class)
from application import app, db
from application.models import Flights , Aeroplanes
from datetime import datetime
 

#base class
class TestBase(TestCase):#inheriting testbase class
    def create_app(self):#creates instance of an app,returning created app
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='Test_SECRET_KEY', #UPDATE:secret key
                Debug=True,
                WTF_CSRF_ENABLED=False
                
                )
        return app
    def setUp(self): #fetching database
        """
        Will be called before every test
        """
      
        db.create_all()#create db

        first_aeroplane = Aeroplanes(
            model_number = "818",
            number_of_seats =  "22",
            company_owned_by = "Vueling"
        )
        db.session.add(first_aeroplane) #adds to database
        db.session.commit()

        first_flight = Flights(
            departure_date = datetime(2021,5,9),
            arrival_date =  datetime(2022,4,7),
            arrival_destination = "Malta",
            direct_flight = True,
            flight_price = "555.98",
            fk_aeroplane_id = "1",
        )
        db.session.add(first_flight)
        db.session.commit()
#making sure databse isn't empty
        

    def tearDown(self): #closes database session
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):    #testing homepage loads test views, inheriting test views. all attributes in test base will be avaliable in test views.
    def testing_home(self):
        response = self.client.get(url_for ('home'))
        self.assertEqual(response.status_code, 200)


class TestViewingCreateFlight(TestBase): #(Get) request for adding/creating a flight.
    def testing_create_flight_get(self):
        response = self.client.get(url_for('create_flight'))
        self.assertIn(b'flight', response.data)


class TestValidateCreateFlight(TestBase):
    def testval(self):
        response = self.client.post(url_for('create_flight'))
        self.assertNotEqual('form_not_validate_on_submit', response.data)





class TestAddingFlight(TestBase): #tests CREATEting flight (post)
    def test_add_flight_post(self):
        response = self.client.post(url_for('create_flight'),
        data = dict( departure_date = (2021-5-9),
            arrival_date = (2021-5-10),
            arrival_destination = "Miami",
            direct_flight = False,
            flight_price = "567.98",
            fk_aeroplane_id = "6" 
        ),
            follow_redirects =True)
    
        self.assertIn(b"a", response.data) 

# Test CREATEting CREATING aeroplane (GET)

class TestViewingCreateAeroplane(TestBase):
    def testing_create_aeroplane_get(self):
        response = self.client.get(url_for('create_aeroplane'))
        self.assertIn(b'aeroplane', response.data) #do i need to add the airplane dictionary  


class TestAddingAeroplane(TestBase): #tests CREATEting Aeroplane (post)
    def test__add_post(self):
        response = self.client.post(url_for('create_aeroplane'),
        data = dict( model_number = "818",
                    number_of_seats =  "22",
                    company_owned_by = "Vueling"
        ), follow_redirects=True)
        
        self.assertIn(b"a", response.data) 


       
class TestViewAeroplane(TestBase):    #testing (READ) aeroplane page loads (get) 
    def testing_Aeroplane_view(self):
        response = self.client.get(url_for ('AllAeroplanes'))
        self.assertEqual(response.status_code, 200) 

class TestViewFlights(TestBase):    #testing (READ) flight page loads (get)
    def testing_Flights_view(self):
        response = self.client.get(url_for ('AllFlights'))
        self.assertEqual(response.status_code, 200) 


    class TestViewUpdateFlight(TestBase):     #testing update Flight page loads(GET)
        def testing_updating_Flight_view(self):
            response = self.client.get(url_for ('updateFlights'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Update a flight', response.data)

class Test_Updating_Flight(TestBase):  #Test updating an flight (POST)
    def testUpdateFlight(self):
        response=self.client.post(
            url_for('updateFlights', id=1),
            data = dict ( departure_date = datetime(2021,5,9),
            arrival_date = datetime (2021,5,1),
            arrival_destination = "Miami",
            direct_flight = False,
            flight_price = "567.98",
            fk_aeroplane_id = "6" 

            ),
            follow_redirects =True
        )
        self.assertIn(b'flight', response.data)



class TestViewUpdateAeroplane(TestBase):     #testing aeroplane page loads (get) (#post - because you are updating,performing)
    def testing_updating_Aeroplane_view(self):
        response = self.client.get(url_for ('updatePlane', id=1),
        follow_redirects =True)
        self.assertEqual(response.status_code, 200)     



class Test_Updating_aeroplane(TestBase): #Test update an aeroplane (POST)
    def testUpdateAeroplane(self):
        response=self.client.post(
            url_for('updatePlane', id=1),
            data = dict (  model_number = "818",
                    number_of_seats =  "22",
                    company_owned_by = "Vueling"

            ),
            follow_redirects =True
        )
        self.assertIn(b'aeroplane', response.data)



#deleting a flight GET

class Test_delete_flight(TestBase):
    def test_delete_flight(self):
        response = self.client.get(url_for('delete_flight', id=1),
        follow_redirects =True)
        self.assertNotIn(b'Malta',response.data)

 

#deleting a aeroplane GET
class Test_delete_aeroplane(TestBase):
    def test_delete_aeroplane(self):
        response = self.client.get(url_for('delete_plane', id=1,
        ),
        follow_redirects =True)
        self.assertNotIn(b'Vueling',response.data)








