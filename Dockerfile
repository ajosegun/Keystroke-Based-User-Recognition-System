# Use an official Python runtime as a parent image
FROM public.ecr.aws/lambda/python:3.8

RUN yum -y install libgomp

COPY . ${LAMBDA_TASK_ROOT}
COPY requirements.txt  .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Expose port 80 for the Flask app
EXPOSE 80

CMD ["app.handler"]
