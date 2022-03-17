import pyrebase
import Adafruit_DHT

config = {
  "apiKey": "AIzaSyCxNPSxlFGhj4m7JueFTZpT9ZtrCmlgMao",
  "authDomain": "kisan-seva-cac6d.firebaseapp.com",
  "databaseURL": "https://kisan-seva-cac6d-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "storageBucket": "kisan-seva-cac6d.appspot.com",
  "serviceAccount": "serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

sensor = Adafruit_DHT.DHT11
pin = 17
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#db.child('dht').child().remove()
data = {"Temperature": "{0:0.1f}".format(temperature),"Humidity": "{0:0.1f}".format(humidity)}
db.child('dht').push(data)

users = db.child('dht').get()
print(data)