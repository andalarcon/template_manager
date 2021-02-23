import json
from snowflake_connect import SFdbconn
from template_management import Template_manager
from functions import read_json_parameters, write_json
import os
import subprocess
import sys

if __name__ == "__main__":

    params = read_json_parameters("templ_parameters.json")

    sf_parameters = params["sf_parameters"]

    git_parameters = params["git_parameters"]

    sf_db = SFdbconn(sf_parameters["user"],
                     sf_parameters["password"],
                     sf_parameters["account"],
                     sf_parameters["warehouse"],
                     sf_parameters["database"],
                     sf_parameters["url"])
    data = sf_db.fetch_one("SELECT json FROM AALARCON.TEST")[0]
    print("Copied Json")

    template = Template_manager(git_parameters["user"], git_parameters["token_pass"])

    template.git_clone(git_parameters["remote_repo"], git_parameters["local_repo_dest"])
    template_repo = template.git_select_local_repo(git_parameters["local_repo_dest"])
    template.git_checkout(template_repo, git_parameters["commit_hash"])
    template_path = os.path.join(git_parameters["local_repo_dest"], "local_broadcasting")

    print(template_path)
    
    template.create_json_parameters(data, template_path, "parameters_local_broadcasting.json")

    # executor_file = os.path.join(template_path, "local_broadcasting.py")
    # params_file = os.path.join(template_path, "parameters_local_broadcasting.json")

    # print(executor_file)
    # print(params_file)

    # subprocess.call([sys.executable, executor_file, params_file])


    

    # with open('data.json', 'w') as f:
    #     json.dump(json.loads(data), f, indent=4) 