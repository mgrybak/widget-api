__author__ = 'Matthew'

from time import datetime

class Client:
    '''
    Common class for all client-related activity, which may include onboarding, removing, and modifying an account
    '''

    def __init__(self,action):
        self.action = action
        self.date_modified = datetime.datetime.now()


    def registerNewClient(self,name):
        self.
