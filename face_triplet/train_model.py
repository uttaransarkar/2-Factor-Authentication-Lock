# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import argparse
import pickle

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-e", "--embeddings", required=True,
# 	help="path to serialized db of facial embeddings")
# ap.add_argument("-r", "--recognizer", required=True,
# 	help="path to output model trained to recognize faces")
# ap.add_argument("-l", "--le", required=True,
# 	help="path to output label encoder")
# args = vars(ap.parse_args())

embeddings = 'face_triplet/output/embeddings.pickle' 
recognizer = 'face_triplet/output/recognizer.pickle' 
le = 'face_triplet/output/le.pickle'


def retrain_model():
	# load the face embeddings
	print("[INFO] loading face embeddings...")
	# data = pickle.loads(open(args["embeddings"], "rb").read())
	data = pickle.loads(open(embeddings, "rb").read())
	# encode the labels
	print("[INFO] encoding labels...")
	label_encoder = LabelEncoder()
	labels = label_encoder.fit_transform(data["names"])

	# train the model used to accept the 128-d embeddings of the face and
	# then produce the actual face recognition
	print("[INFO] training model...")
	recognizer_model = SVC(C=1.0, kernel="linear", probability=True)
	recognizer_model.fit(data["embeddings"], labels)

	# write the actual face recognition model to disk
	# f = open(args["recognizer"], "wb")
	f = open(recognizer,"wb")
	f.write(pickle.dumps(recognizer_model))
	f.close()
	# write the label encoder to disk
	# f = open(args["le"], "wb")
	f = open(le, "wb")
	f.write(pickle.dumps(label_encoder))
	f.close()

# retrain_model()

# Command to run:-
# python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle