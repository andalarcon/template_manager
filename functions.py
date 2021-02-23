import json

def read_json_parameters(json_path):
    try:
        with open(json_path) as jasonFile:
            params = json.load(jasonFile)
        jasonFile.close()
        return params
    except FileNotFoundError as error:
        print(error)
        jasonFile.close()
        return None

def write_json(json_data, json_path):
    try:
        with open(json_path, 'w') as jasonFile:
            json.dump(json.loads(json_data), jasonFile, indent=4)
        jasonFile.close()
    except:
        print("An error has occurred trying to write the json file")
        jasonFile.close()