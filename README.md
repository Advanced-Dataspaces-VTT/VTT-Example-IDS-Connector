# VTT-Example-IDS-Connector

1. Start by pulling this branch and then create a new branch for your deployment
2. Open the github [actions](.github/workflows/docker-build.yml) and change the following to your branch name and desired tag:
   
   ```vtt-connector:latest``` 
   
   ```vtt-connector-ui:latest```
   Also include your branch name under ```branches```
3. Insert your ```certificate```, ```truststore``` file into the [conf](./conf/) directory
4. Update the [config.json](./conf/config.json) file so that the ```ids:keyStore:@id``` and ```ids:trustStore:@id``` match the new uploaded files
5. Update the [docker-compose.yml](docker-compose.yml) so that ```SERVER_SSL_KEY-STORE``` matches the uploaded certificate file
6. Commit and push the changes to your new branch and then wait for the [build](https://github.com/Advanced-Dataspaces-VTT/VTT-Example-IDS-Connector/actions) to pass


