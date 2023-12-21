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

   Please note that when deploying to a server, `http://localhost:8080` should be replaced with `http://server-ip:8080` to access the user interface


## License

This project is licensed under the terms of the [LICENSE](LICENSE) file included in the respective component directories. In addition, the Postgres lisence is described here [Postgres license](https://opensource.org/license/postgresql/) 

For detailed information about the licenses of individual components, refer to the specific component's repository.

# Interacting With The Connector Through web user interface

# Overview

In your browser proceed to `http://server-ip:8080/` and you will be reidrected to `http://server-ip:8080/dashboard` and should see the following:

![dashboard](/assets/ui-dashboard.png)

This provides an overview of your connector.


## Creating a data offering

A data offering is an asset that you register with your connector and can provide to other connectors that agree to use the offering under the conditions you specifiy.

![offering](/assets/data-offering-1.png)

This view will show you current offering that are registered to the connector and will allow you to add new offerings by clicking "ADD OFFERING". 

Clicking "ADD OFFERING" will take you to the following page:

![offering](/assets/data-offering-2.png)

![offering](/assets/data-offering-3.png)

When all the fields are completed move on to the next tab. The Policy tab sets the criteria the consumer will have to agree to in order to use the offering.

![offering](../assets/data-offering-4.png)

You can make a policy template or create a new one for each offtering.

Next we will proceed to the representations tab which allows you to upload a file (.json, .csv) or upload and external data source (REST API, database connection, remote document).

![offering](/assets/data-offering-5.png)

The catalogue tab allows you to create a catalogue (grouping) of similar offerings.

![offering](/assets/data-offering-6.png)

Finally you can then register your offering, policy and catalog to a broker that has previously been configured to the connector.

![offering](/assets/data-offering-7.png)

By clicking save you are making the offering available.

## Consuming a data offering

To consume a data offering you will need to have the connector URL `https://server-ip:8081/api/ids/data`. Once you have the connector URL proceed to the Data consumption tab Requests and from here you can see all offering which you have already agreeded to consume

![offering](/assets/data-consumption-1.png)

Start by clicking on Request resource and in the new tab provide the connector URL that you want to consume data from 

![offering](/assets/data-consumption-2.png)

Show available resources will then fetch all resources from the connector where you can then view them in more detail by selecting the show representations or show meta data icons at the end of each row.

Selecting show representations will provide a URL which when clicked will show an artifact and at the end of the artifact row will allow you to agree or disagree with the contract (policy) for the offering. After agreeing you will be provided with a download URL which can be used to download the offering. 



