from BeautifulSoup import BeautifulSoup
import xbmc, xbmcgui, xbmcaddon
import urllib2, urllib, os

#get actioncodes from https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h
ACTION_PREVIOUS_MENU = 10

class MyClass(xbmcgui.Window):
  def __init__(self):
    self.strActionInfo = xbmcgui.ControlLabel(50, 50, 200, 200, '', 'font16', '0xFFBBBBFF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('VREME - DORFARJE')
    self.strActionInfo = xbmcgui.ControlLabel(870, 600, 200, 200, '', 'font14', '0xFFBBBBFF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Push BACK to quit')

  def onAction(self, action):
    if action == ACTION_PREVIOUS_MENU:
      self.close()
	  
  def localinfos(self):
    url = 'http://dorfarje.poglej.info/mobile.html'
    data = urllib2.urlopen(url).read()
    soup = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)
    links = soup.findAll('tr')
    vrsta = 100
    for link in links:
      links1 = link.findAll('td')
      self.strActionInfo = xbmcgui.ControlLabel(50, vrsta, 500, 500, '', 'font24', '0xFFFFFF11')
      self.addControl(self.strActionInfo)
      self.strActionInfo.setLabel(links1[0].text)
      self.strActionInfo = xbmcgui.ControlLabel(350, vrsta, 500, 500, '', 'font24', '0xFFFF11FF')
      self.addControl(self.strActionInfo)
      self.strActionInfo.setLabel(links1[1].text)
      vrsta = vrsta + 28
    myFile1 = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'slika1.jpg')
    myFile2 = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'slika2.jpg')
    myFile3 = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'slika3.jpg')
    myFile4 = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'slika4.jpg')
    myFile5 = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'slika5.jpg')
    urllib.urlretrieve("http://www.poglej.info/dorfarje.jpg", myFile1)
    urllib.urlretrieve("http://dorfarje.poglej.info/daytempdew.png", myFile2)
    urllib.urlretrieve("http://dorfarje.poglej.info/daybarometer.png", myFile3)
    urllib.urlretrieve("http://dorfarje.poglej.info/daywind.png", myFile4)
    urllib.urlretrieve("http://dorfarje.poglej.info/daywinddir.png", myFile5)
    self.image = xbmcgui.ControlImage(50, 390, 480, 360, myFile1)
    self.addControl(self.image)
    self.image = xbmcgui.ControlImage(550, 100, 300, 180, myFile2)
    self.addControl(self.image)
    self.image = xbmcgui.ControlImage(870, 100, 300, 180, myFile3)
    self.addControl(self.image)
    self.image = xbmcgui.ControlImage(550, 300, 300, 180, myFile4)
    self.addControl(self.image)
    self.image = xbmcgui.ControlImage(870, 300, 300, 180, myFile5)
    self.addControl(self.image)

mydisplay = MyClass()
mydisplay.localinfos()
mydisplay .doModal()
del mydisplay
