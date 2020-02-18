# http-service

I have used Python Flask web framework to create the http service

Requirements:

* Python3
* Python3-venv
* Docker: V19.03.6

** I used python virtual env to run this web service **

## Steps to reproduce:

* Clone this repo
* Start Python virtual environment

``` bash
python3 -m venv flask
```

* Activate the virtual environment
``` bash
source flask/bin/activate
```

* Once you are in the flask venv, install flask 
``` bash
flask/bin/pip install flask
```

* Give executable permissions to the app.py
``` bash
chmod +x app.py
```

* Run the application
``` bash
./app.py 
```
* If you don't specify any port as a command line argument, by default the application will be running on port 8080. You can access the service at:

http://127.0.0.1:8080

* If you want to specify a port other than 8080, pass it as a command line argument
``` bash
./app.py 8181
```
http://127.0.0.1:8181

## Running the service with Dockerfile

A Dockerfile is written to run this service as a container

* Build a docker image with the Dockerfile

``` bash
docker build -t http-service:v1 . 
```

* Run docker container with the image built in above step
``` bash
docker run -d -p 8080:8080 http-service:v1 
```

* Application can be accessed at:
http://127.0.0.1:8080
