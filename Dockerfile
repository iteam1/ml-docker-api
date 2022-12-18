FROM ubuntu:latest

WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential hdf5-tools libgl1 libgtk2.0-dev
RUN pip3 install virtualenv

COPY . /app

RUN pip3 install tensorflow
RUN pip3 install opencv-python
RUN pip3 install flask
RUN pip3 install flask-cors
RUN pip3 install Pillow

RUN source env/bin/activate

EXPOSE 8080

CMD ["python3","app.py"]
