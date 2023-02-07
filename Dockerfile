# Base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py", "--host", "0.0.0.0", "--port", "5000"]

EXPOSE 5000