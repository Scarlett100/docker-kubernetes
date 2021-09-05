from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return "Welcome, are you ready to make your dream flight to the caribbean?!"

@app.route('/about')
def about():
   return 'On this website you can make a flight scheduele for a flight you would like to take'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
