import pymongo
from random import random, uniform
from time import sleep

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["streaming"]
collection = db["wind_0001"]

def generate_random_wind_contract():
    try:
        while 1:
            random_value_wind_rotor_speed = round(random()*1000, 2)
            random_value_active_power = round(random()*100, 2)
            random_value_reactive_power = round(random()*100, 2)
            random_value_power_factor = round(uniform(0.85, 1.0), 3)
            random_value_generated_power = round(random()*10, 2)
            random_value_wind_prediction_probability1 = round(uniform(0.1, 1.0), 2)
            random_value_wind_prediction_probability2 = round(uniform(0.2, 1.0), 2)
            random_value_wind_prediction_probability3 = round(uniform(0.3, 1.0), 2)
            random_value_bearing_temperature = round(uniform(0.25, 0.6)*1000, 1)
            random_value_bearing_vibration = round(uniform(0.01, 3.0), 2)
            random_value_bearing_oil = round(uniform(0.85, 1.0)*100, 1)

            wind_contract = {
                "name": "wind_power", 
                "rotorSpeed": random_value_wind_rotor_speed,
                "activePower": random_value_active_power,
                "reactivePower": random_value_reactive_power,
                "pf": random_value_power_factor,
                "totalEnergy": random_value_generated_power,
                "windPrediction1": random_value_wind_prediction_probability1,
                "windPrediction2": random_value_wind_prediction_probability2,
                "windPrediction3": random_value_wind_prediction_probability3,
                "bearingTemperature": random_value_bearing_temperature,
                "bearingVibration": random_value_bearing_vibration,
                "bearingOil": random_value_bearing_oil,
                }

            collection.insert_one(wind_contract)     
            print('Inserted value ', wind_contract)
            sleep(2)
            
    except Exception as e:print(e)
    finally:
        client.close()

if __name__ == '__main__':
    generate_random_wind_contract()