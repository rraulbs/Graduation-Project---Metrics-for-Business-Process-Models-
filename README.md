# Graduation-Project---Metrics-for-Business-Process-Models-

<h4 align="center"> 
	🚧  Project 🚀 Under construction...  🚧
</h4>

# :point_right: Getting Started
This page will bring you up to speed with the needed configurations and softwares to start working on the project.

# :point_right: Setup

:heavy_check_mark: Make sure you have an editor to work with code like VSCode or another one of your choice.

:heavy_check_mark: Make sure you have camunda modeler installed (version 4.3.0) <br>
https://downloads.camunda.cloud/release/camunda-modeler/4.3.0/

:heavy_check_mark: Make sure you have already installed both Docker Engine and Docker Compose.<br>
https://docs.docker.com/compose/install/compose-desktop/

:heavy_check_mark: Make sure you have all the images needed to run the project.
- [X] :dvd: docker.elastic.co/elasticsearch/elasticsearch:8.0.0 <br>
- [X] :dvd: docker.elastic.co/kibana/kibana:8.0.0 <br>
- [X] :dvd: mysql:5.6 <br>
- [X] :dvd: camunda/camunda-bpm-platform:latest <br>
- [X] :dvd: luarhub/staticmetrics <br>
- [X] :dvd: luarhub/dynamicmetrics <br>

Run the command below to pull the images (Example):
```
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.0.0
```

After pull all images, make sure it is all correct:

```
docker images
```

![image](https://user-images.githubusercontent.com/16651018/172214019-ce599148-9a10-46f1-8348-2902915f76bc.png)


:heavy_check_mark: Clone this project to a local folder


# :point_right: How to use

## Start the services

- Make sure your docker is up and running: start docker desktop.

- The docker-compose file is available in the following path: ***C:/.../Graduation-Project---Metrics-for-Business-Process-Models-/BusinessProcessDashboard/*** <br> Inside this folder, run the following command
```
	docker-compose -f docker-compose.yaml up -d
```
![image](https://user-images.githubusercontent.com/16651018/172227426-e88b1bb1-fd2e-498a-923d-1f3cb46c1357.png)
Done, the services are now up and running:
![image](https://user-images.githubusercontent.com/16651018/172265397-0f7cf837-bb50-4698-bf7d-a2b7ffbd08ba.png)

## Open a web browser
To have access to the services, open a web browser and enter the following ports:  <br>
:wrench: ***ElasticSearch (Kibana)***: http://localhost:5601/  ou http://127.0.0.1:5601/ <br>
:wrench: ***Camunda platform***: http://localhost:8080/camunda/app/welcome/default/#!/login

## Camunda Platform

# :point_right: Conclusion
