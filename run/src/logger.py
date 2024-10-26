import os
from datetime import datetime

class logger:
    path=''
    @staticmethod
    def log(s):
        if logger.path=='':
            CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
            logger.path=os.path.join(CURRENT_DIRECTORY, "res/log.txt")
            file=open(logger.path,"w")
            file.close()
        currentTime=datetime.now().strftime("%Y/%m/%d-%H:%M:%S - ")
        file=open(logger.path,"a")
        file.write(currentTime + s+'\n')
        file.close()