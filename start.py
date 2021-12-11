import json
import pyttsx3
from capstone_gesture_control import *
from capstone_gesture_control.capstone_hand_ges import handgesture
from face_triplet.recognize_video import *

'''
    facerecog()
        input : 
        output : name , confidence

    handgesture()
        input : 
        output : list
'''
password = [0,1,2,3,4,5]
text_speech = pyttsx3.init()

def start():
    access=False
    # Get User_Register Dictionary
    # file = open("./users_register.json","r")
    # data = json.load(file)

    # Face Module
    name,category=facerecog()
    print(name,category)
    text_speech.say("{} has arrived".format(name))
    text_speech.runAndWait()

    # Categorization Logic
    if category.lower()=='master':
        # Matching password
        attempts = 1
        match = False
        while attempts<=3:
            text_speech.say("Please enter passcode")
            text_speech.runAndWait()
            # Hand Gesture Code Run - return sequence
            ans = handgesture()
            # Match Password
            match = ans == password
            if match:
                # Latch Activate
                print("Access Granted.")
                text_speech.say("Access Granted")
                text_speech.runAndWait()
                access=True
                break
            else:
                print("Wrong password. Try again")
                attempts+=1
    elif category.lower()=='known':
        # Text to Speech Code Run
        print("User Name : ",name)
        text_speech.say(name)
        text_speech.runAndWait()
    else:
        # Text to Speech Code Run "Unknown"
        print("Unknown User")
    return access

# start()
