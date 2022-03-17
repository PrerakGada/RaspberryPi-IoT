
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import Adafruit_DHT
import time

cred = credentials.Certificate("serviceAccountCredentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

while True:
    sensor = Adafruit_DHT.DHT11
    pin = 17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print(temperature, humidity)
    db.collection('outputDevices').document('dht').update(
         {
             'Temperature' : str(temperature),
             'Humidity': str(humidity)
         }
     )
    time.sleep(5);
