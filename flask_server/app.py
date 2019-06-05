# Start with a basic flask app webpage.
import pyodbc 
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
import pymongo  
from flask_cors import CORS
# from querymongothread import QueryMongoThread

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = '!#@!6ce2fa3e-0ba4-!#@!ca3-a069-fe66941723e4!#@!'
app.config['DEBUG'] = True
socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()

server = '127.0.0.1,1433' 
database = 'client_sensors' 
username = 'SA' 
password = '1q2w3e%&!' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

class QueryMongoThread(Thread):
    def __init__(self):
        self.delay = 2
        super(QueryMongoThread, self).__init__()

    def getLastSample(self):
        print("Querying last record from db")
        while not thread_stop_event.isSet():
            cursor.execute("SELECT TOP(1) * FROM [client_sensors].[dbo].[sensors] ORDER BY timestamps DESC") 
            row = cursor.fetchone()
            print(row)
            sleep(self.delay)

    def run(self):
        self.getLastSample()


@socketio.on('connect', namespace='/wind')
def test_connect():
    global thread
    print('Client connected')

    if not thread.isAlive():
        print("Starting QueryMongo main Thread")
        thread = QueryMongoThread()
        thread.start()

@socketio.on('disconnect', namespace='/wind')
def test_disconnect():
    print('Client disconnected')

@app.route('/')
def index():
    global thread
    print('Client connected')

    if not thread.isAlive():
        print("Starting QueryMongo main Thread")
        thread = QueryMongoThread()
        thread.start()
    
    return 'Wind Power API'

if __name__ == '__main__':
    socketio.run(app)

