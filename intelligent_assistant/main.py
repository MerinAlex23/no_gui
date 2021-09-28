from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import tkinter as tk

# lija

import time
from time import ctime
import webbrowser
import playsound
import os
import random
import pywhatkit
from gtts import gTTS
from tkinter import *
from PIL import ImageTk,Image





# def onclick():
#     print("button cick")

# root=tk.Tk()
# root.title("gui button")


# btn1=tk.Button(root,text="button 1",command=onclick)
# btn2=tk.Button(root,text="button 2")


# btn1.pack()
# btn2.pack()

# root.mainloop()




recognizer=speech_recognition.Recognizer()
speaker=tts.init()
speaker.setProperty('rate',150)
todo_list=['go shopping','clean room','record video']


def create_note():
    global recognizer
    speaker.say("what do you want to write onto your note?")
    speaker.runAndWait()

    done=False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)
                note=recognizer.recognize_google(audio)
                print('Recognizer voice :'+ note)  #lija
                note=note.lower()


                speaker.say("Choose a filename")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)

                filename=recognizer.recognize_google(audio)
                filename=filename.lower()

            with open(filename,'w') as f:
                f.write(note)
                done=True
                speaker.say("I successfully created the node {filename}")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()


def add_todo():
    global recognizer
    speaker.say('what do you want to add?')
    speaker.runAndWait()

    done=False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                audio=recognizer.listen(mic)

                item=recognizer.recognize_google(audio)
                todo_list.append(item)
                done=True

                speaker.say("I added {item} to the todo list!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()

def show_todos():

    speaker.say("the items on your todo list are the following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def hello():
    speaker.say("hello.What can i do for you?")
    speaker.runAndWait()

def quit():
    speaker.say("bye")
    speaker.runAndWait()
    sys.exit(0)


    
mappings={
    "greeting":hello,
    "create_note":create_note,
    "add_todos":add_todo,
    "show_todos":show_todos,
    "exit":quit
}

assistant=GenericAssistant('intents.json',intent_methods=mappings)
assistant.train_model()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio=recognizer.listen(mic)

            message=recognizer.recognize_google(audio)
            message=message.lower()

        assistant.request(message)

    except speech_recognition.UnknownValueError:
        recognizer=speech_recognition.Recognizer()



        

    
