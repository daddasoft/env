## Make Environment variables for your app/program

## install

```shell
pip install appdotenv
```

### setup

```python
from env import env


```

by default it look for the file in the current work directory the folder of your project

```python
print(env("PORT")) #5000
print(env("JWT_SECRET")) #fgdrgedrger
```

after that you can access the env Variables from your .env file like This :

```python
env("APP_SECRET") # fsgdghfghfghfghfhfhfh
```

# Configuration

if you want the config the .env file path use

```python
from env import config

env = config("path_to_.env_file")
```

now after the configuration use env function the get the value of a key

```python
from env import config

env = config("path_to_.env_file")

print(env("PORT")) #5000
```

### Some Uses Examples

```python
from env import env

if(env("APP_ENV") == "dev"):
    enableDebugMode()

```

```python
from env import env

mysql.connect( env("host"),env("user") , env("password") )
```

```python
from env import env

registerRouter = env("register") == "yes" #it's return true or false

```
