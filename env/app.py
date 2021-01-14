import os


def env(key):
    try:
        f = open(f"{os.getcwd()}/.env", "r")
        allLines = f.read().split("\n")
        for item in allLines:
            selected = item.split("=")
            # print(selected)
            if(selected[0].strip() == key):
                if(len(selected) > 1):
                    return str(selected[1]).strip()
                return None
    except:
        return None
    return env
