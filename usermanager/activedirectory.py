from ldap3 import Server, Connection, NTLM, ALL, MODIFY_ADD, MODIFY_REPLACE
import json
import uuid

# Load settings from the json file and generate
# the server object to be used on all connections
ad_config = json.loads(open('settings.json').read())
server = Server(ad_config['server'], use_ssl=True, get_info=ALL)

def convertGuid(rdGuid):
# Function for Formating AD ObjectGuid in Little Endian Format for Searches
# (e.g. 7fcb5751-bb65-4035-aa51-230a715faa8a will return \51\57\CB\7F\65\BB\35\40\AA\51\23\0A\71\5F\AA\8A)

	#Var for Return Value
	fltrGuid = ""

	#Parse into Guid
	wrkGuid = uuid.UUID('{' + rdGuid + '}')

	for wrkByte in wrkGuid.bytes_le:
		fltrGuid += "\\" + "{:02x}".format(wrkByte).upper()

	return fltrGuid

def getUserDN(username):
        # Return the full CN for the given username
        response = {}
        adFilter = "(&(objectclass=user)(!(objectclass=computer))(sAMAccountName=" + username  + "))"
        with Connection(server,
                        user=ad_config['user'],
                        password=ad_config['password'],
                        authentication=NTLM,
                        auto_bind=True
                ) as conn:
                        conn.search(
                                search_base=ad_config['users_ou'],
                                search_filter=adFilter,
                                attributes = ["distinguishedName"]
                        )
                        response['dn'] = str(conn.entries[0].distinguishedName)
                        return response