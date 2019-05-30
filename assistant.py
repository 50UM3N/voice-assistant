import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import numpy as np
import cv2
import pickle
import time

delay=40    ###for 15 minutes delay 
close_time=time.time()+delay

engine = pyttsx3.init()
client = wolframalpha.Client(put wolframpalpha api key)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant root')
speak('How may I help you?')


def mc():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

def mc1():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query
        

if __name__ == '__main__':

    while True:
        q = mc1()
        q = q.lower()
        if 'hello' in q:
            speak(' Yes sir what can I help you')
            query = mc()
            query = query.lower()
        
            if 'open youtube' in query:
                speak('okay')
                webbrowser.open('www.youtube.com')

            elif 'open google' in query:
                speak('okay')
                webbrowser.open('www.google.co.in')

            elif 'open gmail' in query:
                speak('okay')
                webbrowser.open('www.gmail.com')

            elif "what\'s up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))

            elif 'send a mail' in query:
                speak('Who is the recipient? ')
                recpt = mc()
                recpt = recpt.lower()
                
                if 'me' in recpt :
                    email = '#'#put primary email address

                elif 'maa' in recpt :
                    email = '#' #mom's email address

                elif 'dad' in recpt :
                    email = '' #daad email address

                elif 'moin' in recpt :
                    email = '#' #friens'd email address

                else:
                    email = 'ninjahydra357@gmail.com'
                    speak('Can not found persion I send the mail to me')

                try:
                    speak('What is the subject sir')
                    subject = mc()
                    speak("What should I say sir?")
                    msg = mc()
                    content = 'Subject: {}\n\n{}'.format(subject, msg)
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login( put secondary email address, password of that address)
                    server.sendmail( secondary email address, email, content)
                    server.close()
                    speak('Email sent!')
                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

            elif 'nothing' in query or 'abort' in query or 'stop' in query:
                speak('okay')
                speak('Bye Sir, have a good day.')
                sys.exit()
           
            elif 'hello' in query:
                speak('Hello Sir')

            elif 'bye' in query:
                speak('Bye Sir, have a good day.')
                sys.exit()
                                    
            elif 'play music' in query:
                music_folder = '/root/Desktop/' #directory for linux if you use windows then put your music folder
                music = ['music1', 'music2'] #name of the musics
                random_music = music_folder + random.choice(music) + '.mp3'
                speak('Okay, here is your music! Enjoy!')
                os.system('rhythmbox ' + random_music) #rythmbox is the music player pyt your music player name 

            elif 'who is there' in query:
                cap = cv2.VideoCapture(0)
                faceCascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                recognizer.read("./recognizers/face-trainner.yml")
                labels = {"person_name": 1}

                with open("pickles/face-labels.pickle", 'rb') as f:
                	og_labels = pickle.load(f)
                	labels = {v:k for k,v in og_labels.items()}
                name = 'null'

                while(True):
                    ret, frame = cap.read()
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

                    for(x,y,w,h) in faces:
                        roiGray = gray[y:y+h, x:x+w]
                        roiColor = gray[y:y+h, x:x+w]
                        id_, conf = recognizer.predict(roiGray)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        name = labels[id_]
                        color = (255, 255, 255)
                        stroke = 1
                        cv2.putText(frame, name, (x,y-8), font, 1, color, stroke, cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

                    if (time.time()>close_time) :
                         break

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break

                cap.release()
                cv2.destroyAllWindows()
                #name of the FR persions
                if '#' in name: #you
                    a = ['you r looking gorgious today', 'your hairstyle is cool sir', 'Take care sir']
                    speak('This is you sir ' + random.choice(a))

                elif '#' in name : #your mom
                    speak('She is your mom sir. how ar you maam')
                # add yourself
                else:
                    speak('Unkown person alart')
                    name = 'null'

            else:
                speak('Searching...')
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak('Got it.')
                        speak(results)

                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak('Got it.')
                        speak('WIKIPEDIA says - ')
                        speak(results)

                except:
                    webbrowser.open('www.google.com')

            speak('Next Command! Sir!')
        

