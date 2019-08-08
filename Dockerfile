<<<<<<< HEAD
FROM python:3.6
=======
FROM ubuntu
>>>>>>> d85b0f274176c29ca1e705798a1ce3d776bc8612
MAINTAINER Team-Nano
ADD . /code
WORKDIR /code
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "run.py"]
