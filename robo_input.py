import mysql.connector#to get connected to Mysql server database
import random;#to generate random numbers
from random import randint
import pyttsx3 #is to convert text to audio
import PyPDF2#ready any text in the pdf


speaker=pyttsx3.init()#initiating the module
speaker.say("welcome to hospital.please fill the details.")
speaker.runAndWait()
rate=speaker.getProperty('rate')
speaker.setProperty('rate',rate-20)#setting rate to the voice message

volume=speaker.getProperty('volume')

speaker.setProperty('volume',volume-5)#voice volume settings

voices=speaker.getProperty('voices')
for voice in voices:
   speaker.setProperty('voice',voice.id)


db1=mysql.connector.connect(host='localhost',user='bhargavi',password='Password!23',database='robo')

cur=db1.cursor()
s='insert into details values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'



speaker=pyttsx3.init()
speaker.say("enter your name" )
speaker.runAndWait()
name=input("enter your name\n") 

speaker=pyttsx3.init()
speaker.say("enter your age")
speaker.runAndWait()
age=input("enter your age\n")

speaker=pyttsx3.init()
speaker.say("enter your phone number")
speaker.runAndWait()
phone_number=input("enter your phone number\n")

speaker=pyttsx3.init()
speaker.say("enter your email-ID")
speaker.runAndWait()
email_id=input("enter your email ID\n")

speaker=pyttsx3.init()
speaker.say("enter your temperature")
speaker.runAndWait()
temperature=int(input("enter your temperature\n"))

speaker=pyttsx3.init()
speaker.say("enter your blood-pressure")
speaker.runAndWait()
blood_pressure=input("enter your blood pressure\n")

speaker=pyttsx3.init()
speaker.say("enter your oxygen-level")
speaker.runAndWait()
oxygen_level=input("enter your oxygen_level\n")

speaker=pyttsx3.init()
speaker.say("enter your height")
speaker.runAndWait()
height=input("enter your height\n")

speaker=pyttsx3.init()
speaker.say("enter your weight")
speaker.runAndWait()
weight=input("enter your weight\n")

speaker=pyttsx3.init()
speaker.say("your unique ID is")
speaker.runAndWait()
print('your unique_id is')

unique_unique=print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))

t=(name,age,phone_number,email_id,temperature,blood_pressure,oxygen_level,height,weight)

cur.execute(s,t)
speaker=pyttsx3.init()
speaker.say("dear,check the details you have given")
speaker.runAndWait()
print("('name','age','phone number','email-ID','temperature',blood pressure',oxygen level''height','weight')")
cur.execute("select *from details limit 1")
result=cur.fetchall()
for row in result:
    print(row)

db1.commit()


