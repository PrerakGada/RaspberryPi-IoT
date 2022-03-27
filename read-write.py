import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
buzzer = 31
blue = 38
green = 37
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def read():
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        return text
        
    finally:
        pass


def buzz():
    for x in range(2):
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(buzzer, GPIO.LOW)
        sleep(0.1)


def write(text):
    reader = SimpleMFRC522()
    try:
        reader.write(text)
        print('Written')
    finally:
        pass
    
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: # Run forever
    #IN Data
    if GPIO.input(10) == GPIO.HIGH:
        GPIO.output(green, GPIO.HIGH)
        name = read()
        
        date = dt.strftime("%d %B %Y")
        time = dt.strftime("%I:%M %p")
        day = dt.strftime("%A, ")
        db.collection('workers').document(name).collection('attendance').document(date).update(
        {
            'in': time,
        }
    )
        
        buzz()
        GPIO.output(green, GPIO.LOW)
        
        
    #OUT Data
    if GPIO.input(12) == GPIO.HIGH:
        GPIO.output(blue, GPIO.HIGH)
        print(read())
        buzz()
        GPIO.output(blue, GPIO.LOW)
        
