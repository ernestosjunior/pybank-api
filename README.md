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

### If you are on a computer other than the Mac M1, you must remove the attr platform from the docker-compose.yml file
<img width="1044" alt="Screenshot 2023-12-21 at 14 18 22" src="https://github.com/ernestosjunior/pybank-api/assets/54125328/a996047a-36fd-4d1d-af17-d01516087ce3">

### First Person:

email: pessoainicial@pybank.com
password: mudar123

### Running the app in production mode

You must have a MySQL instance created and included in the .env file.

Execute the command to up containers:

```bash
$ docker-compose -f docker-compose.prod.yml up -d
```

### 🚀 It's ready!


