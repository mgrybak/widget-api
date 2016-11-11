__author__ = 'Matthew'

import register
import register_new_client


'''
Client Details
'''
client_name = register_new_client.PUBLISHER_NAME
client_domain = register_new_client.DOMAIN
client_color = register_new_client.COLOR_THEME
client_gmaps_key = register_new_client.GMAPS_API_KEY


if action == "EXCHANGE":
    '''
    Exchange all Prog API entries with new visualizations containing new preferences
    '''
    #DELETE ALL PROG API ENTRIES FOR PUBLISHER
    #ADD PROG API ENTRIES TO PROG API AND ONBOARDING TRACKER



if action == "REGISTER ACCOUNT":
    '''
    Register a new client with a standard package or custom package
    '''
    new_client = register.Client(client_name)



if action == "REMOVE ACCOUNT":
    '''
    Register a new client with a standard package or custom package
    '''
    new_client = register.Client(client_name)



if action == "ADD":
    '''
    Add specific visualizations to an individual client's account
    '''



if action == "REMOVE":
    '''
    Remove specific visualizations from a client's account
    '''



if action == "PRODUCT LAUNCH":
    '''
    Add specific visualizations to every user in the API partners topic
    '''



if __name__ == "__main__":
    action = sys.