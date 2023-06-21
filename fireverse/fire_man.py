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

    