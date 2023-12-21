# PyBank API

### Getting Started

_Make sure you have docker installed._

Create the **.env** file on project root and include the variables in **.env.example**.

**ALL IS MANDATORY**.

Example:

```bash
SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:password@host:port/db
SQLALCHEMY_TRACK_MODIFICATIONS=False
JWT_SECRET_KEY=my_secret
JWT_ACCESS_TOKEN_EXPIRES=8 #int

#DOCKER

MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=my_db
MYSQL_USER=user
MYSQL_PASSWORD=password
```

### Running the app in developer mode

Execute the command to up containers:

```bash
$ docker-compose -f docker-compose.yml up -d
```

### Running the app in production mode

You must have a MySQL instance created and included in the .env file.

Execute the command to up containers:

```bash
$ docker-compose -f docker-compose.prod.yml up -d
```

### 🚀 It's ready!


