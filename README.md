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
