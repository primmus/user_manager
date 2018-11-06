class User():

    def __init__(self):
        # General properties
        self.firstName = ''
        self.lastName = ''
        self.login = ''
        self.location = ''
        self.password = ''
        self.services = list()
        self.vpn = list()        
        #  Active Directory properties
        self.adExists = False
        self.adGroups = list()
        self.adGroups = list()
        self.adDn = ''        
        self.adAccountStatus = ''
        self.adWrongPasswordAttempts = 0
        # Google properties
        self.gExists = False
        self.gMainEmail = ''
        self.gEmailAliases = list()
        self.gAdmin = False
        self.gOu = ''
     
    def setAdAccountStatus(self, statusCode):
        if statusCode == 512:
            self.adAccountStatus = 'Active'
        elif statusCode == 514:
            self.adAccountStatus = 'Account disabled'
        elif statusCode == 528:
            self.adAccountStatus = 'Account locked out'
        elif statusCode == 8389120:
            self.adAccountStatus = 'Password expired'
        elif statusCode == 0:
            self.adAccountStatus = 'Not set'
        elif statusCode == 66048:
            self.adAccountStatus = 'Password never expires'
        else:
            self.adAccountStatus = 'Unhandled status - ' + str(statusCode)
   
    def getFullName(self):
        fullName = self.firstName + ' ' + self.lastName
        fullName = fullName.title()
        return fullName

    def __str__(self):
        response = ('GSuite user: {}\nAD user: {}\nLogin: {}\nName: {} {}'
                    '\nMain email: {}\nLocation: {}\nEmail aliases: {}'
                    '\nAD account status: {}\nDN: {}\nAD groups: {}').format(
            self.gExists,
            self.adExists,
            self.login,
            self.firstName.title(),
            self.lastName.title(),
            self.gMainEmail,
            self.location.title(),
            self.gEmailAliases,
            self.adAccountStatus,
            self.adDn,
            self.adGroups
        )       
        
        return response