from BeautifulSoup import BeautifulSoup
import xbmc, xbmcgui
import urllib2

#get actioncodes from https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h
ACTION_PREVIOUS_MENU = 10

class MyClass(xbmcgui.Window):
  def __init__(self):
    self.strActionInfo = xbmcgui.ControlLabel(100, 60, 200, 200, '', 'font14', '0xFFBBBBFF')
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
      self.strActionInfo = xbmcgui.ControlLabel(100, vrsta, 500, 500, '', 'font24', '0xFFFFFF11')
      self.addControl(self.strActionInfo)
      self.strActionInfo.setLabel(links1[0].text)
      self.strActionInfo = xbmcgui.ControlLabel(500, vrsta, 500, 500, '', 'font24', '0xFFFF11FF')
      self.addControl(self.strActionInfo)
      self.strActionInfo.setLabel(links1[1].text)
      vrsta = vrsta + 30

mydisplay = MyClass()
mydisplay.localinfos()
mydisplay .doModal()
del mydisplay