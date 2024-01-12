# Base image for Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

ENV PYTHONPATH=/app

#copy the files into the container working directory
COPY ./app /app

# Copy the tests in the project directory into the app directory
# To be removed for Production
COPY ./tests /app/tests 

# Copy the requirements into the container working directory
COPY ./requirements.txt /app/requirements.txt

# TO send output to terminal without getting buffered
ENV PYTHONUNBUFFERED=1

# install the dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Expose the FASTAPI port
EXPOSE 8000

# TO send output to terminal without getting buffered
ENV PYTHONUNBUFFERED=1

# Set environment variable to prevent creation of __pycache__ directories
ENV PYTHONDONTWRITEBYTECODE 1

# Setup the commands to be run into the container image.
# For Development use this
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

#for Production use this
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
