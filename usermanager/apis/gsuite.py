from google.oauth2 import service_account
import googleapiclient.discovery
import sys
import user
import apis.database

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.datatransfer']
SERVICE_ACCOUNT_FILE = 'service.json'
# TODO: Move the user account to the settings files
SUBJECT = 'sergio.bestetti@distilled.ie'

def getEmailService():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(SUBJECT)
    return googleapiclient.discovery.build('admin', 'directory_v1', credentials=delegated_credentials)

def getDatatransferService():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(SUBJECT)
    return googleapiclient.discovery.build('admin', 'datatransfer_v1', credentials=delegated_credentials)


def disableUser(userToDisable):
    service = getEmailService()
    myBody = {
        "suspended": True
    }
    tmp = service.users().update(userKey=userToDisable.gMainEmail, body=myBody).execute()    

def searchUser(userToSearch):        
    try:        
        service = getEmailService()
        results = service.users().get(userKey=userToSearch.gMainEmail, projection='basic').execute()
        userToSearch.firstName = results['name']['givenName']
        userToSearch.lastName = results['name']['familyName']
        userToSearch.gMainEmail = results['primaryEmail']
        userToSearch.gAdmin = results['isAdmin']
        userToSearch.gOu = results['orgUnitPath']
        userToSearch.gId = results['id']        
        
        for item in results['emails']:
            userToSearch.gEmailAliases.append(item['address'])
        
        if 'nonEditableAliases' in results:
            for item in results['nonEditableAliases']:
                userToSearch.gEmailAliases.append(item)
        
        userToSearch.gExists = True     
            
    except:        
        return userToSearch

    return userToSearch

def dataTransfer(originUser, destinationUser):
    service = getDatatransferService()    
    dataTransferRequestBody = {
        "oldOwnerUserId": originUser.gId,
        "newOwnerUserId": destinationUser.gId,
        "applicationDataTransfers": [
            {"applicationId": 55656082996}
        ]
    }
    response = service.transfers().insert(body=dataTransferRequestBody).execute()
    apis.database.addTask(response['id'], originUser, destinationUser)

def dataTransferChecker(taskId):    
    service = getDatatransferService()    
    response = service.transfers().get(dataTransferId=taskId).execute()
    print("Transfer status: {}".format(response['overallTransferStatusCode']))
