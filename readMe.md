This in an initial version of the instructions that describe how to install and deploy an example IDS connector instance. The connector can be connected to VTT's Data Space Innovation Lab and it can be used to test e.g. IDS based data exchange.

Before installation, the following prerequisites should be installed: 

(Windows or Linux environment):
- Git
- Docker 
- Postman
- Unzip (Linux environment)
- Python3

<h2> 1. Installation </h2>

<b>1.1 Clone the repository and unzip the package</b>

git clone  https://github.com/IlkkaNis/IDSTestbed_client_connector.git

Navigate to folder "IDSTestbed_client_connector"

Unzip the file 'VTT connector.zip' 

(NOTE: The official documentation of the dataspace connector can be found at https://international-data-spaces-association.github.io/DataspaceConnector/)

<b> 1.2. Configure the connector (Optional step)</b> <br>
You can change the connector's self description by editing the file /IDSTestbed_client_connector/VTT connector/DataspaceConnector-main/src/main/resources/conf/config.json.
A typical configuration task is, for example, to edit the ID, title or description of the connector. The ID of the connector can be found at:

```
  "ids:connectorDescription" : {
    "@type" : "ids:BaseConnector",
     "@id" : "https://w3id.org/idsa/autogen/baseConnector/3d6d9440-ebba-11ec-8ea0-0242ac120002"
```
You can also change the port where the connector is deployed on (by default the connector runs on port 8081): 
```
Step 1: In folder "IDSTestbed_client_connector/VTT connector/DataspaceConnector-main" open the "Dockerfile" file and edit the  EXPOSE section (e.g. EXPOSE 8080)
Step 2: In folder "DataspaceConnector/src/main/resources"  open the file "application.properties" and edit the section "server.port" section (e.g. server.port=8080)

```

<b>1.3 Build the connector</b>
Navigate to folder "IDSTestbed_client_connector/VTT connector/DataspaceConnector-main" and type (do not forget to include the dot in the end) 
```yaml

sudo docker build -t dsca . 
```
(NOTE: Depending on your deployment environment / configuration you may not need to include the "sudo" part)


<b>1.4 Run the connector</b>
```yaml
sudo docker run --publish 8081:8081 --name connectora dsca
```

<h2> 2. Receive data from VTT's Data Space Innovation Lab connector</h2>

VTT Data Space Innovation Lab provides an experimental data space that can be used for e.g., performing combatibility tests with different IDS modules. Next, we will test our connector instance using the innovation lab. The data flows between modules are shown in the picture below. 

![Testbed workflow](https://github.com/IlkkaNis/IDSTestbed_client_connector/blob/main/Images/testbedworkflow.png)

In the following, Postman tool is utilized for managing the connector.

<b>2.1 Download the data consumer request collection and import it to Postman</b>
- Navigate to the folder "Postman_collections" in Github repository and download the file "data_consumer_and_provider.zip".
- Unzip the file and import the json files into to your Postman application ("Import" button  + select file)
- You should see two new collections in your Postman: "Consume data resource" and "Provide data resource".

<b>2.2 Test data retrieval from Data Space Innovation Lab's connector </b> <br> <br>
In Postman most of the needed configuration tasks can be done by editing the collection variables (click the name of the collection and examine the "Variables" tab)

- Change the "connectorURL" variable to correspond the URL where your connector instance is deployed on. 

(NOTE: Remember to press "Save" button every time you edit the collection variables)

![Postman](https://github.com/IlkkaNis/IDSTestbed_client_connector/blob/main/Images/postman2.png)

- The "Broker query" request enables searching available connectors from the IDS Broker. By opening the "Body" tab of the request you can examine the pre-defined SPARQL query that retrieves necessary data from the broker. Press the "Send" button to execute the query.
- You should now see results in the response's body section, for example:

```yaml
    "@id": "https://localhost/connectors/-1475001399",
    
           "resourceCatalogURL": "https://broker.collab-cloud.eu:8081/api/catalogs/dac9f6f6-67dd-4594-aa5f-2f9937aaa57f",
    
           "dataProviderAccessURL": "https://broker.collab-cloud.eu:8081/api/ids/data",
    
    "description": "An example connector deployed as a part of VTT's IDS testbed",
    "title": "VTT IDS testbed example connector",
```
- From the response body, copy the value of the key "dataProviderAccessURL" and paste it to the collection variable table (field "dataProviderAccessURL"). See example image below
- Do the same for the value of the key "resourceCatalogURL" ("catalogURL" in the collection variable table). On the data provider side, the data catalogs contain the different data resources the provider offer See [here](https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v6/DataModel) for more information about the connector's data model.
- Save the collection variables

![Postman variables](https://github.com/IlkkaNis/IDSTestbed_client_connector/blob/main/Images/postman_variables.png)

- Next, open the "Description request with catalogue" and press the "Send" button. Again, you should see a json description in the response's "Body" section located in the lower part of the view. Examine the json and try to find the part where different data artifacts are described, for example:

```yaml
  "@type": "ids:Artifact",
  
  
  "@id": "https://broker.collab-cloud.eu:8081/api/artifacts/81cde26e-2290-479c-aba1-f002d1e3d84a",
  
  
  "ids:fileName": "MyTestArtifact",
  "ids:creationDate": {
    "@value": "2022-04-06T07:48:23.556Z",
    "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
  },
  "ids:byteSize": 5594,
  "ids:checkSum": "2673503218"
},
```
- Select the URL of the artifact you are interested in and copy it to the collection variable table ("artifactURL").
- In the "Contract request" the data consumer negotiates a contract agreement with the data provider in order to receive the requested data artifact. You can open the "Params" and "Body" sections to examine the details of the request. 
- As can be seen, in addition to the catalogURL other variables must be added to the request. These variables include "offer" and "rule" (in our example, Postman adds these variables automatically). To learn more about the contract negotiation phase, navigate [here](https://international-data-spaces-association.github.io/DataspaceConnector/CommunicationGuide/v6/Consumer) and [here](https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v6/UsageControl) for more detailed information. 
- Hit the "Send" button and examine the results. The most interesting part of the results is shown below:

```yaml
"artifacts": {
  "href": "https://130.188.160.90:8081/api/agreements/dfd5dab6-df25-4a56-b489-80e9396f206a/artifacts{?page,size}",
  "templated": true
 }
```
- Copy the new artifact URL excluding the "{?page,size}" and paste it either to the URL field of the "Get Artifact" call in Postman or into your wer browser (e.g. Mozilla Firefox).
- From the opened json description, find the "data" section and copy the URL ending with the term "/data", for example: 
```yaml
data:	
  href:	"https://130.188.160.90:8081/api/artifacts/8c835266-fd31-43a4-b81a-66026fb5552f/data"
```
- In Postman, open the "Get artifact" request and paste the copied data URL into the URL field (next to the "GET" button).
- You should see the data received from the data provider connector

The hands-on tutorial part ends here. The following steps are for more advanced use of the connector. 

<b>2.3 Publish / subscribe </b> <br><br> 
The connector enables subscribing for notifications when a selected data artifact is updated on provider's side. In this example, this can be done using the "Subscribe for updates" request. Before the subscription can be done, a contract agreement that points to the data resource / artifact must exist between the provider and the consumer. 
- Examine the pre-defined body section of the "Subscribe for updates" request. The "target" parameter represents the artifact we want to listen (it can also be a data resource). In addition, the "location" is the endpoint where the notifications should be sent and the "subscriber" is the URL of the data consumer connector.   
- In this example, a pre-defined http server implementation is provided to receive notifications on data resource updates. It is a simple Python script that can be found at **IDSTestbed_client_connector/DataspaceConnector/pythonScripts**. Start the script with the command "python3 notificationReceiver.py"
(NOTE: Please examine the console output to identify if you need to install any Python libraries before you can run the script).
- When the specified artifact is updated on the provider side, the Python script should print the details of the update event. In addition, as you selected "pushData: true" in the subscription request, you should be able to directly access the updated data resource.
- Navigate again to the "Get artifact" request and specify the same data URL as you did in the contract request phase (e.g. "https://130.188.160.90:8081/api/artifacts/8c835266-fd31-43a4-b81a-66026fb5552f/data"). You should be able to examine the updated data.

<h2> 3. Define your own data resource </h2>

In this section it is explained, how different types of data resources can be registered to the connector. As a result, the connector can act as a data provider and offer the defined resources to be consumed by other connectors participating in the same data space. 

Again, the registering process is performed using a pre-defined Postman collection. For different operations, the collection includes some pre-defined example parameter values that can be found in the "body" sections. However, these values can be edited as needed.

The data resource registering process follows the connector's data model. More detailed information about the process can be found from [here](https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v6/Messages) and [here](https://international-data-spaces-association.github.io/DataspaceConnector/CommunicationGuide/v6/Provider). 
In addition, the data model is described in [here](https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v6/DataModel)


To be continued... 

