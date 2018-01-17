import threading,xbmc,xbmcplugin,xbmcgui,re,os,xbmcaddon,sys
import shutil,plugintools
import zipfile
import urlparse
import urllib,urllib2,json
import common,xbmcvfs,downloader,extract
import datetime
import base64, time
import unicodedata
AddonID = 'plugin.video.redalert'
AddonTitle = 'Red Alert'
ADDON=xbmcaddon.Addon(id='plugin.video.redalert')
dialog       =  xbmcgui.Dialog()
dialogprocess =  xbmcgui.DialogProgress()
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
HOME         =  xbmc.translatePath('special://home/')
Images=xbmc.translatePath(os.path.join('special://home','addons',AddonID,'resources/art/'));
Username=plugintools.get_setting("Username")
Password=plugintools.get_setting("Password")
lehekylg= base64.b64decode("aHR0cDovL3JlZGFsZXJ0MTk3My5kZG5zLm5ldA==") #####
pordinumber=""
AddonRes = xbmc.translatePath(os.path.join('special://home','addons',AddonID,'resources'))
loginurl   = base64.b64decode("JXM6JXMvZ2V0LnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcyZ0eXBlPW0zdV9wbHVzJm91dHB1dD10cw==")%(lehekylg,pordinumber,Username,Password)

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database
def Add_Directory_Item(handle, url, listitem, isFolder):
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder)

def correctPVR():

	try:
		connection = urllib2.urlopen(loginurl)
		print connection.getcode()
		connection.close()
		#playlist found, user active & login correct, proceed to addon
		pass
		
	except urllib2.HTTPError, e:
		print e.getcode()
		dialog.ok("[COLOR white]Error[/COLOR]",'[COLOR white]This process will not run as your account has expired[/COLOR]',' ','[COLOR white]Please check your account information[/COLOR]')
		sys.exit(1)
		xbmc.executebuiltin("Dialog.Close(busydialog)")
		

	RAM = int(xbmc.getInfoLabel("System.Memory(total)")[:-2])
	RAMM = xbmc.getInfoLabel("System.Memory(total)")
	
	if RAM < 1999:
		choice = xbmcgui.Dialog().yesno('[COLOR white]Low Power Device [COLOR lime]RAM: ' + RAMM + '[/COLOR][/COLOR]', '[COLOR white]Your device has been detected as a low end device[/COLOR]', '[COLOR white]We recommend avoiding PVR usage for this reason[/COLOR]', '[COLOR white]We cannnot support low end devices for PVR[/COLOR]', nolabel='[COLOR lime]OK, Cancel this[/COLOR]',yeslabel='[COLOR red]I know, proceed[/COLOR]')
		if choice == 0:
			sys.exit(1)
		elif choice == 1:
			pass
	xbmc.executebuiltin("ActivateWindow(busydialog)")
	nullPVR   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":false},"id":1}'
	nullLiveTV = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":false},"id":1}'
	jsonSetPVR = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
	IPTVon 	   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
	nulldemo   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
	EPGurl   = base64.b64decode("JXM6JXMveG1sdHYucGhwP3VzZXJuYW1lPSVzJnBhc3N3b3JkPSVz")%(lehekylg,pordinumber,Username,Password)

	xbmc.executeJSONRPC(nullPVR)
	xbmc.executeJSONRPC(nullLiveTV)
	time.sleep(5)
	xbmc.executeJSONRPC(jsonSetPVR)
	xbmc.executeJSONRPC(IPTVon)
	xbmc.executeJSONRPC(nulldemo)
	
	moist = xbmcaddon.Addon('pvr.iptvsimple')
	moist.setSetting(id='m3uUrl', value=loginurl)
	moist.setSetting(id='epgUrl', value=EPGurl)
	moist.setSetting(id='m3uCache', value="false")
	moist.setSetting(id='epgCache', value="false")
	xbmc.executebuiltin("Dialog.Close(busydialog)")
	dialog.ok("[COLOR white]" + AddonTitle + "[/COLOR]",'[COLOR white]We\'ve copied your logins to the PVR Guide[/COLOR]',' ','[COLOR white]You [B]MUST[/B] allow time to load the EPG to avoid issues.[/COLOR]')

def disablePVR():
	xbmc.executebuiltin("ActivateWindow(busydialog)")
	nullPVR   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":false},"id":1}'
	nullLiveTV = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":false},"id":1}'
	PVRdata   =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/','pvr.iptvsimple'))
	xbmc.executeJSONRPC(nullPVR)
	xbmc.executeJSONRPC(nullLiveTV)
	shutil.rmtree(PVRdata)
	xbmc.executebuiltin("Container.Refresh")
	xbmc.executebuiltin("Dialog.Close(busydialog)")
	dialog.ok("[COLOR white]" + AddonTitle + "[/COLOR]",'[COLOR white]PVR Guide is now disabled[/COLOR]',' ','[COLOR white]You may set this up again any time[/COLOR]')

def SpeedChoice():
	choice = dialog.select("[COLOR white]" + AddonTitle + " Speedtest[/COLOR]", ['[COLOR white]Ookla Speedtest[/COLOR]','[COLOR white]Fast.com Speedtest by Netflix[/COLOR]'])
	if choice == 0:
		xbmc.executebuiltin('Runscript("special://home/addons/plugin.video.redalert/speedtest.py")') ###############
	if choice == 1:
		xbmc.executebuiltin('Runscript("special://home/addons/plugin.video.redalert/fastload.py")')  ###############

def iVueInt():

	try:
		connection = urllib2.urlopen(loginurl)
		print connection.getcode()
		connection.close()
		#playlist found, user active & login correct, proceed to addon
		pass
		
	except urllib2.HTTPError, e:
		print e.getcode()
		dialog.ok("[COLOR white]Error[/COLOR]",'[COLOR white]This process will not run as your account has expired[/COLOR]',' ','[COLOR white]Please check your account information[/COLOR]')
		sys.exit(1)
		xbmc.executebuiltin("Dialog.Close(busydialog)")

	xbmc.executebuiltin("ActivateWindow(busydialog)")
	iVue_SETTINGS = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.ivueguide','settings.xml'))
	UseriVueSets = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.ivueguide','oldsettings.xml'))
	AddoniVueSet = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.redalert/resources','ivueset.xml')) ###############
	iVue_DATA = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.ivueguide/'))
	if not xbmc.getCondVisibility('System.HasAddon(script.ivueguide)'):
		install('iVue','https://raw.githubusercontent.com/totaltec2014/ivue2/master/script.ivueguide/script.ivueguide-3.0.3.zip')
		install('iVue','https://raw.githubusercontent.com/totaltec2014/ivue2/master/xbmc.repo.ivueguide/xbmc.repo.ivueguide-0.0.1.zip')
		xbmc.executebuiltin("UpdateAddonRepos")
		xbmc.executebuiltin("UpdateLocalAddons")
		time.sleep(5)

	if not xbmc.getCondVisibility('System.HasAddon(xbmc.repo.ivueguide)'):
		install('iVue','https://raw.githubusercontent.com/totaltec2014/ivue2/master/xbmc.repo.ivueguide/xbmc.repo.ivueguide-0.0.1.zip')
		xbmc.executebuiltin("UpdateAddonRepos")
		xbmc.executebuiltin("UpdateLocalAddons")
		time.sleep(5)

	if not os.path.isfile(iVue_SETTINGS):
		if not os.path.exists(iVue_DATA):
			os.makedirs(iVue_DATA)
		shutil.copyfile(AddoniVueSet, iVue_SETTINGS)
	else:
		os.remove(iVue_SETTINGS)
		xbmc.log('Old iVue settings deleted')
		if not os.path.exists(iVue_DATA):
			os.makedirs(iVue_DATA)
		shutil.copyfile(AddoniVueSet, iVue_SETTINGS)

	EnableiVue   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"script.ivueguide","enabled":true},"id":1}'
	xbmc.executeJSONRPC(EnableiVue)	
	
	FullDB = os.path.join(AddonRes, 'fullivue.zip')
	dp = xbmcgui.DialogProgress()
	dp.create(AddonTitle,"Copying DB",'', 'Please Wait')
	unzip(FullDB,iVue_DATA,dp)
	xbmc.log("Full iVue Master DB Copied")
	xbmc.executebuiltin('Runscript("special://home/addons/plugin.video.redalert/fullivue.py")') ###############

def install(name,url):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create(AddonTitle,"Installing...",'', 'Please Wait')
    lib=os.path.join(path, 'content.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://home','addons'))
    time.sleep(3)
    dp = xbmcgui.DialogProgress()
    dp.create(AddonTitle,"Installing...",'', 'Please Wait')
    dp.update(0,"", "Installing... Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    unzip(lib,addonfolder,dp)

def unzip(_in, _out, dp):
	__in = zipfile.ZipFile(_in,  'r')
	
	nofiles = float(len(__in.infolist()))
	count   = 0
	
	try:
		for item in __in.infolist():
			count += 1
			update = (count / nofiles) * 100
			
			if dp.iscanceled():
				dialog = xbmcgui.Dialog()
				dialog.ok(AddonTitle, 'Process was cancelled.')
				
				sys.exit()
				dp.close()
			
			try:
				dp.update(int(update))
				__in.extract(item, _out)
			
			except Exception, e:
				print str(e)

	except Exception, e:
		print str(e)
		return False
		
	return True	

def AddDir(name, url, mode, iconimage, description="", isFolder=True, background=None):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    a=sys.argv[0]+"?url=None&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    print name.replace('-[US]','').replace('-[EU]','').replace('[COLOR yellow]','').replace('[/COLOR]','').replace(' (G)','')+'='+a
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def AddDir2(name, url, mode, iconimage, description="", isFolder=True, background=None):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    a=sys.argv[0]+"?url=None&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def addItem(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addXMLMenu(name,url,mode,iconimage,fanart,description):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
    liz.setProperty( "Fanart_Image", fanart )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def OPEN_URL_NORMAL(url):

	if "https://" in url:
		url = url.replace("https://","http://")
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
	response = urllib2.Request(req)
	link=response.read()
	response.close()
	return link

"""def ExtraMenuu():
    link = OPEN_URL('http://futurestreams.tk/Backup/Downloads/ExtrasList2.xml').replace('\n','').replace('\r','')  #Spaf
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,FanArt,description in match:
        addXMLMenu(name,url,6,iconimage,FanArt,description)"""

def Buildlist(url):
    list = common.m3u2list(url)
    for channel in list:
        name = common.GetEncodeString(channel["display_name"])
        AddDir(name ,channel["url"], 3, iconimage, isFolder=False)
		
def PlayUrl(name, url, iconimage=None):
        _NAME_=name
        list = common.m3u2list(loginurl)
        for channel in list:
            name = common.GetEncodeString(channel["display_name"])
            stream=channel["url"]
            if _NAME_ in name:
                listitem = xbmcgui.ListItem(path=stream, thumbnailImage=iconimage)
                listitem.setInfo(type="Video", infoLabels={ "Title": name })
                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)				

def Get_Params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?','')
        if (params[len(params)-1] == '/'):
            params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0].lower()] = splitparams[1]
    return param
	
params=Get_Params()
url=None
name=None
mode=None
iconimage=None
description=None

try:url = urllib.unquote_plus(params["url"])
except:pass
try:name = urllib.unquote_plus(params["name"])
except:pass
try:iconimage = urllib.unquote_plus(params["iconimage"])
except:pass
try:mode = int(params["mode"])
except:pass
try:description = urllib.unquote_plus(params["description"])
except:pass

if mode == 7:
	quit
if mode == 6:
	FootballSchedule()
elif mode == 8:
	iVuemenu()
elif mode == 12:
	PVRmenu()
elif mode == 1:
	Buildlist(url)
elif mode == 3:
    PlayUrl(name, url, iconimage)
elif mode == 9:
	SpeedChoice()
elif mode == 10:
	correctPVR()
elif mode == 11:
	xbmc.executebuiltin('ActivateWindow(TVGuide)')
elif mode == 13:
	iVueInt()
elif mode == 14:
    xbmc.executebuiltin('RunAddon(script.ivueguide)')
elif mode == 17:
	disablePVR()