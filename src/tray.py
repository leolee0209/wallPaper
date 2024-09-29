from PyQt6.QtGui import *
import os
from PyQt6.QtWidgets import *
import save

class Tray:
    def __init__(self):
        self.save=list(save.loadSave())
    def quit(self):
        save.pushSave(tuple(self.save))
        self.window.app.quit()
    def trayiconclicked(self):
        self.window.show()

    def CreateTray(self,window):
        self.window=window
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        iconPath=os.path.join(CURRENT_DIRECTORY, "res/icon.png")
        icon = QIcon(iconPath)


        self.tray = QSystemTrayIcon(icon=icon,parent=window.app)
        self.tray.setVisible(True)

        menu = QMenu()

        self.tray.activated.connect(self.trayiconclicked)

        # Add the menu to the tray
        self.tray.setContextMenu(menu)
        self.tray.show()
    def hourChange(self,n):
        self.save[0]=n
    def minuteChange(self,n):
        self.save[1]=n
    def secondChange(self,n):
        self.save[2]=n

    