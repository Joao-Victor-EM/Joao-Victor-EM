import os
import json
import requests

class FirebaseProjectManager:
    def __init__(self, base_project_path):
        self.base_project_path = base_project_path
        self.current_branch = None
        self.cross_domain = None
        self.firebase_projects = None
        self.selected_project = None
        self.android_apps = None

    def switch_git_branch(self):
        # Implement your logic here to switch Git branches
        pass
    
    def get_cross_domain(self):
        with open(os.path.join(self.base_project_path, 'google-services.json')) as file:
            data = json.load(file)
            self.cross_domain = data['project_id']
    
    def access_firebase_management_api(self):
        url = 'https://firebase.googleapis.com/v1beta1/projects'
        #add headers for authentication
        response = requests.get(url)
        self.firebase_projects = response.json()

    def iterate_over_projects(self):
        for project in self.firebase_projects:
            if project['project_id'] == self.cross_domain:
                self.selected_project = project
                break

    def check_android_app_domain(self):
        project_id = self.selected_project['project_id']
        url = f'https://firebase.googleapis.com/v1beta1/{project_id}/androidApps'
        #add headers for authentication
        response = requests.get(url)
        self.android_apps = response.json()
    
    def verify_app_domain_registration(self):
        app_nickname = self.selected_project['app_nickname']
        for app in self.android_apps:
            if self.cross_domain in app['package_name'] and app_nickname in app['app_nickname']:
                return True
        return False
    
    def perform_filter_action(self):
        package_name = self.android_apps[0]['package_name']
        if self.cross_domain == package_name.split('.')[0]:
            version = 'V5'
        else:
            version = 'V4'
        return version
    
    def build_answer(self):
        answer = {}
        branches = ['main', 'hmg', 'dev']
        for branch in branches:
            answer[branch] = []
            self.switch_git_branch(branch)
            self.get_cross_domain()
            self.access_firebase_management_api()
            self.iterate_over_projects()
            self.check_android_app_domain()
            if self.verify_app_domain_registration():
                version = self.perform_filter_action()
                answer[branch].append({self.cross_domain: version})
        return answer

    def check_goal(self, answer):
        for branch, app_list in answer.items():
            if len(app_list) > 1:
                return False
        return True