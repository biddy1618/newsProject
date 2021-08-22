ARG APP_IMAGE=python:3.8-slim-buster

FROM ${APP_IMAGE}

LABEL "Author"="Dauren Baitursyn"

RUN apt update -y
# RUN apt install -y python3-pip
# RUN apt install -y libpq-dev
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
ENV FLASK_ENV="development"
ENV FLASK_APP="app"
CMD ["flask", "run", "-h", "0.0.0.0"]
