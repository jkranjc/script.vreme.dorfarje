import xbmc, xbmcgui

#get actioncodes from https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h
ACTION_PREVIOUS_MENU = 10

class MyClass(xbmcgui.Window):
  def __init__(self):
    self.strActionInfo = xbmcgui.ControlLabel(250, 60, 200, 200, '', 'font14', '0xFFBBBBFF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Push BACK to quit')

  def onAction(self, action):
    if action == ACTION_PREVIOUS_MENU:
      self.close()

  def localinfos(self):
    myinfos1 = xbmc.getLanguage()
    self.strActionInfo = xbmcgui.ControlLabel(100, 150, 200, 200, '', 'font13', '0xFFFFFFFF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Your language is : ' + myinfos1)
    myinfos2 = xbmc.getIPAddress()
    self.strActionInfo = xbmcgui.ControlLabel(100, 200, 300, 200, '', 'font16', '0xFFFF2211')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Your IP adress je : ' + myinfos2)

mydisplay = MyClass()
mydisplay.localinfos()
mydisplay .doModal()
del mydisplay
