### AWS Cloud Deployment Steps for Serving the Keystroke Based User Recognition System Model API

These are the step-by-step instructions to develop the deployment pipeline and serve a machine learning model API using AWS Lambda, AWS Elastic Container Registry (ECR), and AWS API Gateway.

### Requirements
1. AWS CLI
2. AWS Account

### Steps
Clone this repo in your local system.

The contents of the folder should include the following files:

`App.py`
`Dockerfile`
`Requirements.txt`
`Rf_model.pkl`
`Svm_model.pkl`
`Xgb_model.pkl`

Login to AWS ECR by running the following command in your terminal:

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```

Run the following command to log in to AWS:

```
aws ecr login
```

Create a repository inside AWS Elastic Container Registry by running the following command:

```
aws ecr create-repository --repository-name threatfabric --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
```

Build the Docker image by running the following command:

```
docker build -t keystroke_based_user_recognition .
```

Tag the container image by running the following command:

```
docker tag keystroke_based_user_recognition <awsaccountid>.dkr.ecr.us-east-1.amazonaws.com/keystroke_based_user_recognition
```

Replace <awsaccountid> with your AWS account ID.

Push the image to ECR by running the following command:

```
docker push <awsaccountid>.dkr.ecr.us-east-1.amazonaws.com/keystroke_based_user_recognition:latest
```
  
Replace <awsaccountid> with your AWS account ID.

Go to the AWS Console and navigate to the AWS ECR page to verify that the repository with the image has been created.

Go to the AWS Lambda page and create a new lambda function. Select "Container Image" and browse the images to select the image you uploaded to ECR.
  
<img width="453" alt="image" src="https://user-images.githubusercontent.com/94995067/227770743-cfe759fb-5326-43a2-a538-4b06ef879bd0.png">

On the function overview page, click "Add Trigger".
  
<img width="668" alt="image" src="https://user-images.githubusercontent.com/94995067/227770983-9c9dfe73-3c23-470b-a5bf-438656fdd2ba.png">


On the next page, select the API Gateway and follow the instructions.
  
  <img width="453" alt="image" src="https://user-images.githubusercontent.com/94995067/227770691-7fdbf012-f8ec-4a35-8fd6-0dbdb8510a47.png">


Copy the API endpoint at the end of the process. You can also see the API Gateway trigger on the function page by navigating to "Configuration" and then "Triggers".
  


  
Test the API on any HTTP client such as Postman.
  
<img width="653" alt="image" src="https://user-images.githubusercontent.com/94995067/227770662-7097e89b-781b-4f58-9ea1-ca3dd98e24b7.png">

  
  
