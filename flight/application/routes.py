@app.route('/')
@app.route('/home')
def home():
    return "Welcome, are you ready to make your dream flight to the caribbean?!"

@app.route('/about')
def about():
   return 'On this website you can make a flight scheduele for a flight you would like to take'