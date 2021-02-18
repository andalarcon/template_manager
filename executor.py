import json
from snowflake_connect import SFdbconn

if __name__ == "__main__":

    with open("templ_parameters.json") as jasonFile:
        params = json.load(jasonFile)

    sf_parameters = params["sf_parameters"]

    jasonFile.close()

    sf_db = SFdbconn(sf_parameters["user"],
                     sf_parameters["password"],
                     sf_parameters["account"],
                     sf_parameters["warehouse"],
                     sf_parameters["database"],
                     sf_parameters["url"])
    
    print(sf_db.fetch_one("SELECT json FROM AALARCON.TEST")[0])