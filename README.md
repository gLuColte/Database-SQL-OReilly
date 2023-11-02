![Main Banner](./markdown-images/main-banner.png)

# Database-SQL-OReilly
Welcome to the SQL Mastery Repository! This repository is your gateway to mastering the art and science of Structured Query Language (SQL). As you journey through the realms of relational databases, you'll encounter hands-on exercises, code snippets, and challenges that will solidify your grasp on SQL and its intricacies, ensuring you gain a practical and deep understanding of database querying and structure.

## Why Learn SQL?
In the vast world of data, understanding SQL is paramount for several reasons:

1. **Ubiquity**: SQL is the lingua franca of data. Most relational database management systems (RDBMS) use SQL, making it an indispensable skill for data professionals.
2. **Data Retrieval & Manipulation**: SQL provides powerful means to retrieve, filter, and manipulate data, allowing for complex operations with simple, readable syntax.
3. **Optimization**: With SQL, you can optimize data retrieval operations, ensuring efficient and speedy access even with vast amounts of data.
4. **Security**: SQL offers granular control over data access, ensuring data security and integrity.
5. **Integration** : SQL databases easily integrate with various tools, platforms, and applications, making data accessibility and utilization streamlined.

### SQL vs. Other Database Forms
While NoSQL databases like MongoDB, Cassandra, or Redis have their strengths and specific use cases, SQL databases stand out for:
- **Structured Data**: SQL databases provide a clear structure, ensuring data consistency and integrity.
- **ACID Properties**: SQL databases adhere to Atomicity, Consistency, Isolation, and Durability (ACID) properties, guaranteeing reliable transactions.
- **Flexibility in Queries**: SQL offers unmatched flexibility in querying, allowing for complex joins, sub-queries, and aggregations.
- **Maturity**: Being around for decades, SQL databases have matured, offering robustness and a vast ecosystem of tools and community support.

## Dive Deep into SQL!
As you embark on this enlightening journey, remember that learning SQL is not just about writing queries. It's about comprehending the philosophy of structured data, the art of relational design, and the essence of data relationships. Happy Querying!

## Setup

### Docker

Following [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/) to install Docker Engine.

Please ensure to enable Non-Root User Access for Docker - [How to Fix Docker Permission Denied?](https://phoenixnap.com/kb/docker-permission-denied):
```termnial
sudo groupadd -f docker
sudo usermod -aG docker $USER
newgrp docker
```

### Docker Compose

Following [Install the Compose plugin](https://docs.docker.com/compose/install/linux/) to install Docker-Compose Plugin.
```terminal
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

### SQL Related Installation

An ODBC driver uses the Open Database Connectivity (ODBC) interface by Microsoft that allows applications to access data in database management systems (DBMS) using SQL as a standard for accessing the data. ODBC permits maximum interoperability, which means a single application can access different DBMS.

Following tutorial from Microsoft - [Install the Microsoft ODBC driver for SQL Server (Linux)](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline)

A shell script is provided and need to be executed:

```terminal
chmod +x microsoft_odbc_18_installation.sh
./microsoft_odbc_18_installation.sh
```

### Conda Environment

Create a virutal python environment and install requirements.txt

```terminal
conda env create -f environment.yml
```

**To save a conda environment**:
```terminal
conda env export | grep -v "^prefix: " > environment.yml
```

### Python Environment

If you are installing through pip

```terminal
pip install -r requirements.txt
```

**To save a python environment**:
```terminal
pip freeze > requirements.txt
```

### Initialization & Verification

```terminal
sudo docker-compose -f docker-compose.yml up -d
docker container ls
```
Outputs the following:
```terminal
CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS                 PORTS                                                                    NAMES
4d8115aeea93   mcr.microsoft.com/mssql/server   "/opt/mssql/bin/perm…"   37 seconds ago   Up 7 seconds           0.0.0.0:1433->1433/tcp, :::1433->1433/tcp                                database-sql-oreilly_sql_1
```


### How to Use This Repository:

Place Holder
- Jupyter NoteBook for Chapters