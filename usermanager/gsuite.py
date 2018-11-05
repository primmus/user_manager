from google.oauth2 import service_account
import googleapiclient.discovery
import user

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
SERVICE_ACCOUNT_FILE = 'service.json'

def searchUser(userToSearch):    
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject('sergio.bestetti@distilled.ie')
    service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=delegated_credentials)    
    try:        
        results = service.users().get(userKey=userToSearch.email, projection='basic').execute()
        
        userToSearch.firstName = results['name']['givenName']
        userToSearch.lastName = results['name']['familyName']
        userToSearch.gMainEmail = results['primaryEmail']
        userToSearch.gAdmin = results['isAdmin']
        userToSearch.gOu = results['orgUnitPath']
        
        for item in results['emails']:
            userToSearch.gEmailAliases.append(item['address'])
        
        for item in results['nonEditableAliases']:
            userToSearch.gEmailAliases.append(item)
        
        userToSearch.gExists = True
            
    except:
        return userToSearch

    return userToSearch