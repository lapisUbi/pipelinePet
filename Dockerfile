# Uses python 3 version in a base image
FROM python:3.11-slim

# App directory
WORKDIR /app

# Copy requirements and installs it
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY app.py .

#Set port env variable
ENV PORT=9000
#Expose the port so our computer can acces it
EXPOSE 9000

CMD ["python", "app.py"]
