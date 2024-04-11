from flask import Flask, redirect, render_template, request


app = Flask(__name__)

#the app.py function to render index page
@app.get('/')
def index():
    return render_template('index.html')

#renders events page and lists the current database
@app.get('/events')
def list_all_events():
    # TODO: Complete Feature 1
    list_all_events = request.form.get('events')
    Name = request.form.get('name')
    EventName = request.form.get('director')
    Time = request.form.get('time')
    return render_template('list_all_events.html', list_events_active=True, event_list = list_all_events.get_all_events())

#calls the create events page for the main method of user input
@app.get('/events/new')
def create_events_form():
    return render_template('create_events_form.html')

#create movies implements the format for the create movies function
@app.post('/movies')
def create_movie():
    #basic input for events
    Name = request.form.get('name')
    EventName = request.form.get('director')
    Time = request.form.get('time')
    #temp address input
    Address = request.form.get('address')
    
    #to be changed in next ver
    movie_repository.create_movie(Name, EventName, Time, Address)
    return redirect('/movies')


#event search
@app.get('/events/search')
def search_event():
    #todo
    return render_template('search_event.html', search_active=True)

