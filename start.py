import json
# from Hand_Gesture import handgesture
from face_triplet.recognize_video import *


'''
    facerecog()
        input : 
        output : name , confidence

    handgesture()
        input : 
        output : list
'''
def start():
    # Get User_Register Dictionary
    file = open("./users_register.json","r")
    data = json.load(file)

    # Face Module
    name,category=facerecog()
    print(name,category)

    # Categorization Logic
    if category.lower()=='master':
        # Matching password
        attempts = 1
        match = False
        while attempts<=3:
            # Hand Gesture Code Run - return sequence

            # Match Password
            match = True
            ## 
            if match:
                # Latch Activate
                print("Access Granted.")
                break
            else:
                print("Wrong password. Try again")
                attempts+=1

        
        print("User Name : ",name)
    elif category.lower()=='known':
        # Text to Speech Code Run
        print("User Name : ",name)
    else:
        # Text to Speech Code Run "Unknown"
        print("Unknown User")

start()