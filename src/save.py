import json
import os
def loadSave():
    CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    dataPath=os.path.join(CURRENT_DIRECTORY, "res/data.json")
    save = json.load(open(dataPath))
    return (save['hour'],save['minute'],save['second'],save['path'])
def pushSave(s):
    CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    dataPath=os.path.join(CURRENT_DIRECTORY, "res/data.json")
    save = json.load(open(dataPath))
    save['hour']=s[0]
    save['minute']=s[1]
    save['second']=s[2]
    save['path']=s[3]
    with open(dataPath, 'w', encoding='utf-8') as f:
        json.dump(save, f, ensure_ascii=False, indent=4)
