import base64 as b
import xbmcaddon
id   = b.b64decode('cGx1Z2luLnZpZGVvLnJlZGFsZXJ0')

name = b.b64decode('UmVkIEFsZXJ0')

port = b.b64decode('ODA=')

def host():
	if xbmcaddon.Addon().getSetting('direct') == 'true':
		url = b.b64decode('aHR0cDovL3JlZGFsZXJ0MTk3Ny5jb20=')
	else:
		url = b.b64decode('aHR0cDovL3JlZGFsZXJ0MTk3My5kZG5zLm5ldA==')
	return url