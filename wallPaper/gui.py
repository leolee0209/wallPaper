import sys
import worker
from PyQt6.QtWidgets import QWidget, QApplication,QFileDialog
from PyQt6 import uic
import save
import tray

class MyApp(QWidget):
    def __init__(self, app):
        super().__init__()
        uic.loadUi('UI.ui',self)
        self.tray=tray.Tray()
        self.app=app
        self.browse.clicked.connect(self.selectFile)
        self.quitB.clicked.connect(self.quit)
        self.minuteBox.setMaximum(59)
        self.minuteBox.setMinimum(0)
        self.minuteBox.setWrapping(True)
        self.secondBox.setMaximum(59)
        self.secondBox.setMinimum(0)
        self.secondBox.setWrapping(True)
        self.hourBox.valueChanged.connect(self.hourChange)
        self.minuteBox.valueChanged.connect(self.minuteChange)
        self.secondBox.valueChanged.connect(self.secondChange)
        self.loadData()
        self.tray.CreateTray(self)
        self.worker = worker.Worker(self)  # Create a Worker instance
        self.worker.start()
        
    def quit(self):
        save.pushSave(tuple(self.tray.save))
        self.tray.quit()
    def closeEvent(self, event):
        save.pushSave(tuple(self.tray.save))
    def getTime(self):
        return self.tray.save[0]*3600+self.tray.save[1]*60+self.tray.save[2]
    def getDirectory(self):
        return self.tray.save[3]
    
    def selectFile(self):
        self.lineEdit.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
        self.tray.save[3]=self.lineEdit.text()
        self.worker.resetFileNames()


    def loadData(self):
        o= save.loadSave()
        self.hourBox.setValue(o[0])
        self.minuteBox.setValue(o[1])
        self.secondBox.setValue(o[2])
        self.lineEdit.setText(o[3])
    
        
    def hourChange(self):
        self.tray.hourChange(self.hourBox.value())
    def minuteChange(self):
        self.tray.minuteChange(self.minuteBox.value())
    def secondChange(self):
        self.tray.secondChange(self.secondBox.value())



def Start():
    app=QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    MyApp(app)

    sys.exit(app.exec())

        




