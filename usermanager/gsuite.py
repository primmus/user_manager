from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
SERVICE_ACCOUNT_FILE = 'service.json'

def searchUser(username):
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject('sergio.bestetti@distilled.ie')
    service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=delegated_credentials)
    if '@' in username:
        username = username.split('@')[0]
    email = username + '@distilled.ie'
    try:
        results = service.users().get(userKey=email, projection='basic').execute()
    except:
        return 1

    return results 