import json

data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    }
}

def recursivesearConfig(jsonData, strkey:str):
    if isinstance(jsonData, dict):
        for key, value in jsonData.items():
            if(strkey == key):
                return value
            else:
                ret = recursivesearConfig(value, strkey)
                if ret is not None:
                    return ret
    return None

if __name__ == "__main__":
    print(recursivesearConfig(data, "e"))