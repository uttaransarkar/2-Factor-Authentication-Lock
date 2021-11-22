import json
# from Hand_Gesture import handgesture
from face_triplet.recognize_video import facerecog



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
    file = open("./face_triplet/users_register.json","r")
    data = json.load(file)

    # Face Module
    name,category=facerecog()


    # Hand Module
    # handgesture()
    # Latch Circuit

start()