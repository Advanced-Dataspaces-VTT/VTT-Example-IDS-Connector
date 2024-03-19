# VTT-Example-IDS-Connector

1. Start by pulling this branch and then create a new branch for your deployment
2. Open the github [actions](.github/workflows/docker-build.yml) and change the following so that the tag reflects the current branch:
   
   ```vtt-connector:latest``` 
   
   ```vtt-connector-ui:latest```
   Also include your branch name under ```branches```
3. Insert your ```certificate```, ```truststore``` file into the [conf](./conf/) directory
4. Update the [config.json](./conf/config.json) file so that the ```ids:keyStore:@id``` and ```ids:trustStore:@id``` match the new uploaded files
5. Update the [docker-compose.yml](docker-compose.yml) so that ```SERVER_SSL_KEY-STORE``` matches the uploaded certificate file, also ensure the image for the connector and UI are correctly deffined ```image```
6. Commit and push the changes to your new branch and then wait for the [build](https://github.com/Advanced-Dataspaces-VTT/VTT-Example-IDS-Connector/actions) to pass


