from PyQt6.QtCore import QThread
import subprocess as sps
import time
from queue import Queue
from logger import logger as l

queue = Queue()
gsCmd='/usr/bin/gsettings'

def GetFiles(directory):
    cmd=['ls',directory]
    try:
        fileNames = sps.run(cmd,capture_output=True,text=True).stdout.split('\n')
    except:
        return None
    return fileNames

def GetColorTheme():
    cmd=['/usr/bin/gsettings','get','org.gnome.desktop.interface','color-scheme']
    prefer_dark_theme = sps.run(cmd,capture_output=True,text=True).stdout.strip() == '\'prefer-dark\''
    return prefer_dark_theme

class Worker(QThread):
    changenow=False
    def __init__( self, myApp):
        self.myApp=myApp
        super(Worker, self).__init__()
    def resetFileNames(self):
        self.fileNames=GetFiles(self.myApp.getDirectory())

    def run(self):

        self.fileNames=GetFiles(self.myApp.getDirectory())
        prefer_dark_theme=GetColorTheme()

        pic_uri = 'picture-uri-dark' if (prefer_dark_theme) else 'picture-uri'

        i=0
        #/usr/bin/gsettings set org.gnome.desktop.background picture-uri-dark file:///home/leo/Desktop/wallPaper/1.png
        while True:
            name=self.fileNames[i]
            try:
                cmd=f'{gsCmd} set org.gnome.desktop.background {pic_uri} file://{self.myApp.getDirectory()}/{name}'
                sps.run(cmd,shell=True,check= True,capture_output=True).stdout
                l.log('wallpaper changed to \"'+name+'\"')
            except sps.CalledProcessError as e:
                print()
            timeinter=self.myApp.getTime()
            x=0
            while x< timeinter:
                time.sleep(1)
                x=x+1
                if self.changenow==True:
                    x=0
                    timeinter=self.myApp.getTime()
                    self.changenow=False
            i=i+1
            if i>=len(self.fileNames):
                i=0
