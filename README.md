# VTT-Example-IDS-Connector

This project contains components for the VTT Example IDS Connector, which includes a User Interface (UI), a Connector component and Postgres database

## Directory Structure

The project directory is structured as follows:

```
.
├── bamboo-specs
├── conf
├── devops
├── docker-compose.yml
├── Makefile
├── README.md
└── sonar-project.properties
```

- `bamboo-specs`: This directory contains sepecific parameters needed by the Bamboo tool
- `conf`: This directory contains the needed config.json file as well as p12 certification files
- `devops`: Contains dev, prod and qa values
- `docker-compose.yml`: Docker Compose configuration for orchestrating the services.
- `Makefile`: Includes configuration details on how to build the docker container.
- `README.md`: Description of the repository contents
- `sonar-project.properties`: Contains project details (name, version etc.)

All components included in the project are built using the same docker compose file. The file has references to docker images that are imported from remote repositories. 

The imported components are: 

- **User Interface (UI)**: The UI component is developed based on the [DataspaceConnectorUI](https://github.com/International-Data-Spaces-Association/DataspaceConnectorUI) project.

- **Connector**: The Connector component is based on the [DataspaceConnector](https://github.com/International-Data-Spaces-Association/DataspaceConnector) project.
  
- **Postgres**: The Postgres database component is based on the [Postgres](https://github.com/postgres/postgres) project.


## Usage

To set up and run the VTT Example IDS Connector, follow these steps:

### Running the connector 

1. From the root directory run `docker compose up --build -d` this will start the `VTT_connector` and `VTT_UI` in detached mode	

2. Once the services have started you can navigate to `http://localhost:8080` to access the user interface

   Please note that when deploying to a server, `http://localhost:8080' should be replaced with `http://server-ip:8080` to access the user interface


## License

This project is licensed under the terms of the [LICENSE](LICENSE) file included in the respective component directories. In addition, the Postgres lisence is described here [Postgres license](https://opensource.org/license/postgresql/) 

For detailed information about the licenses of individual components, refer to the specific component's repository.

