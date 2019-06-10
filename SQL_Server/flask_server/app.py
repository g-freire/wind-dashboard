# Start with a basic flask app webpage.
import pyodbc 
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context, jsonify,make_response, request
from random import random
from time import sleep, time
import json
from threading import Thread, Event
import pymongo  
from flask_cors import CORS
# from querymongothread import QueryMongoThread
# from ai_processor import AIProcessor
from sklearn.externals import joblib
from random import random, uniform

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = '!#@!6ce2fa3e-0ba4-!#@!ca3-a069-fe66941723e4!#@!'
app.config['DEBUG'] = True
socketio = SocketIO(app)

# aiProcessor = AIProcessor()
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

            a = row[1] * round(random()*.221230, 2)
            b = row[1] * round(uniform(0.1, 1.0), 2)
            c = row[1] * round(random()*100, 2)
            print('a:',a,'b:',b,'c:',c)

            model_from_joblib = joblib.load('xgb-3features-fmc.joblib')
            model_prediction = model_from_joblib.predict([a, b, c])
            print("Predicted value:", model_prediction)
            sleep(self.delay)

    def run(self):
        self.getLastSample()

# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     try:
#         start = time.time()
#         post_body = json.loads(request.data.decode('utf-8'))
#
#         sensor1 = float(post_body['sensor1'])
#         sensor2 = float(post_body['sensor2'])
#         sensor3 = float(post_body['sensor3'])
#
#         data = aiProcessor.predict_pump_output(sensor1, sensor2, sensor3)
#
#         return str(data[0])
#     except Exception as e:print(e)

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
    
    return 'SQL SERVER API'

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    socketio.run(app)

