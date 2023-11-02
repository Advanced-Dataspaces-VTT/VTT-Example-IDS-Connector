# Quick start

Note: root directory `hack/`

Start the application: `docker compose up --build` alternatively running it in the background `docker compose up --build -d` you can then ensure the correct containers are running and on which ports with `docker ps`

Successfully running the [docker-compose.yml](./docker-compose.yml) file will result in the following containers running:

| CONTAINER ID   | IMAGE                                                                     | COMMAND                  | CREATED         | STATUS         | PORTS                                                            | NAMES                |
|-----------------|---------------------------------------------------------------------------|--------------------------|-----------------|-----------------|------------------------------------------------------------------|----------------------|
| 94ca65d41d28   | ryankford/vtt-example-connector-ui:latest-amd64                           | "docker-entrypoint.s…"   | 5 minutes ago   | Up 5 minutes   | 0.0.0.0:8083->8083/tcp, :::8083->8083/tcp                        | vtt-connector-ui    |
| a271a6f58904   | ghcr.io/international-data-spaces-association/dataspace-connector:8.0.2   | "java org.springfram…"   | 5 minutes ago   | Up 5 minutes   | 8080/tcp, 29292/tcp, 0.0.0.0:8081->8081/tcp, :::8081->8081/tcp   | connectorb          |
| 39125654d4f4   | postgres:13                                                               | "docker-entrypoint.s…"   | 5 minutes ago   | Up 5 minutes   | 0.0.0.0:5433->5432/tcp, :::5433->5432/tcp                        | postgresb-container |


After 10 minutes you can then navigate to the following URLs:
* User interface: http://localhost:8083/
* Connector endpoints: https://localhost:8081/
* Connector swagger endpoint: https://localhost:8081/api/docs
    * Username: admin
    * Password: password

Suggested browser: `Chrome`

Troubleshooting:
* First run: `docker compose down -v`
* Then run: `docker compose up --build`