# ml-docker-api
build docker container for image classification with rest api service

# quick-start

- run ml-server `python3 app.py`

# packages

- opencv-python (linux ubuntu 18.04) `pip3 install opencv-python==3.2.0.7`
- tensorflow `pip3 install tensorflow`
- flask `pip3 install flask`
- flask-cors `pip3 install flask-cors`
- pillow `pip3 install Pillow`

# build docker image

    FROM ubuntu:latest
    WORKDIR /app
    RUN apt-get update -y
    RUN apt-get install -y python3-pip python3-dev build-essential hdf5-tools libgl1 libgtk2.0-dev
    COPY . /app
    RUN pip3 install -r setup.txt
    EXPOSE 8080
    CMD ["python3", "my_api.py"]

# deploy docker

# references

[source](https://github.com/thangnch/MiAI_Docker_DeepLearning)
