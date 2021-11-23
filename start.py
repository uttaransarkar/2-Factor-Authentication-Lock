import json
# from Hand_Gesture import handgesture
from face_triplet.recognize_video import *
from face_triplet.build_dataset import *
from face_triplet.extract_embeddings import *
from face_triplet.train_model import *


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

def add_user():
    # Build Data, Take Input
    build_data()

    # Extract Embeddings
    extract_embeddings()
    
    print(len(next(os.walk('dir_name'))[1]))
    if len(next(os.walk('dir_name'))[1])>1:
        retrain_model()

    # Retrain Model
    

# start()
add_user()