__author__ = 'Matthew'


from time import datetime
import requests
import creds

class Account:

    PUB_URL = 'https://platform-api.findthebest.com/API/v1/publisher/exists?name='
    TOKEN = creds.import_token

    '''
    Common class for all API account activity, which may include adding vizualizations, removing visualizations from an account
    '''

    def __init__(self,client_name):
        self.client_name = client_name
        self.date_modified = datetime.datetime.now()


    def removeAllVisualizations(self):
        return


    def removeVisualizationsWhere(self):
        return


    def importStardardPackage(self,package,prefs):
        return


    def importCustomPackage(self,package,prefs):
        return


    def importVisualization(self,client,vid,prefs):
        return


    def launchProduct(self,vid,exclude=None):
        return
