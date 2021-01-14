import os

# if you want to configirate the path of .env file


def config(path=f"{os.getcwd()}/.env"):
    """
    it's Take the path of .env file as parameter
    by default is the root of your project (current work directory)
    if you change the place of the file pass the path ass parameter to
    the config function
    """
    def env(key):
        try:
            f = open(path, "r")
            allLines = f.read().split("\n")
            for item in allLines:
                selected = item.split("=")
                if(selected[0].strip() == key):
                    if(len(selected) > 1):
                        return str(selected[1]).strip()
                    return None
        except:
            return None
    return env

# if you keep .env in the root


def env(key):
    """
    give the key of the environment variable and 
    it's return the value 
    if not found it return None
    """
    try:
        f = open(f"{os.getcwd()}/.env", "r")
        allLines = f.read().split("\n")
        for item in allLines:
            selected = item.split("=")
            if(selected[0].strip() == key):
                if(len(selected) > 1):
                    return str(selected[1]).strip()
                return None
    except:
        return None
