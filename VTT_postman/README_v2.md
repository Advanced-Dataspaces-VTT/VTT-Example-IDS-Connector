<h1> Interacting With The Connector Through Postman </h1>

This section offers guidance for advanced users on effectively managing and configuring the connector via its REST API. The REST API is accessed using the Postman tool.

In the provided example, the user initiates the process by querying the IDS metadata broker to obtain information regarding available connectors. Leveraging this information, the user then proceeds to request more in-depth descriptions of the available data resources. 
Finally, the user creates a contract agreement and gains access to the chosen dataset.

<h2> 2. Receive data from VTT's Data Space Innovation Lab connector</h2>

VTT Data Space Innovation Lab provides an experimental data space that can be used for e.g., performing combatibility tests with different IDS modules. Next, we will test our connector instance using the innovation lab. The data flows between modules are shown in the picture below. 

![Testbed workflow](https://github.com/IlkkaNis/VTT-OSME-tutorial/blob/main/Images/testbedworkflow.png?raw=true)

The configuration interface provided by the connector can be accessed with different methods. One example is the Swagger GUI that can be found at https://your_connector_URL/api/docs. 

However, in the following, the Postman tool is utilized for managing the connector.

<b>2.1 Import the Postman collections</b>
- Navigate to the folder "Postman_collections" and import the json files into to your Postman application ("Import" button  + select file)
- From the shown collections, select the "Consume data resource"

<b>2.2 Test data retrieval from Data Space Innovation Lab's connector </b> <br> <br>
In Postman most of the needed configuration tasks can be done by editing the collection variables (click the name of the collection and examine the "Variables" tab)

- Change the "connectorURL" variable to correspond the URL where your connector instance is deployed on. 

(NOTE: Remember to press "Save" button every time you edit the collection variables)

- The "Broker query" request enables searching available connectors from the IDS Broker. By opening the "Body" tab of the request you can examine the pre-defined SPARQL query that retrieves necessary data from the broker. Press the "Send" button to execute the query.
- You should now see results in the response's body section, for example:

```yaml
    "@id": "https://localhost/connectors/-1475001399",
    "resourceCatalogURL": "https://130.188.160.90:8081/api/catalogs/dac9f6f6-67dd-4594-aa5f-2f9937aaa57f",
    "dataProviderAccessURL": "https://130.188.160.90:8081/api/ids/data",
    "description": "An example connector deployed as a part of VTT's IDS testbed",
    "title": "VTT IDS testbed example connector",
```
- From the response body, copy the value of the key "dataProviderAccessURL" and paste it to the collection variable table (field "dataProviderAccessURL"). See example image below
- Do the same for the value of the key "resourceCatalogURL" ("catalogURL" in the collection variable table). On the data provider side, the data catalogs contain the different data resources the provider offer See [here](https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v6/DataModel) for more information about the connector's data model.
- Save the collection variables

![Postman variables](https://github.com/IlkkaNis/VTT-OSME-tutorial/blob/main/Images/postman_variables.png?raw=true)

- Next, open the "Description request with catalogue" and press the "Send" button. Again, you should see a json description in the response's "Body" section located in the lower part of the view. Examine the json and try to find the part where different data artifacts are described, for example:

```yaml
  "@type": "ids:Artifact",
  "@id": "https://130.188.160.90:8081/api/artifacts/81cde26e-2290-479c-aba1-f002d1e3d84a",
  "ids:fileName": "MyTestArtifact",
  "ids:creationDate": {
    "@value": "2023-04-06T07:48:23.556Z",
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
  "href": "https://1ocalhost:8081/api/agreements/dfd5dab6-df25-4a56-b489-80e9396f206a/artifacts{?page,size}",
  "templated": true
 }
```
- Copy this URL excluding the "{?page,size}", and in Postman, open the "Get artifact" request and paste the copied URL into the URL field (next to the "GET" button).
- From the opened json description, find the "data" part and copy the URL ending with the term "/data", for example: 
```yaml
data:	
  href:	"https://localhost:8081/api/artifacts/8c835266-fd31-43a4-b81a-66026fb5552f/data"
```
- Paste the URL to the "Get artifact" URL field (as in the previous step)
- You should see the data received from the data provider connector
