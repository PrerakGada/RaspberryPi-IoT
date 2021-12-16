from tkinter import *
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
buzzer = 31
red = 37
green = 33
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

window = Tk()
window.title('Practical')
window.geometry('350x200')

def read():
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        readLabel.config(text=f"User: {str(text).strip()}")
        if str(text).strip() == "prerak":
            GPIO.output(green, GPIO.HIGH)
            GPIO.output(buzzer, GPIO.HIGH)
            sleep(0.3)
            GPIO.output(buzzer, GPIO.LOW)
            GPIO.output(green, GPIO.LOW)
            status.config(text="Authenticated!")
        else:
            GPIO.output(red, GPIO.HIGH)
            for x in range(3):
                GPIO.output(buzzer, GPIO.HIGH)
                sleep(0.1)
                GPIO.output(buzzer, GPIO.LOW)
                sleep(0.1)
            GPIO.output(red, GPIO.LOW)
            status.config(text="Invalid ID")
    finally:
        pass
        
def write(text):
    reader = SimpleMFRC522()
    try:
        reader.write(text)
        status.config(text="Written")
        writeBox.delete(0, END)
    finally:
        pass
    
readLabel = Label(window, text="Read an RFID", bg="white")
readLabel.place(x=140,y=35)
readBtn = Button(window, text="Read RFID", command=read)
readBtn.place(x=40, y=30)

writeBox = Entry(window, width=13)
writeBox.place(x=40, y=83)
writeBtn = Button(window, text="Write RFID", command=lambda: write(writeBox.get()))
writeBtn.place(x=165,y=80)

status = Label(window, text='', width=20)
status.place(x=80, y=150)
 
window.mainloop()
