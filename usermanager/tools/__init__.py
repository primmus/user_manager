import user
from apis import activedirectory, gsuite

def getUser(username):
    userToSearch = user.User()
    if '@' in username:
        username = username.split('@')[0]
    email = username + '@distilled.ie'
    userToSearch.login = username
    userToSearch.gMainEmail = email

    activedirectory.searchUser(userToSearch)
    gsuite.searchUser(userToSearch)

    return userToSearch

