FROM python:3.7-stretch

EXPOSE 80

WORKDIR /app
RUN apt-get -y update
COPY requirements.txt ./
RUN  apt-get -y install python3-pip
RUN  pip3 install --no-cache-dir -r requirements.txt
RUN  pip3 install requests
RUN  pip3 install mysql-connector 
COPY . ./

LABEL maintainer="Hemanth C <hemanthvenki910@gmail.com>"
