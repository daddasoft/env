import os


def int__config(pathOfEnv=f"{os.getcwd()}/.env"):
    """
    by default the path to env is os.getcwd()}/.env 
    mean that is on your current work space if you
    want to change it pass it as argument when you 
    init the Config 👆👆 
    """
    def getEnv(key):
        try:
            f = open(pathOfEnv, "r")
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
    return getEnv
