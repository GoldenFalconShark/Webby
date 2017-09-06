import httplib2
import qs
from apiclient import errors

def getNgrok():
        credentials = qs.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = qs.discovery.build('drive', 'v3', http=http)
        qs.get_file(service,'0B8bBACMvHqiMUFdlR014TW10U3M','/var/lib/openshift/574de04d7628e10c4900014c/app-root/repo/ngrok.txt')
