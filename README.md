# VTT-Example-IDS-Connector

This project contains components for the VTT Example IDS Connector, which includes a User Interface (UI) and a Connector component.

## Directory Structure

The project directory is structured as follows:

```
.
├── README.md
├── VTT_connector
├── VTT_postman
├── VTT_ui
├── assets
├── config.json
└── docker-compose.yml
```

- `VTT_connector`: This directory contains the Connector component files.
- `VTT_ui`: This directory contains the User Interface (UI) files.
- `VTT_postman`: Contains a Postman collection for data consumer and provider.
- `assets`: Contains various assets used in the project.
- `docker-compose.yml`: Docker Compose configuration for orchestrating the services.

## Project Components

- **User Interface (UI)**: The UI component can be found in the `VTT_ui` directory. It is developed based on the [DataspaceConnectorUI](https://github.com/International-Data-Spaces-Association/DataspaceConnectorUI) project.

- **Connector**: The Connector component can be found in the `VTT_connector` directory. It is based on the [DataspaceConnector](https://github.com/International-Data-Spaces-Association/DataspaceConnector) project.

## Usage

To set up and run the VTT Example IDS Connector, follow these steps:

### Running locally 

1. From the root directory run `docker compose up --build -d` this will start the `VTT_connector` and `VTT_UI`

2. Once the services have started you can navigate to `http://localhost:8083`

### Deploying to a server

1. Navigate to the [docker-compose.yml](docker-compose.yml)

2. Locate the `ui` service and ensure that `CONNECTOR_URL` is set to the URL / IP of the server where the connector is deployed on.

3. From the root directory run `docker compose up --build -d` this will start the `VTT_connector` and `VTT_UI`

4. Once the services have started you can navigate to `http://server-ip:8083` where you will find the connectors user interface

## Further information
* [User interface](./VTT_ui/README.md)
* [Postman collections](./VTT_postman/README.md)

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file included in the respective component directories.

For detailed information about the licenses of individual components, refer to the specific component's repository.

