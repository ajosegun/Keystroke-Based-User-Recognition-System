import pickle
import boto3
import os

s3_bucket = os.environ.get('S3BUCKET')
model_key_path = os.environ.get('MODEL_PATH')


def load_model(model_name):
    # Load the model from the S3 bucket
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=s3_bucket, Key=f"{model_key_path}/{model_name}")
    model = pickle.loads(obj["Body"].read())
    return model


def predict(event, context):
    # Get the model name from the input
    model_type = event["Model"]

    # Load the corresponding model from disk
    if model_type == 'SVM':
        model = load_model('svm_model.joblib')
    elif model_type == 'RF':
        model = load_model('rf_model.joblib')

    elif model_type == 'XGB':
        model = load_model('xgb_model.joblib')

    else:
        return 'Error: Invalid model type', 400

    # Get the input features from the input
    features = [event["HT"]["Mean"], event["HT"]["STD"],
                event["PPT"]["Mean"], event["PPT"]["STD"],
                event["RRT"]["Mean"], event["RRT"]["STD"],
                event["RPT"]["Mean"], event["RPT"]["STD"]]
    # Make the prediction
    prediction = model.predict([features])[0]
    # Return the prediction
    return {"prediction": prediction}
