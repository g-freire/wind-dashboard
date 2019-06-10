cd angular_server
start npm start

SLEEP 10
cd ../flask_server
start python insert_wind_mongo.py
start python app.py

SLEEP 10
start "" "chrome" "http://127.0.0.1:3000/"

pause