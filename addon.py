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
    self.strActionInfo = xbmcgui.ControlLabel(100, 200, 200, 200, '', 'font13', '0xFFFFFFFF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Your IP adress is : ' + myinfos2)
    myinfos3 = xbmc.getDVDState()
    self.strActionInfo = xbmcgui.ControlLabel(100, 250, 200, 200, '', 'font13', '0xFFFFFFFF')
    self.addControl(self.strActionInfo)
    dvdstate = ''
    if (myinfos3 == 1):
      dvdstate = 'DRIVE_NOT_READY'
    if (myinfos3 == 16):
      dvdstate = 'TRAY_OPEN'
    if (myinfos3 == 64):
      dvdstate = 'TRAY_CLOSED_NO_MEDIA'
    if (myinfos3 == 96):
      dvdstate = 'TRAY_CLOSED_MEDIA_PRESENT'            
    self.strActionInfo.setLabel('dvd state : ' + dvdstate )
    myinfos4 = xbmc.getFreeMem()
    self.strActionInfo = xbmcgui.ControlLabel(100, 300, 200, 200, '', 'font13', '0xFFFFFFFF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('free mem : ' + str(myinfos4) + ' Mb')
    myinfos5 = xbmc.getCpuTemp()
    self.strActionInfo = xbmcgui.ControlLabel(100, 350, 200, 200, '', 'font13', '0xFFFFFFFF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('cpu temp : ' + str(myinfos5) )

mydisplay = MyClass()
mydisplay.localinfos()
mydisplay .doModal()
del mydisplay
