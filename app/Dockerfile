# IMAGE
FROM python:3.10-slim-buster

# APP DIR
WORKDIR /usr/src/app

# PYTHON
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# PIP PACKAGES
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

#RUN django-admin startproject app

# # AFTER BUILD COPY and START APP
# COPY ./entrypoint.sh .
# COPY . .
#
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
