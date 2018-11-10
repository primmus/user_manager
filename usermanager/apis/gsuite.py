from google.oauth2 import service_account
import googleapiclient.discovery
import user
import sys

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
SERVICE_ACCOUNT_FILE = 'service.json'
# TODO: Move the user account to the settings files
SUBJECT = 'sergio.bestetti@distilled.ie'

def getService():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(SUBJECT)
    return googleapiclient.discovery.build('admin', 'directory_v1', credentials=delegated_credentials)

def disableUser(userToDisable):
    service = getService()
    myBody = {
        "suspended": True
    }
    tmp = service.users().update(userKey=userToDisable.gMainEmail, body=myBody).execute()    

def searchUser(userToSearch):        
    try:        
        service = getService()
        results = service.users().get(userKey=userToSearch.gMainEmail, projection='basic').execute()        
        userToSearch.firstName = results['name']['givenName']
        userToSearch.lastName = results['name']['familyName']
        userToSearch.gMainEmail = results['primaryEmail']
        userToSearch.gAdmin = results['isAdmin']
        userToSearch.gOu = results['orgUnitPath']
        
        for item in results['emails']:
            userToSearch.gEmailAliases.append(item['address'])
        
        if 'nonEditableAliases' in results:
            for item in results['nonEditableAliases']:
                userToSearch.gEmailAliases.append(item)
        
        userToSearch.gExists = True     
            
    except:        
        return userToSearch

    return userToSearch