# Model Scoring Deployed in Flask

## Steps
1. model.py: Train a model and save a model.pkl file
2. app.py: Create Flask app that will expose a POST method

## Build docker image with the following docker commands
1. Create docker image: "docker build -t my_iris:v1 ." -> Creates image with the name "my_iris:v1"
2. Run docker container: "docker container run -d -p 5000:5000 --name my_iris_app my_iris:v1" -> runs a container with the name "my_iris_app" from the image "my_iris:v1"


The docker container is going to expose the model in http://localhost:5000/api

You can check it through different ways:
- request.py: this script uses requests python library to send POST method to the model
- Curl: you can use curl from a terminal in your computer (please be careful with the differences for curl between linux/windows)
- Talend: you can use any API tester helper in your browser.

ok
