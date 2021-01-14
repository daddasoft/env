## Make Environment variables for your app/program

### setup

```python
from env import init__config
```

by default it look for the file in the current work directory the folder of your project

### if you have your .env in another place call

```python
env = init__config("path_to_.env_file")
```

after that you can access the env Variables from your .env file like This :

```python
env("APP_SECRET") # fsgdghfghfghfghfhfhfh
```
