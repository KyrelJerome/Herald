import yaml

class CredentialFactory:
    def __init__(self, path):
        self.path = path

    def loadYaml(self):
        
        with open(self.path, 'r') as stream:
            try:
                creds = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def getPassword(self, app_key):
        return creds.get(app_key, None)
