import json
def loadSave():
    save = json.load(open('data.json'))
    return (save['hour'],save['minute'],save['second'],save['path'])
def pushSave(s):
    save = json.load(open('data.json'))
    save['hour']=s[0]
    save['minute']=s[1]
    save['second']=s[2]
    save['path']=s[3]
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(save, f, ensure_ascii=False, indent=4)
