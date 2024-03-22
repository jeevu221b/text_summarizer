# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY . .

RUN pip install pipreqs

RUN pipreqs .

RUN pip install -r requirements.txt

ENV FLASK_APP=web
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "--app", "web", "run"]

