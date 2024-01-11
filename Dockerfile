# Base image for Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

#copy the files into the container working directory
COPY ./app /app

# Copy the requirements into the container working directory
COPY ./requirements.txt /app/requirements.txt

# install the dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Expose the FASTAPI port
EXPOSE 8000

# Setup the commands to be run into the container image.
# For Development use this
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

#for Production use this
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]