# Interacting With The Connector Through Postman

## Importing The Collections
* Open the Postman Desktop GUI
* Import the following collections
    * [Provide collection](./Provide%20data%20resource.postman_collection.json)
    * [Consume collection](./Consume%20data%20resource.postman_collection.json)
    * [Environment varaiable collections](./Environment%20variables.postman_environment.json)
* For the request we make use of Basic Authentication which works by authenticating a user by username and password (admin:password)
* Ensure that the Environment variable collection is also selected

Checklist for this step, there should be two request collections (provide, and consume), there should also be one environment variable collection.

## Running the Provide Collection

This collection differes from the Keycloak configuration as it works with Basic Authentication and we do not need to manage any tokens.

Using Postman "Run collection" tool to automate the provide collection requests:
* Navigate to the Provide collection root
* Locate the three dots on the right of the collection name
* Select "Run collection" from the drop down
* In the new tab ensure all the POST requests have the checkbox as checked
* In the new tab ensure all the GET requests have thec checkbox as note checked
* Locate "Advances settings"
* Under "Advances settings" ensure the checkbox for "save responses" is checked
* The tab should look as follows ![The tab should look as follows](../assets/correct-postman-run-collection-configuration-spring.png)
* You can then click "Run Provide data resource ..."

By clicking this button you will execute all the requests and we have tests made that will collect and set the required variables under the collection variables.

(Note: please ensure that all requests have either a 200 or 201 status)

## Running the Consume Collection
To run the consume collection requests you will need to have the specific values available for the following variables (catalogURL), they can be taken from the reponse body of the "Run collection" results, note that the values to be extracted are found under "response.body._links.self.href" for each request (catalogURL: Create catalog)

```
"_links": {
    "self": {
        "href": "https://localhost:8081/api/representations/c26f43cd-8984-4797-be15-1eced5b5c231"
    }
}
```

The consume collection is made up of three requests:
* Description request with catalogue
* Contract request
* Get artifact

These requests will be called in the order presented. To run the first request (Description request with catalogue), you will need to set the catalogURL after setting this value in the consume environment variables should look as follows. ![Correct consume data request variables](../assets/correct-consume-description-request.png)

The description request can then be executed by clicking the "SEND" button and if successful you should see content in the response body and also a status message of 200.

Next the following values must be set (offerURL: Create offer (resource), ruleURL: Create rule). These can be fetched from the "Run collection" response bodies of the apporpriate requests. Once these values have been set the "Contract request" can be made.

When a successful "Contract request" is made you can then extract the artficat id url and place it in the "Get artifact" request.
