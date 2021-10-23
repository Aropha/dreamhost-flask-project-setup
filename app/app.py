# import numpy as np
# import pandas as pd
from flask import Flask, render_template, request, make_response, Response
# import pickle
# from rdkit import DataStructs, Chem
# from rdkit.Chem import AllChem
# from rdkit.Chem.rdMolDescriptors import GetMACCSKeysFingerprint
import time, random, string, os




################################################## General ###################################################
app = Flask(__name__)


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/aerobic-biodegradation/about.html')
def AB_about():
    return render_template('/aerobic-biodegradation/about.html')


## Remove the automatically generated csv files
def remove_files():
    # specify the path
    path = "app/static/prediction-files/"
    # specify the days (files older than 30 days are removed)
    days = 10
    # converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)
    # checking whether the file is present in path or not

    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)) and 'Prediction-' in i:
            # comparing the days
            if seconds >= os.stat(i).st_ctime:
                # remove the file i
                os.remove(i)



###################################### Aerobic biodegradation classification ###################################################

from module import Aropha_ABClassifier ## Change to "from app.module import ABClassifier" during production


@app.route('/aerobic-biodegradation/classification/about.html')
def ABClassifer_about():
    return render_template('/aerobic-biodegradation/classification/about.html')


@app.route('/aerobic-biodegradation/classification/predictor.html')
def ABClassifer_predictor():
    return render_template('/aerobic-biodegradation/classification/predictor.html')


@app.route('/aerobic-biodegradation/classification/jupyter.html')
def ABClassifer_jupyter():
    return render_template('/aerobic-biodegradation/classification/jupyter.html')


#To use the predict button for smiles
@app.route('/aerobic-biodegradation/classification/predict-smiles.html', methods=['POST', 'GET'])
def ABClassifer_predict_smiles():
    return Aropha_ABClassifier.predict_smiles()


#To use the predict button for a file
@app.route('/aerobic-biodegradation/classification/predict-file.html', methods=['POST', 'GET'])
def ABClassifer_predict_file():
    return Aropha_ABClassifier.predict_file()


@app.route('/aerobic-biodegradation/classification/dataset.html')
def ABClassifer_dataset():
    return Aropha_ABClassifier.dataset()




###################################### Aerobic biodegradation regression ###################################################

from module import Aropha_ABRegressor ## Change to "from app.module import ABRegressor" during production


@app.route('/aerobic-biodegradation/regression/about.html')
def ABRegressor_about():
    return render_template('/aerobic-biodegradation/regression/about.html')


@app.route('/aerobic-biodegradation/regression/predictor.html')
def ABRegressor_predictor():
    return render_template('/aerobic-biodegradation/regression/predictor.html')


@app.route('/aerobic-biodegradation/regression/jupyter.html')
def ABRegressor_jupyter():
    return render_template('/aerobic-biodegradation/regression/jupyter.html')


#To use the predict button for smiles
@app.route('/aerobic-biodegradation/regression/predict-smiles.html', methods=['POST', 'GET'])
def ABRegressor_predict_smiles():
    return Aropha_ABRegressor.predict_smiles()


#To use the predict button for a file
@app.route('/aerobic-biodegradation/regression/predict-file.html', methods=['POST', 'GET'])
def ABRegressor_predict_file():
    return Aropha_ABRegressor.predict_file()


@app.route('/aerobic-biodegradation/regression/dataset.html')
def ABRegressor_dataset():
    return Aropha_ABRegressor.dataset()










#Starting the Flask Server 
if __name__ == '__main__':
    app.debug = True
    app.run()