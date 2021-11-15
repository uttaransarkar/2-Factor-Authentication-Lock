from Hand_Gesture import handgesture
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
    data = {}
    # Face Module
    name=facerecog()
    # user category determination
    category=data['category'][name]

    # Hand Module
    handgesture()
    # Latch Circuit