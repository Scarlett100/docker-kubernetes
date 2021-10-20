#!/bin/bash 
sudo apt-get update
sudo apt install -y python3 python3-pip gunicorn
git clone https://github.com/Scarlett100/Flight_CRUD_App.git
cd./FLIGHT_CRUD_APP/flight
SECRET_KEY=ngjtnggjengjwnjrtj
export SECRET_KEY
pip3 install -r requirements.txt
python3 create.py
gunicorn -D --workers=4 --bind=0.0.0.0:5000 app:app
  