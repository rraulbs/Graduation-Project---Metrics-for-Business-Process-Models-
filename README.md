# Graduation-Project---Metrics-for-Business-Process-Models-

<h4 align="center"> 
	🚧  Project 🚀 Under construction...  🚧
</h4>

# :point_right: Getting Started
This page will bring you up to speed with the needed configurations and softwares to start working on the project.

# :point_right: Setup

:heavy_check_mark: Make sure you have an editor to work with code like VSCode or another one of your choice. <br>
https://code.visualstudio.com/

:heavy_check_mark: Make sure you have git installed <br>
https://git-scm.com/downloads

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


:heavy_check_mark: Clone this project to a local folder <br>
Open the command prompt, choose a path to the project and run the command. <br>
```
git clone https://github.com/rraulbs/Graduation-Project---Metrics-for-Business-Process-Models-.git
```
![image](https://user-images.githubusercontent.com/16651018/172268602-33d68955-5d45-4b2c-a5f6-701af1f98964.png)

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

## Camunda Modeler
### Load a new process

1. **Model the process through Camunda Modeler** <br>
1. **Save the xml file** <br>
   - Id: ```<ProcessName>_<Version> ``` <br>
***p.s.*** The Id must have this format above, to map the process_id in later steps. <br>
***p.s.*** The file name, must have this same id format <br>
***p.s.*** Save the xml file in the following path: <br>
***``` C:\...\Graduation-Project---Metrics-for-Business-Process-Models-\BusinessProcessDashboard\static-metrics-data\processes\ ```***
![image](https://user-images.githubusercontent.com/16651018/172481331-c91de7cd-5fa5-4983-a8fd-376d74f8ef6d.png)

3. **Update Kibana** <br>
To send the project's static metrics to Kibana, perform the following step
   - Update the key "UpdateOnce" to the value "true" and save. <br>
   - The conf.json file is available in the path: <br>
   ***``` C:\...\Graduation-Project---Metrics-for-Business-Process-Models-\BusinessProcessDashboard\static-metrics-data\env\ ```*** <br>
![image](https://user-images.githubusercontent.com/16651018/172491799-bcb90d17-bbc5-432e-a299-fe3835990eea.png)
   - This configuration will update the process index in kibana with the information of this new process.

### Check static metrics in Kibana
Now you can check the static metrics of the process that was saved. To do so, access Kibana's DevTools option, or through the link: <br>
http://localhost:5601/app/dev_tools#/console
![image](https://user-images.githubusercontent.com/16651018/172486507-b69c8383-fc05-4c15-8359-d3d7f9498746.png)
As shown in the image, see the metrics through the GET request below: <br>
```GET processes/_doc/ReviewInvoice_2``` <br>
The static metrics available for verification include all types of elements present in the camunda modeler. Then you can check how many elements of each type your process contains. <br>

Example:
```
{"FileName":"ReviewInvoice_2.bpmn","BPMN_Modeler":"Camunda","nTask":0,"nTaskMultipleIstance":0,"nTaskLoopActivity":0,"nSendTask":0,"nReceiveTask":0,"nUserTask":2,"nManualTask":0,"nBusinessRuleTask":0,"nServiceTask":0,"nScriptTask":0,"nCollapsedSubProcess":0,"nExpandedSubProcess":0,"nAdHocSubProcess":0,"nTransaction":0,"nCallActivity":0,"nExclusiveGateway":0,"nParallelGateway":0,"nInclusiveGateway":0,"nEventBasedGateway":0,"nComplexGateway":0,"nStartNoneEvent":1,"nStartMultipleParallelEventDefinition":0,"nStartMultipleEventDefinition":0,"nStartSignalEventDefinition":0,"nStartConditionalEventDefinition":0,"nStartTimerEventDefinition":0,"nStartMessageEventDefinition":0,"nStartCompensateEventDefinition":0,"nStartCancelEventDefinition":0,"nStartEscalationEventDefinition":0,"nStartErrorEventDefinition":0,"nIntermediateCatchMultipleEventDefinition":0,"nIntermediateCatchMultipleParallelEventDefinition":0,"nIntermediateCatchMessageEventDefinition":0,"nIntermediateCatchTimerEventDefinition":0,"nIntermediateCatchConditionalEventDefinition":0,"nIntermediateCatchLinkEventDefinition":0,"nIntermediateCatchSignalEventDefinition":0,"nIntermediateThrowNoneEvent":0,"nIntermediateThrowMessageEventDefinition":0,"nIntermediateThrowEscalationEventDefinition":0,"nIntermediateThrowLinkEventDefinition":0,"nIntermediateThrowSignalEventDefinition":0,"nIntermediateThrowCompensateEventDefinition":0,"nIntermediateThrowMultipleEventDefinition":0,"nBoundaryMessageEvent":0,"nBoundaryTimerEvent":0,"nBoundaryCancelEvent":0,"nBoundaryConditionalEvent":0,"nBoundaryEscalationEvent":0,"nBoundaryErrorEvent":0,"nBoundarySignalEvent":0,"nBoundaryCompensateEvent":0,"nBoundaryTimerEventNonInt":0,"nBoundaryEscalationEventNonInt":0,"nBoundaryConditionalEventNonInt":0,"nBoundaryMessageEventNonInt":0,"nEndEventNone":1,"nEndTerminateEventDefinition":0,"nEndEscalationEventDefinition":0,"nEndMessageEventDefinition":0,"nEndErrorEventDefinition":0,"nEndCompensateEventDefinition":0,"nEndCancelEventDefinition":0,"nEndSignalEventDefinition":0,"nEndMultipleEventDefinition":0,"nSequenceFlow":3,"nDefaultFlow":0,"nConditionalFlow":0,"nMessageFlow":0,"nAssociation":0,"nPool":0,"nLane":0,"nDataObject":0,"nDataStore":0,"nGroup":0,"nTextAnnotation":0,"nMessage":0,"nChoreographyTask":0,"nChoreographyParticipant":0,"nChoreographySubprocess":0,"nConversation":0,"nSubConversation":0,"nCallConversation":0,"nConversationLink":0,"TotalElements":7}
```
The static metrics of our example process were successfully captured:
![image](https://user-images.githubusercontent.com/16651018/172490901-b5c9d5b5-6c20-4852-94e8-e347015ca29f.png)

### Deploy process to Camunda Platform
This step is necessary so that we can also capture dynamic metrics.
1. Deploy current diagram
1. Deploy
![image](https://user-images.githubusercontent.com/16651018/172494086-07239622-31d1-4d8e-ad10-e26aebc4def4.png)
If there is nothing wrong with your process modeling, a success message will appear, and your process will be ready to be managed on the camunda platform. <br>
![image](https://user-images.githubusercontent.com/16651018/172494207-2cf88e55-9c14-4416-bd99-c22a9e2c2cf9.png)


## Camunda Platform
If any instance of your process has already finished running, dynamic metrics will be available in kibana. <br>
![image](https://user-images.githubusercontent.com/16651018/172494756-2254f369-edba-4b94-8512-e5558317e526.png) <br>
For example, the image below shows the result after running two instances of the ReviewInvoice_1 process. <br>
![image](https://user-images.githubusercontent.com/16651018/172494936-aa6242c2-f8a0-455d-8034-a51a81b88f26.png) <br>

The dynamic metrics are:
- The minimum/average/maximum time to perform a task.
- The minimum/average/maximum execution time of a process.

As in the case of static metrics, dynamic measures also have a 'conf.json' file, but the difference is that in this case, the update is continuous, every 30s the 'dynamicmetrics' container uses the Camunda Platform API to capture these measures and update the index of the processes in kibana. <br>

If you want to configure this: <br>
   - You can update the key "keepUpdating" to the value "false" and save. <br>
   - The conf.json file is available in the path: <br>
   ***``` C:\...\Graduation-Project---Metrics-for-Business-Process-Models-\BusinessProcessDashboard\dynamic-metrics-data\env\ ```*** <br>
![image](https://user-images.githubusercontent.com/16651018/172496300-411a063c-8e6b-4e9c-9ac4-37b5f996b7d6.png)
   - This configuration will stop the continuos update of dynamic metrics to kibana.

## Dashboard

# :point_right: Conclusion
