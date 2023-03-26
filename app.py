from flask import Flask, request
import joblib
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the model type from the request body
    model_type = request.json['Model']

    # Get the input features from the request body
    ht_mean = request.json['HT']['Mean']
    ht_std = request.json['HT']['STD']
    rpt_mean = request.json['RPT']['Mean']
    rpt_std = request.json['RPT']['STD']
    ppt_mean = request.json['PPT']['Mean']
    ppt_std = request.json['PPT']['STD']
    rrt_mean = request.json['RRT']['Mean']
    rrt_std = request.json['RRT']['STD']

    # Load the corresponding model from disk
    if model_type == 'SVM':
        with open('svm_model.pkl', 'rb') as f:
            model = pickle.load(f)
    elif model_type == 'RF':
        with open('rf_model.pkl', 'rb') as f:
            model = pickle.load(f)
    elif model_type == 'XGB':
        print(xgb.__version__)
        with open('xgb_model.pkl', 'rb') as f:
            model = pickle.load(f)

        X = np.array(X).reshape((1,-1))

    else:
        return 'Error: Invalid model type', 400

    X = [[ht_mean, ht_std, rpt_mean, rpt_std, ppt_mean, ppt_std, rrt_mean, rrt_std]]

    # Make a prediction using the loaded model
    y_pred = model.predict(X)

    # Return the prediction result
    return str(y_pred[0]), 200

if __name__ == '__main__':
    app.run()
