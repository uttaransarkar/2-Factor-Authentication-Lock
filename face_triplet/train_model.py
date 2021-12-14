# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import argparse
import pickle
from pycaret.classification import *
import pandas as pd

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

def preprocess_data(labels,data):
    y=pd.DataFrame(labels,columns=['label'])
    df=pd.DataFrame(data["embeddings"])
    dfp=pd.concat([df,y],axis=1)
    return dfp

def get_best_models_by(model,m,param,n):
    print("[INFO] Getting Best Model by {}".format(param))
    maxscore=0
    argmaxscore=-1
    count=0
    for i in range(len(m)):
        if i == n:
            break
        if m.iloc[i][param]<1 and m.iloc[i][param]>maxscore:
            maxscore=m.iloc[i][param]
            argmaxscore=i
    return model[argmaxscore]

def get_best_model(modellist):
    freq = {}
    for model in modellist:
        if model in freq:
            freq[model] += 1
        else:
            freq[model] = 1
    maxvalue = 0
    for key, value in freq.items():
        if value>maxvalue:
            maxvalue = value
            bestmodel = key
    return bestmodel

def best_model_finder(labels,data):
    print("[INFO] Preprocessing Data for Pycaret...")
    df=preprocess_data(labels,data)
    print("[INFO] Setting up Pycaret...")
    clf=setup(data=df, target='label', normalize=True, normalize_method='zscore',data_split_shuffle=False,fold=12)
    n=18
    print("[INFO] Compare Model Analysis using Pycaret...")
    model=compare_models(n_select=n)
    m = pull()
    params = ['Accuracy','AUC','Recall','Prec.','F1','Kappa','MCC']
    modellist = []
    for param in params:
        modellist.append(get_best_models_by(model,m,param,n))
    print("[INFO] Getting Best Model...")
    bestmodel=get_best_model(modellist)
    print('Best Model : ',bestmodel)
    print("[INFO] Getting Best Model Parameters using Hyperparameter Tuning...")
    tuned_model = tune_model(bestmodel)
    print('Best Model Tuned : ',tuned_model)
    return tuned_model

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
	###################### 
	# recognizer_model = SVC(C=1.0, kernel="linear", probability=True)
	recognizer_model = best_model_finder(labels,data)
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