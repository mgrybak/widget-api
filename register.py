__author__ = 'Matthew'

from time import datetime
import requests
import creds

class Client:

    PUB_URL = 'https://platform-api.findthebest.com/API/v1/publisher/exists?name='
    TOKEN = creds.import_token

    '''
    Common class for all publisher registration activity, which includes registering a new client and removing existing clients
    '''

    def __init__(self,name):
        self.name = name
        self.date_modified = datetime.datetime.now()


    def getPublisherID(self):
        return


    def clientExists(self):
        url = PUB_URL + self.name
        headers = {
        'token': TOKEN
        }
        try:
            response = requests.get(url, headers=headers)
            response_dict = json.loads(response.text)
            if response_dict['exists'] = "true":
                return True
            elif response_dict['exists'] = "false":
                return False
        except requests.exceptions.RequestException as e:
            print e
            sys.exit(1)


    def removeClient(self,name):
        return

    def registerNewClient(self,domain,theme_color=None,gmaps_api_key=None):
        client_data = {'name':self.name,'domain':domain}
        '''
        CHANGE TO MATCH COLUMN NAMES
        if theme_color:
            client_data['pub_theme_color'] = theme_color
        if gmaps_api_key:
            client_data['pub_maps_api_key'] = gmaps_api_key
        '''
        headers = {
        'token': TOKEN
        }
        payload = {'data': json.dumps(client_data)}
        try:
            response = requests.request("POST", IMPORT_URL.format(app_id), data=payload, headers=headers)
            print response.text
        except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)

    def editClient(self,name):
        return