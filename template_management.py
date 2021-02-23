from git import Repo
import os
from functions import read_json_parameters, write_json

class Template_manager:

    def __init__(self, user, token_pass):
        self.user = user
        self.token_pass = token_pass
    
    def git_clone(self, remote_repo, local_repo_dest):
        
        https = "https://"
        
        try:        
            if https in remote_repo:
                rm_repo = remote_repo.replace(https, '')            
            else:
                rm_repo = remote_repo

            Repo.clone_from(https + '{0}:{1}@{2}'.format(self.user,
                                                        self.token_pass,
                                                        rm_repo
                                                        ), local_repo_dest)
        except Exception as e:
            print(e)

    def git_stage_commit(self, sel_repo):
        #Check changes in the repo
        if sel_repo.is_dirty(untracked_files = True):
            print('Changes detected.')
            #Stage all changes
            sel_repo.git.add(update = True)
            #Commit
            sel_repo.index.commit('Commit last changes')
            print("Commit succesful")
        else:
            print("No changes detected")
    
    def git_select_local_repo(self, local_repo_dest):
        try:
            selected_repo = Repo(local_repo_dest)
            return selected_repo
        except Exception as e:
            print(e)            
        
    def git_checkout(self, selected_repo, selected_checkout):
        try:
            selected_repo.git.checkout(selected_checkout)
        except Exception as e:
            print(e)
    
    def create_json_parameters(self, json, local_repo_dest, json_name):
        try:
            write_json(json, os.path.join(local_repo_dest, json_name))
        except Exception as e:
            print(e)
    
    # def execute_template(self, local_repo_dest, template_executor, parameters):
    #     # execfile('file.py')
    #     os.system('python ' + os.path.join(local_repo_dest, template_executor) '')