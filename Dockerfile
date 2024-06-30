# FROM python:3.9-slim
# FROM python:3.12-slim
FROM public.ecr.aws/lambda/python:3.12

# Copy requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Copy function code
COPY src/ ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD ["query_db.lambda_handler"]