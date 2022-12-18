# ml-docker-api
build docker container for image classification with rest api service

# quick-start

- run ml-server `python3 app.py`

# packages

- opencv-python (linux ubuntu 18.04) `pip3 install opencv-python==3.2.0.7`

(from versions: 3.4.0.14, 3.4.10.37, 3.4.11.39, 3.4.11.41, 3.4.11.43, 3.4.11.45, 3.4.13.47, 3.4.15.55, 3.4.16.57, 3.4.16.59, 3.4.17.61, 3.4.17.63, 3.4.18.65, 4.3.0.38, 4.4.0.40, 4.4.0.42, 4.4.0.44, 4.4.0.46, 4.5.1.48, 4.5.3.56, 4.5.4.58, 4.5.4.60, 4.5.5.62, 4.5.5.64, 4.6.0.66)

- tensorflow `pip3 install tensorflow`
- flask `pip3 install flask`
- flask-cors `pip3 install flask-cors`
- pillow `pip3 install Pillow`

# build docker image

    FROM ubuntu:latest # download base image
    WORKDIR /app # create floder inside the container
    RUN apt-get update -y
    RUN apt-get install -y python3-pip python3-dev build-essential hdf5-tools libgl1 libgtk2.0-dev
    COPY . /app # copy source into your floder
    RUN pip3 install -r requirements.txt # run setup
    EXPOSE 8080 # map port
    CMD ["python3", "my_api.py"] # run server

**Note:**

There are 3 way to install python-packages in the container

- install python-packages via requirements.txt (not working always)

    RUN pip3 install -r requirements.txt

- install python-packages via commands

    RUN pip3 install tensorflow
    RUN pip3 install opencv-python
    RUN pip3 install flask
    RUN pip3 install flask-cors
    RUN pip3 install Pillow

- copy virtual enviroment from local

    COPY . /app
    RUN source env/bin/activate

# deploy docker

- build docker image name `ml-app` tag `1.0`: `sudo docker build -t ml-app:1.0`

- run docker build container name `con1`: `sudo docker run -it --name con1 ml-app:1.0`

- stop docker container: `sudo docker stop con1` (if permission denied run `sudo aa-remove-unknown`)

- jump in docker container `sudo docker exec -it con1 bash`

- run docker again `sudo docker start con1`

# references

[source](https://github.com/thangnch/MiAI_Docker_DeepLearning)
