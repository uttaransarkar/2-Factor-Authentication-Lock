from face_triplet.build_dataset import *
from face_triplet.extract_embeddings import *
from face_triplet.train_model import *

def add_user():
    print(len(next(os.walk('face_triplet/dataset/'))[1]))
    # Build Data, Take Input
    build_data()

    # Extract Embeddings
    extract_embeddings()

    # Retrain Model

    print(len(next(os.walk('face_triplet/dataset/'))[1]))
    if len(next(os.walk('face_triplet/dataset/'))[1])>1:
        retrain_model()


add_user()