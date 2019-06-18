from multiprocessing import Pool
from random import random, uniform
from time import sleep
import datetime
import pyodbc 

server = '127.0.0.1,1433' 
database = 'client_sensors' 
username = 'SA' 
password = '1q2w3e%&!' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


def insert_generator():
    try:
        while 1:
            timestamp = str(datetime.datetime.now())
            random_inputs = round(uniform(0.25, 0.6)*1000, 1)
            sensor_value = random_inputs
            print("INSERT INTO [client_sensors].[dbo].[sensors] VALUES('{}',{})".format(timestamp, sensor_value))
            cursor.execute("INSERT INTO [client_sensors].[dbo].[sensors] VALUES('{}',{})".format(timestamp, sensor_value))
            cnxn.commit()
            # sleep(2)
            
    except Exception as e:print(e)
    finally:
        cnxn.close()

if __name__ == '__main__':
    print("---------------------------------------------- ")
    print("Start ramdom data generator ")
    # print("Number of cpu : ", multiprocessing.cpu_count())
    print("---------------------------------------------- ")
    insert_generator()

    # random_inputs = [round(uniform(0.25, 0.6)*1000, 1)]
    # with Pool(4) as pool:
    #     report = pool.map(insert_generator(), [round(uniform(0.25, 0.6)*1000, 1) for x in xrange(20000000000000000000000000000000000000000000000000000000000000000000000000)])


    # p = Process(target=f, args=('bob',))
    # p.start()
    # p.join()