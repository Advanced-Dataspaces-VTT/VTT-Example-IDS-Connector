# VTT-Example-IDS-Connector

1. Start by pulling this branch and then create a new branch for your deployment
2. Open the github [actions](.github/workflows/docker-build.yml) and change the following so that the tag reflects the current branch:
   
   ```vtt-connector:latest``` 
   
   ```vtt-connector-ui:latest```
   Also include your branch name under ```branches```
3. Insert your ```certificate```, ```truststore``` file into the [conf](./conf/) directory
4. Update the [config.json](./conf/config.json) file so that the ```ids:keyStore:@id``` and ```ids:trustStore:@id``` match the new uploaded files
5. Update the [docker-compose.yml](docker-compose.yml) so that ```SERVER_SSL_KEY-STORE``` matches the uploaded certificate file, also ensure the image for the connector and UI are correctly deffined ```image```
6. Commit and push the changes to your new branch and then wait for the  to pass
7. After a successful build you will find your [image](https://github.com/Advanced-Dataspaces-VTT/VTT-Example-IDS-Connector/pkgs/container/vtt-example-ids-connector%2Fvtt-connector) here
8. Then all you need to distribute will be the content of the [docker-compose.yml](docker-compose.yml) file
9. To run the application execute the following commands
```docker login ghcr.io -u USERNAME -p TOKEN```
```docker compose pull```
```docker compose up```

(Note: If you use sudo to login you must then use sudo for every other command)




