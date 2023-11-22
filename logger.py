import sys
from datetime import datetime

class Logger:
    def __init__(self, filename = ""):
        if (filename != ""):
            self.logfile = open(filename, "a")

    def out(self, message):
        datetimeStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        if (sys.argv.__contains__("-log")):
            print(f"[{datetimeStr}]: {message}")
        if (self.logfile):
            self.logfile.write(f"[{datetimeStr}]: {message}\n")
        
logger = Logger("logs.txt")
