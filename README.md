## Keystroke-Based User Recognition System (MLOPs)

Read the Objectives [here](./objectives.md)
Follow the AWS Deployment Steps [here](./cloud_deployment.md)

### Technologies Overview

| Technology | Purpose |
| --- | --- |
| Python | Programming language used for the inference code and other scripts |
| numpy | Library used for numerical operations in Python |
| pandas | Library used for data analysis in Python |
| scikit-learn | Library used for machine learning in Python |
| Flask | Library used for building APIs in Python |
| Docker | Tool used for containerization |
| AWS Lambda | Serverless compute service used to run the inference code |
| AWS Elastic Container Registry (ECR) | Container image registry used to store and deploy the Docker image |
| AWS API Gateway | Service used to manage and expose the Lambda function as an API |
| boto3 | Python library used to interact with AWS services |
| Jupyter Notebook | Environment used to develop the machine learning models |


### System Architecture for Machine Learning Inference

This system architecture enables serverless inference for machine learning models using Amazon Web Services (AWS) cloud services. The architecture includes several modules and services that work together to provide a seamless experience for HTTP clients that want to use the machine learning models.

<img width="517" alt="image" src="https://user-images.githubusercontent.com/94995067/227769215-12e9a465-7818-4e22-9021-2cbbe9d6d928.png">

### Overview
The architecture is shown in Figure 1, which provides a comprehensive diagram of the various modules and services involved. The following steps summarize the system's workflow:

1. Machine learning models were created in a Jupyter Notebook and exported as pickle files.
2. The inference code was written in Python and packaged with the model in a Docker container image.
3. The container image was uploaded to Amazon Elastic Container Registry (ECR).
4. A lambda function was created to perform the serverless inference.
5. An Amazon API Gateway receives requests from HTTP clients and triggers the lambda function.

### How to Use
To use this system architecture for serverless inference with machine learning models, follow these steps:

1. Create machine learning models using this [Jupyter Notebook](./model.ipynb) and export them as pickle files.
2. The inference code is written Python ([Flask](./app.py) and [AWS Lambda](./lambda_function.py)), and packaged with the model in a Docker container image.
4. Upload the container image to Amazon ECR.
5. Create a lambda function (lambda_function.py) to perform the serverless inference using the container image from Amazon ECR.
6. Create an API Gateway that receives requests from HTTP clients and triggers the lambda function.

After completing these steps, you will have a fully-functional system that can perform serverless inference with machine learning models.
