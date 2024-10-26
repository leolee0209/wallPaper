import json
from logger import logger as l
import os

class s:
    dataPath=''
    @staticmethod
    def loadSave():
        l.log('loading saved data')
        if s.dataPath=='':
            CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
            s.dataPath=os.path.join(CURRENT_DIRECTORY, "res/data.json")
        try:
            save = json.load(open(s.dataPath,"r"))
        except Exception as e:
            save=dict()
            save['hour']=0
            save['minute']=30
            save['second']=0
            save['path']=''
            with open(s.dataPath, 'w', encoding='utf-8') as f:
                json.dump(save, f, ensure_ascii=False, indent=4)
        return (save['hour'],save['minute'],save['second'],save['path'])
    @staticmethod
    def pushSave(o):
        l.log('saving changes')
        save = json.load(open(s.dataPath))
        save['hour']=o[0]
        save['minute']=o[1]
        save['second']=o[2]
        save['path']=o[3]
        with open(s.dataPath, 'w', encoding='utf-8') as f:
            json.dump(save, f, ensure_ascii=False, indent=4)
