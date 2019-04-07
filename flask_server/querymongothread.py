class QueryMongoThread(Thread):
    def __init__(self):
        self.delay = 2
        super(QueryMongoThread, self).__init__()

    def getLastSample(self):
        print("Querying last record from db")
        while not thread_stop_event.isSet():
            cursor = collection.find().limit(1).sort("_id", -1)
            for doc in cursor:
                mongo_contract = doc
            print(mongo_contract['name'])
            print(mongo_contract['rotorSpeed'])

            socketio.emit( 'wind', {
                'name': mongo_contract['name'], 
                'rotorSpeed': mongo_contract['rotorSpeed'], 
                'activePower': mongo_contract['activePower'], 
                'reactivePower': mongo_contract['reactivePower'], 
                'pf': mongo_contract['pf'], 
                'totalEnergy': mongo_contract['totalEnergy'], 
                'windPrediction1': mongo_contract['windPrediction1'], 
                'windPrediction2': mongo_contract['windPrediction2'], 
                'windPrediction3': mongo_contract['windPrediction3'], 
                'bearingTemperature': mongo_contract['bearingTemperature'], 
                'bearingVibration': mongo_contract['bearingVibration'], 
                'bearingOil': mongo_contract['bearingOil']
                }, 
                namespace='/wind')

            sleep(self.delay)

    def run(self):
        self.getLastSample()

