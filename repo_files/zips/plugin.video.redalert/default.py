import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os,json,base64,plugintools
import GoDev
import common,xbmcvfs,zipfile,downloader,extract
import xml.etree.ElementTree as ElementTree
import unicodedata
import time
import string
reload(sys)
dialog       =  xbmcgui.Dialog()
sys.setdefaultencoding('utf8')
SKIN_VIEW_FOR_MOVIES="515"
addonDir = plugintools.get_runtime_path()
global kontroll
background = "ZmFuYXJ0LmpwZw==" 
defaultlogo = "ZmFuYXJ0LmpwZw==" 
hometheater = "ZmFuYXJ0LmpwZw=="
noposter = "aWNvbi5wbmc="
theater = "ZmFuYXJ0LmpwZw=="
addonxml = "YWRkb24ueG1s"
addonpy = "ZGVmYXVsdC5weQ=="
icon = "aWNvbi5wbmc="
supplier = "UmVkIEFsZXJ0" #####
fanart = "ZmFuYXJ0LmpwZw=="
GuideLoc = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.redalert', 'g')) #####
Guide = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.redalert', 'guide.xml')) #####
lehekylg= base64.b64decode("aHR0cDovL3JlZGFsZXJ0MTk3My5kZG5zLm5ldA==") #####
pordinumber=""
message = "VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"
kasutajanimi=plugintools.get_setting("Username")
salasona=plugintools.get_setting("Password")
LOAD_LIVEchan = os.path.join( plugintools.get_runtime_path() , "resources" , "art/arch" )

def run():
    global pnimi
    global televisioonilink
    global filmilink
    global andmelink
    global uuenduslink
    global lehekylg
    global LOAD_LIVE
    global uuendused
    global vanemalukk
    global version
    version = int(get_live("MQ=="))
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    if not kasutajanimi:
        kasutajanimi = "NONE"
        salasona="NONE"
	
    uuendused=plugintools.get_setting(sync_data("dXVlbmR1c2Vk"))
    vanemalukk=plugintools.get_setting(sync_data("dmFuZW1hbHVraw=="))
    pnimi = get_live("T25lIFZpZXcg")
    LOAD_LIVE = os.path.join( plugintools.get_runtime_path() , "resources" , "art" )
    plugintools.log(pnimi+get_live("U3RhcnRpbmcgdXAgLSBCZW4gRXBpYyB3aW5zIQ=="))
    televisioonilink = get_live("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9jYXRlZ29yaWVz")%(lehekylg,pordinumber,kasutajanimi,salasona)
    filmilink = vod_channels("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX2NhdGVnb3JpZXM=")%(lehekylg,pordinumber,kasutajanimi,salasona)
    andmelink = vod_channels("JXM6JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw==")%(lehekylg,pordinumber,kasutajanimi,salasona)
    params = plugintools.get_params()

    if params.get("action") is None:
        peamenyy(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def peamenyy(params):
    plugintools.log(pnimi+vod_channels("TWFpbiBNZW51IC0gQmVuIEVwaWMgV2lucyE=")+repr(params))
    load_channels()
    if not lehekylg:
        plugintools.open_settings_dialog()

    channels = kontroll()
    if channels == 1 and GoDev.mode != 5 and GoDev.mode != 1:
        plugintools.log(pnimi+vod_channels("TG9naW4gU3VjY2VzcyAtIEJlbiBFcGljIFdpbnMh"))
        plugintools.add_item( action=vod_channels("ZXhlY3V0ZV9haW5mbw=="),   title="Account Information", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        plugintools.add_item( action=vod_channels("c2VjdXJpdHlfY2hlY2s="),  title= "" + vod_channels(supplier) + " TV" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        plugintools.add_item( action=vod_channels("ZGV0ZWN0X21vZGlmaWNhdGlvbg=="),   title="On Demand" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        plugintools.add_item( action=vod_channels("VGhlRGV2"),   title="" + vod_channels(supplier) + " CatchUp" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
        plugintools.add_item( action=vod_channels("U1BPUlRfTElTVElOR1M="),   title="UK Sport Listings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title="Settings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("c2V0dGluZ3MucG5n")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )
        plugintools.addItem('Run Speedtest','speed',9,GoDev.Images + 'speed.png',GoDev.Images + 'background.png')
        if not xbmc.getCondVisibility('Pvr.HasTVChannels'):
            plugintools.addItem('Setup IPTV Simple PVR','pvr',10,GoDev.Images + 'extras.png',GoDev.Images + 'background.png')
        else:
            plugintools.addItem('Launch PVR','pvr',11,GoDev.Images + 'extras.png',GoDev.Images + 'background.png')
            plugintools.addItem('Disable PVR','pvr',17,GoDev.Images + 'extras.png',GoDev.Images + 'background.png')
        if not xbmc.getCondVisibility('System.HasAddon(script.ivueguide)'):
            plugintools.addItem('Run iVue Integration','pvr',13,GoDev.Images + 'extras.png',GoDev.Images + 'background.png')
        else:
            plugintools.addItem('Launch iVue Guide','pvr',14,GoDev.Images + 'extras.png',GoDev.Images + 'background.png')
            plugintools.addItem('Run iVue Integration','pvr',13,GoDev.Images + 'extras.png',GoDev.Images + 'background.png')
    elif channels != 1 and GoDev.mode != 1:
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title="Step 1. Insert Login Credentials" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")), folder=False )	
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjazI="), title="Step 2. Click Once Login Is Input" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")), folder=False )	
    if plugintools.get_setting("improve")=="true":
        advancedsettings = xbmc.translatePath(sync_data("c3BlY2lhbDovL3VzZXJkYXRhL2FkdmFuY2Vkc2V0dGluZ3MueG1s")) ##System advanced settings##
        if os.path.exists(advancedsettings):
            file = open( os.path.join(plugintools.get_runtime_path(),vod_channels("cmVzb3VyY2Vz"),sync_data("YWR2YW5jZWRzZXR0aW5ncy54bWw=")) ) ##app advanced settings##
            data = file.read()
            file.close()
            file = open(advancedsettings,"w")
            file.write(data)
            file.close()

def DownloaderClass(url, dest):
    dp = xbmcgui.DialogProgress()
    dp.create('Fetching latest Catch Up',"Fetching latest Catch Up...",' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))

def SPORT_LISTINGS(params):

	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A=')
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('href="http://www.wheresthematch.com/fixtures/(.+?).asp.+?class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em>.+?time-channel ">(.+?)</span>').findall(r)
	for game,team1,team2,gametime in match:
		a,b = gametime.split(" on ")
		plugintools.add_item (action="",  title='[COLOR white]'+team1+' vs '+team2+' - '+a+' [/COLOR]' , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )
		plugintools.add_item (action="",  title='[COLOR yellowgreen][B]Watch on '+b+'[/B][/COLOR]' , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )
		plugintools.add_item (action="",  title='------------------------------------------' , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )


def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            mbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % (currently_downloaded)
            e = '[COLOR white]Speed:  %.02f Mb/s ' % mbps_speed  + '[/COLOR]'
            dp.update(percent, mbs, e)
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled():
            dialog = xbmcgui.Dialog()
            dialog.ok(vod_channels(supplier), 'The download was cancelled.')
				
            sys.exit()
            dp.close()

def TheDev(params):

    loginurl   = base64.b64decode("JXM6JXMvZ2V0LnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcyZ0eXBlPW0zdV9wbHVzJm91dHB1dD10cw==")%(lehekylg,pordinumber,kasutajanimi,salasona)
    try:
        connection = urllib2.urlopen(loginurl)
        print connection.getcode()
        connection.close()
        #playlist found, user active & login correct, proceed to addon
        pass
        
    except urllib2.HTTPError, e:
        print e.getcode()
        dialog.ok("[COLOR white]Expired Account[/COLOR]",'[COLOR white]You cannot use this service with an expired account[/COLOR]',' ','[COLOR white]Please check your account information[/COLOR]')
        sys.exit(1)
        xbmc.executebuiltin("Dialog.Close(busydialog)")

    url = base64.b64decode("JXM6JXMveG1sdHYucGhwP3VzZXJuYW1lPSVzJnBhc3N3b3JkPSVz")%(lehekylg,pordinumber,kasutajanimi,salasona)
    DownloaderClass(url,GuideLoc + "uide.xml")
    
    f = open(Guide, 'r+')
    input = open(Guide).read().decode('UTF-8')
    output = unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')
    f.write(output)
    f.truncate()
    f.close()

    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMQ=="), title="[COLOR white]BBC One HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YmJjb25laGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMg=="), title="[COLOR white]BBC Two HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YmJjdHdvaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMw=="), title="[COLOR white]ITV HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlNA=="), title="[COLOR white]Channel 4 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("Y2hhbm5lbDRoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlNQ=="), title="[COLOR white]Channel 5 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("Y2hhbm5lbDVoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlNDM="), title="[COLOR white]ITV Encore HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2ZW5jb3JlaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlNg=="), title="[COLOR white]ITV 2 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2MmhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlNw=="), title="[COLOR white]ITV 3 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2M2hkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlOA=="), title="[COLOR white]ITV 4 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2NGhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlOQ=="), title="[COLOR white]ITVBE HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2YmVoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTA="), title="[COLOR white]Sky One HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5MWhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTE="), title="[COLOR white]Lifetime HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("bGlmZXRpbWVoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTI="), title="[COLOR white]Alibi HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YWxpYmloZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTM="), title="[COLOR white]Animal Planet HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YW5pbWFscGxhbmV0aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTQ="), title="[COLOR white]Dave HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("ZGF2ZWhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTU="), title="[COLOR white]Comedy Central HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("Y29tZWR5Y2VudHJhbGhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTY="), title="[COLOR white]Discovery Channel HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("ZGlzY292ZXJ5Y2hhbm5lbGhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTc="), title="[COLOR white]Eden HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("ZWRlbmhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTg="), title="[COLOR white]SyFy HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c3lmeWhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMTk="), title="[COLOR white]Nat Geo Wild HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("bmF0Z2Vvd2lsZGhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjA="), title="[COLOR white]National Geographic HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("bmF0aW9uYWxnZW9ncmFwaGljaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjE="), title="[COLOR white]BT Sport 1 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YnRzcG9ydDFoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjI="), title="[COLOR white]BT Sport 2 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YnRzcG9ydDJoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjM="), title="[COLOR white]BT Sport 3 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YnRzcG9ydDNoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjQ="), title="[COLOR white]BT Sport ESPN HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YnRzcG9ydGVzcG5oZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjU="), title="[COLOR white]Sky Sports 1 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQxaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjY="), title="[COLOR white]Sky Sports 2 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQyaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjc="), title="[COLOR white]Sky Sports 3 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQzaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjg="), title="[COLOR white]Sky Sports 4 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQ0aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMjk="), title="[COLOR white]Sky Sports 5 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQ1aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzA="), title="[COLOR white]Sky Sports F1 HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnRzZjFoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzE="), title="[COLOR white]Sky Sports MIX HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BtaXhoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzI="), title="[COLOR white]Sky Cinema Premiere HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hcHJlbWllcmVoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzM="), title="[COLOR white]Sky Cinema Drama & Romance HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hZHJhbWFoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzQ="), title="[COLOR white]Sky Cinema Greats HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hZ3JlYXRzaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzU="), title="[COLOR white]Sky Cinema Disney HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hZGlzbmV5aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzY="), title="[COLOR white]Sky Cinema Family HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hZmFtaWx5aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzc="), title="[COLOR white]Sky Cinema Action & Adventure HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hYWN0aW9uaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzg="), title="[COLOR white]Sky Cinema Comedy HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hY29tZWR5aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlMzk="), title="[COLOR white]Sky Cinema Crime & Thriller HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hdGhyaWxsZXJoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlNDA="), title="[COLOR white]Sky Cinema Hits HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1haGl0c2hkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlNDE="), title="[COLOR white]Sky Cinema Sci-fi & Horror HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hc2NpZmloZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )
    plugintools.add_item( action=sync_data("dHZhcmNoaXZlNDI="), title="[COLOR white]Sky Cinema Select HD[/COLOR]" , url="", thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hc2VsZWN0aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=False, folder=True )

def tvarchive1(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: BBC 1 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'308')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YmJjb25laGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive2(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: BBC 2 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'7')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YmJjdHdvaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive3(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: ITV HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'4')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive4(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: CHANNEL 4 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'5')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("Y2hhbm5lbDRoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive5(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: CHANNEL 5 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'420')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("Y2hhbm5lbDVoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive6(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: ITV2 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'15')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2MmhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive7(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: ITV3 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'365')
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'365')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2M2hkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive8(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: ITV4 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'366')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2NGhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive9(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: ITVBE HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'364')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2YmVoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive10(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: SKY ONE HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'336')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5MWhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive11(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: LIFETIME HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'53')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("bGlmZXRpbWVoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive12(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: ALIBI HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'640')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YWxpYmloZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive13(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='DOC: ANIMAL PLANET HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'605')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YW5pbWFscGxhbmV0aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive14(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: DAVE HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'630')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("ZGF2ZWhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive15(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: COMEDY CENTRAL HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'1036')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("Y29tZWR5Y2VudHJhbGhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive16(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='DOC: DISCOVERY CHANNEL HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'60')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("ZGlzY292ZXJ5Y2hhbm5lbGhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive17(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='DOC: EDEN HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'68')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("ZWRlbmhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive18(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: SYFY HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'329')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c3lmeWhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive19(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='DOC: NAT GEO WILD HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'67')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("bmF0Z2Vvd2lsZGhkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive20(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='DOC: NATIONAL GEOGRAPHIC HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'712')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("bmF0aW9uYWxnZW9ncmFwaGljaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive21(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='BTS: BT SPORT 1 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'25')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YnRzcG9ydDFoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive22(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='BTS: BT SPORT 2 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'33')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YnRzcG9ydDJoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive23(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='BTS: BT SPORT 3 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'35')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YnRzcG9ydDNoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive24(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='BTS: BT SPORT/ESPN HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'88')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("YnRzcG9ydGVzcG5oZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive25(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='SSS: SKY SPORTS 1 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'1')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQxaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive26(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='SSS: SKY SPORTS 2 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'26')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQyaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive27(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='SSS: SKY SPORTS 3 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'27')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQzaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive28(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='SSS: SKY SPORTS 4 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'28')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQ0aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive29(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='SSS: SKY SPORTS 5 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'32')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnQ1aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive30(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='SSS: SKY SPORTS F1 HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'30')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BvcnRzZjFoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive31(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='SSS: SKY SPORTS MIX HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'258')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5c3BtaXhoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive32(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA PREMIERE HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'42')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hcHJlbWllcmVoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive33(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA DRAMA & ROMANCE HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'37')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hZHJhbWFoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive34(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA GREATS HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'41')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hZ3JlYXRzaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive35(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA DISNEY HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'206')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hZGlzbmV5aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive36(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA FAMILY HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'40')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hZmFtaWx5aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive37(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA ACTION & ADVENTURE HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'38')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hYWN0aW9uaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive38(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA COMEDY HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'39')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hY29tZWR5aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive39(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA CRIME & THRILLER HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'207')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hdGhyaWxsZXJoZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive40(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA HITS HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'204')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1haGl0c2hkLnBuZw==")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive41(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA SCI-FI & HORROR HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'43')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hc2NpZmloZC5wbmc=")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive42(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='MOV: SKY CINEMA SELECT HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'208')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("c2t5Y2luZW1hc2VsZWN0aGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def tvarchive43(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.datetime.now() - datetime.timedelta(days=5)
    date = str(date3)
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if programme.attrib.get('channel') =='ENT: ITV ENCORE HD':
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = get_live("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,pordinumber,kasutajanimi,salasona,'19')
                    pony = poo1 + str(head) + "&duration=240"
                    kanalinimi = str(head2)+ " - " + programme.find('title').text
                    plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=pony, thumbnail=os.path.join(LOAD_LIVEchan,vod_channels("aXR2ZW5jb3JlaGQucG5n")) , plot="", fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )

def license_check(params):
    plugintools.log(pnimi+get_live("U2V0dGluZ3MgbWVudSAtIEJlbiBFcGljIHdpbnMh")+repr(params))
    plugintools.open_settings_dialog()
def license_check2(params):
	loginurl   = base64.b64decode("JXM6JXMvZ2V0LnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcyZ0eXBlPW0zdV9wbHVzJm91dHB1dD10cw==")%(lehekylg,pordinumber,kasutajanimi,salasona)
	try:
		connection = urllib2.urlopen(loginurl)
		print connection.getcode()
		connection.close()
		#playlist found, user active & login correct, proceed to addon
		xbmc.executebuiltin('Container.Refresh')
		
	except urllib2.HTTPError, e:
		print e.getcode()
		#playlist not found, either expired or wrong login

		#check for expired account
		content    = GoDev.OPEN_URL(andmelink)
		match    = re.compile('"auth":(.+?)').findall(content) 

		for result in match:
			if "0" in result:
				dialog.ok('[COLOR white]Invalid Login[/COLOR]','[COLOR white]Incorrect login details found![/COLOR]','[COLOR white]Please check your spelling and case sensitivity[/COLOR]','[COLOR white]Check your password with the team otherwise[/COLOR]')
				plugintools.open_settings_dialog()
			else:
				dialog.ok("[COLOR white]Expired Login[/COLOR]",'[COLOR white]Your login has expired[/COLOR]','[COLOR white]Please review your account information[/COLOR]','[COLOR white]or contact the team[/COLOR]')
				xbmc.executebuiltin('Container.Refresh')

def security_check(params):
    #plugintools.add_item( action=vod_channels("VFZzZWFyY2g="),   title="Search Shows on Now" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
    plugintools.log(pnimi+sync_data("TGl2ZSBNZW51")+repr(params))
    request = urllib2.Request(televisioonilink, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        kanalinimi = channel.find(get_live("dGl0bGU=")).text
        kanalinimi = base64.b64decode(kanalinimi)
        kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        CatID = channel.find(get_live("Y2F0ZWdvcnlfaWQ=")).text        
        plugintools.add_item( action=get_live("c3RyZWFtX3ZpZGVv"), title=kanalinimi , url=CatID , thumbnail=os.path.join(LOAD_LIVE,sync_data("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) ,info_labels=kanalinimi, folder=True )
	                            
    plugintools.set_view( plugintools.LIST )

def detect_modification(params):
    plugintools.add_item( action=vod_channels("Vk9Ec2VhcmNo"),   title="Search On Demand" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
    plugintools.log(pnimi+vod_channels("Vk9EIE1lbnUg")+repr(params))
    request = urllib2.Request(filmilink, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        filminimi = channel.find(get_live("dGl0bGU=")).text
        filminimi = base64.b64decode(filminimi)
        kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=vod_channels("Z2V0X215YWNjb3VudA=="), title=filminimi , url=kategoorialink , thumbnail=os.path.join(LOAD_LIVE,sync_data("dm9kLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=True )
	
    plugintools.set_view( plugintools.LIST )

def stream_video(params):
    plugintools.log(pnimi+sync_data("TGl2ZSBDaGFubmVscyBNZW51IA==")+repr(params))
    plugintools._log(vod_channels("QmVuIEVwaWMgQmxvb21maWVsZCB3aW5zIQ=="))
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    CatID = params.get(get_live("dXJs")) #description
    url = get_live("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9zdHJlYW1zJmNhdF9pZD0lcw==")%(lehekylg,pordinumber,kasutajanimi,salasona,CatID)
    request = urllib2.Request(url, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")): #channel
        kanalinimi = channel.find(get_live("dGl0bGU=")).text #title
        kanalinimi = base64.b64decode(kanalinimi)
        kanalinimi = kanalinimi.partition("[")
        striimilink = channel.find(get_live("c3RyZWFtX3VybA==")).text #stream_url
        pony = striimilink
        if ("%s:%s/enigma2.php")%(lehekylg,pordinumber)  in striimilink: 
            pony = striimilink.split(kasutajanimi,1)[1]
            pony = pony.split(salasona,1)[1]
            pony = pony.split("/",1)[1]            
        pilt = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text #desc_image
        kava = kanalinimi[1]+kanalinimi[2]
        kava = kava.partition("]")
        kava = kava[2]
        kava = kava.partition("   ")
        kava = kava[2]
        shou = get_live("W0NPTE9SIHdoaXRlXSVzIFsvQ09MT1Jd")%(kanalinimi[0])+kava
        kirjeldus = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text #description
        if kirjeldus:
           kirjeldus = base64.b64decode(kirjeldus)
           nyyd = kirjeldus.partition("(")
           nyyd = sync_data("Tm93OiA=") +nyyd[0]
           jargmine = kirjeldus.partition(")\n")
           jargmine = jargmine[2].partition("(")
           jargmine = sync_data("TmV4dDog") +jargmine[0] #shou
           kokku = nyyd+jargmine
        else:
           kokku = ""
        if pilt:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=pilt, plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")), extra="", isPlayable=True, folder=False )
        else:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=os.path.join(LOAD_LIVE,vod_channels("YWxsY2hhbm5lbHMucG5n")) , plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
    plugintools.set_view( plugintools.EPISODES )
    xbmc.executebuiltin(vod_channels("Q29udGFpbmVyLlNldFZpZXdNb2RlKDUwMyk="))

def open_url(url):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
    except:quit()

def VODsearch(params):
	SEARCH_LIST = base64.b64decode(b'JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX3N0cmVhbXMmY2F0X2lkPTA=')%(lehekylg,pordinumber,kasutajanimi,salasona)
	keyb = xbmc.Keyboard('', '[COLOR white]Search[/COLOR]')
	keyb.doModal()
	if (keyb.isConfirmed()):
		searchterm=keyb.getText()
		searchterm=string.capwords(searchterm)
	else:quit()
	xbmc.log('User searched for: '+ searchterm)
	link=open_url(SEARCH_LIST) 
	match = re.compile('<title>(.+?)</title><desc_image><!\[CDATA\[(.+?)\]\]></desc_image><description>(.+?)</description>.+?<stream_url><!\[CDATA\[(.+?)\]\]></stream_url>').findall(link)
	for pealkiri,pilt,kirjeldus,striimilink in match:
		pealkiri = base64.b64decode(pealkiri)
		pealkiri = pealkiri.encode("utf-8")
		if kirjeldus:
			kirjeldus = base64.b64decode(kirjeldus)
		if searchterm in pealkiri:
			xbmc.log('***************** FOUND IT *****************')
			if pilt:
				plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=pilt, plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
			else:
				plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=os.path.join("dm9kLnBuZw=="), plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )

def TVsearch(params):
	SEARCH_LIST = base64.b64decode(b'JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9zdHJlYW1zJmNhdF9pZD0w')%(lehekylg,pordinumber,kasutajanimi,salasona)
	keyb = xbmc.Keyboard('', '[COLOR white]Search[/COLOR]')
	keyb.doModal()
	if (keyb.isConfirmed()):
		searchterm=keyb.getText()
		searchterm=string.capwords(searchterm)
	else:quit()
	xbmc.log('User searched for: '+ searchterm)
	request = urllib2.Request(SEARCH_LIST, headers={"Accept" : "application/xml"})
	u = urllib2.urlopen(request)
	tree = ElementTree.parse(u)
	rootElem = tree.getroot()
	for channel in tree.findall(sync_data("Y2hhbm5lbA==")): #channel
		kanalinimi = channel.find(get_live("dGl0bGU=")).text #title
		kanalinimi = base64.b64decode(kanalinimi)
		kanalinimi = kanalinimi.partition("[")
		striimilink = channel.find(get_live("c3RyZWFtX3VybA==")).text #stream_url
		pony = striimilink
		if ("%s:%s/enigma2.php")%(lehekylg,pordinumber) in striimilink:
			pony = striimilink.split(kasutajanimi,1)[1]
			pony = pony.split(salasona,1)[1]
			pony = pony.split("/",1)[1]			
		pilt = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text #desc_image
		kava = kanalinimi[1]+kanalinimi[2]
		kava = kava.partition("]")
		kava = kava[2]
		kava = kava.partition("   ")
		kava = kava[2]
		shou = get_live("W0NPTE9SIHdoaXRlXSVzIFsvQ09MT1Jd")%(kanalinimi[0])+kava
		kirjeldus = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text #description
		if kirjeldus:
			kirjeldus = base64.b64decode(kirjeldus)
			nyyd = kirjeldus.partition("(")
			nyyd = sync_data("Tm93OiA=") +nyyd[0]
			jargmine = kirjeldus.partition(")\n")
			jargmine = jargmine[2].partition("(")
			jargmine = sync_data("TmV4dDog") +jargmine[0] #shou
			kokku = nyyd+jargmine
		else:
			kokku = ""
		if searchterm in kava:
			if pilt:
				plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=pilt, plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")), extra="", isPlayable=True, folder=False )
			else:
				plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=os.path.join(LOAD_LIVE,vod_channels("YWxsY2hhbm5lbHMucG5n")) , plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )

def get_myaccount(params):
        plugintools.log(pnimi+get_live("Vk9EIGNoYW5uZWxzIG1lbnUg")+repr(params))
        plugintools._log(vod_channels("QmVuIEVwaWMgQmxvb21maWVsZCB3aW5zIQ=="))
        if vanemalukk == "true":
           pealkiri = params.get("title")
           vanema_lukk(pealkiri)
        purl = params.get("url")
        request = urllib2.Request(purl, headers={"Accept" : "application/xml"})
        u = urllib2.urlopen(request)
        tree = ElementTree.parse(u)
        rootElem = tree.getroot()
        for channel in tree.findall("channel"):
            try:
                pealkiri = channel.find("title").text
                pealkiri = base64.b64decode(pealkiri)
                pealkiri = pealkiri.encode("utf-8")
                striimilink = channel.find("stream_url").text
                pilt = channel.find("desc_image").text
                kirjeldus = channel.find("description").text
                if kirjeldus:
                   kirjeldus = base64.b64decode(kirjeldus)
                if pilt:
                   plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=pilt, plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
                else:
                   plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=os.path.join("dm9kLnBuZw=="), plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
            except:
                kanalinimi = channel.find("title").text
                kanalinimi = base64.b64decode(kanalinimi)
                kategoorialink = channel.find("playlist_url").text
                plugintools._log(kategoorialink)
                CatID = channel.find("category_id").text
                plugintools.add_item( action=get_live("Z2V0X215YWNjb3VudA=="), title=kanalinimi , url=kategoorialink , thumbnail=os.path.join(LOAD_LIVE,sync_data("dm9kLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) ,info_labels=kanalinimi, folder=True )

        plugintools.set_view( plugintools.EPISODES )
        xbmc.executebuiltin('Container.SetViewMode(503)')

def run_cronjob(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    lopplink = params.get("url")
    if "http://"  not in lopplink: 
        lopplink = get_live("http://%s:%s/enigma.php/live/%s/%s/%s")%(lehekylg,pordinumber,kasutajanimi,salasona,lopplink)
        lopplink = lopplink[:-2]
        lopplink = lopplink + "ts"
    listitem = xbmcgui.ListItem(path=lopplink)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def sync_data(channel):
    video = base64.b64decode(channel)
    return video

def restart_service(params):
    lopplink = params.get(vod_channels("dXJs"))
    plugintools.play_resolved_url( lopplink )

def grab_epg():
    req = urllib2.Request(andmelink)
    req.add_header(sync_data("VXNlci1BZ2VudA==") , vod_channels("S29kaSBwbHVnaW4gYnkgTWlra00="))
    response = urllib2.urlopen(req)
    link=response.read()
    jdata = json.loads(link.decode('utf8'))
    response.close()
    if jdata:
       plugintools.log(pnimi+sync_data("amRhdGEgbG9hZGVkIC0gQmVuIEVwaWMgV2lucyE="))
       return jdata
def kontroll():
    randomstring = grab_epg()
    kasutajainfo = randomstring[sync_data("dXNlcl9pbmZv")]
    kontroll = kasutajainfo[get_live("YXV0aA==")]
    return kontroll
def get_live(channel):
    video = base64.b64decode(channel)
    return video
def execute_ainfo(params):
    plugintools.log(pnimi+get_live("TXkgYWNjb3VudCBNZW51IA==")+repr(params))
    andmed = grab_epg()
    kasutajaAndmed = andmed[sync_data("dXNlcl9pbmZv")]
    seis = kasutajaAndmed[get_live("c3RhdHVz")]
    aegub = kasutajaAndmed[sync_data("ZXhwX2RhdGU=")]
    if aegub:
       aegub = datetime.datetime.fromtimestamp(int(aegub)).strftime('%d/%m/%Y %H:%M')
    else:
       aegub = vod_channels("TmV2ZXI=")
    leavemealone = kasutajaAndmed[get_live("bWF4X2Nvbm5lY3Rpb25z")]
    activecons = kasutajaAndmed[get_live("YWN0aXZlX2NvbnM=")]
    polarbears = kasutajaAndmed[sync_data("dXNlcm5hbWU=")]
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdVXNlcjogWy9DT0xPUl0=")+polarbears , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdU3RhdHVzOiBbL0NPTE9SXQ==")+seis , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=get_live("W0NPTE9SID0gd2hpdGVdRXhwaXJlczogWy9DT0xPUl0=")+aegub , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=vod_channels("W0NPTE9SID0gd2hpdGVdTWF4IGNvbm5lY3Rpb25zOiBbL0NPTE9SXQ==")+leavemealone , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=vod_channels("W0NPTE9SID0gd2hpdGVdQWN0aXZlIGNvbm5lY3Rpb25zOiBbL0NPTE9SXQ==")+activecons , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
	
    plugintools.set_view( plugintools.LIST )
def vanema_lukk(name):
        plugintools.log(pnimi+sync_data("UGFyZW50YWwgbG9jayA="))
        a = 'XXX', 'Adult', 'Adults','ADULT','ADULTS','adult','adults','Porn','PORN','porn','Porn','xxx'
        if any(s in name for s in a):
           xbmc.executebuiltin((u'XBMC.Notification("Parental Lock", "Channels may contain adult content", 2000)'))
           text = plugintools.keyboard_input(default_text="", title=get_live("UGFyZW50YWwgbG9jaw=="))
           if text==plugintools.get_setting(sync_data("dmFuZW1ha29vZA==")):
              return
           else:
              exit()
        else:
           name = ""
def check_user():
    plugintools.message(get_live("RVJST1I="),vod_channels("VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"))
    sys.exit()
def load_channels():
    statinfo = os.stat(LOAD_LIVE+"/"+get_live("YmFja2dyb3VuZC5wbmc="))

def vod_channels(channel):
    video = base64.b64decode(channel)
    return video

run()