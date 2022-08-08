from cgitb import text
import math
from tkinter import *
from datetime import datetime
import datetime as dt
from tkinter.ttk import Labelframe

root = Tk()
root.title('DARK') # Windows Title
root.geometry("600x700")# Windows Size


def GetCurrentTime(): # Get Currrent Time From System
    now = datetime.now()
    Time = f'{now.hour}:{now.minute}:{now.second}'
    return Time

def setTime(Time, lbl): # set Time in Specific label
    lbl.config(text=str(Time))



def InsertTime(lbl): # in here we Specific the label to inser the Start Time Data
    Time = GetCurrentTime()
    setTime(Time, objlbllist[int(lbl)])
    
def InsertStopTime(lbl): # here we Specific  the lable to Insert the Stop Time data
    Time = GetCurrentTime()
    setTime(Time,objectLablelsForStopTime[int(lbl)])
    plytime = PlayedTime(objlbllist[int(lbl)],objectLablelsForStopTime[int(lbl)])
    totalLabel = TotalPlayedTime[int(lbl)]
    totalLabel.config(text=str(plytime))


def PlayedTime(lblstart,lblstop): # calculationg the Total Time that player Played
    start = str(lblstart.cget('text'))
    stop = str(lblstop.cget('text'))
    StartHour,StartMinute,StartSecond = start.split(':')
    StopHour, StopMinute,StopSecond = stop.split(':')
    TotalStartAsSecond = (int(StartHour) * 3600) + (int(StartMinute) * 60) + (int(StartSecond))
    TotalStopAsSecond = (int(StopHour) * 3600) + (int(StopMinute) * 60) + (int(StopSecond))
    return str(dt.timedelta(seconds=(TotalStopAsSecond - TotalStartAsSecond)))
    

def CalcPrice(ButtonNum): # Calculatin Total Price 
    price = PriceInput[ButtonNum].get()
    Time = TotalPlayedTime[ButtonNum].cget('text')
    h,m,s = Time.split(':')
    time = (int(h) * 3600) + (int(m) * 60) + (int(s))
    print((math.ceil(time/60)*int(price))/60)


frameList = [] # Creating Frame
for i in range(0,8):
    Sit1 = Labelframe(root,text=f"دستگاه شماره {i}")
    Sit1.grid(row=i,column=0)
    frameList.append(Sit1)


StartTimeLables = ['lbl1', 'lbl2', 'lbl3']

global objectLablelsForStopTime # List of Label Objects
objectLablelsForStopTime = []

global objlbllist # List of Label Objects
objlbllist = []

global TotalPlayedTime # List of Label Objects
TotalPlayedTime = []

global PriceInput
PriceInput = []
i = 0
for framename, lblnames in zip(frameList, StartTimeLables):
    myButton = Button(framename, text="Start", padx=50 , pady=10, command=lambda mydata = i: InsertTime(mydata)).grid(row=0, column=0)
    mybutton = Button(framename, text="Stop", padx=50, pady=10, command= lambda mydata = i:InsertStopTime(mydata) ).grid(row=0, column=1)
    mybutt = Button(framename,text="Calc", padx=50,pady=10, command=lambda mydata = i:CalcPrice(mydata)).grid(row=0,column=2)
    i = i + 1

    global temp
    temp = lblnames
    temp = Label(framename, text=f"Hi {temp}")
    temp.grid(row=1,column=1)
    objlbllist.append(temp)

    global temp2
    temp2 = lblnames
    temp2 = Label(framename, text=f"hi {temp2}")
    temp2.grid(row=2, column=1)
    objectLablelsForStopTime.append(temp2)

    global PlayedTimeLabel
    PlayedTimeLabel = lblnames
    PlayedTimeLabel = Label(framename,text=f"{PlayedTimeLabel}")
    PlayedTimeLabel.grid(row=3,column=1)
    TotalPlayedTime.append(PlayedTimeLabel)

    e = Entry(framename ,width=15)
    e.grid(row=4,column=1)
    PriceInput.append(e)


    lable_title = Label(framename, text="زمان شروع بازی").grid(row=1,column=0)
    lable_title = Label(framename, text="زمان اتمام بازی").grid(row=2,column=0)
    lable_title = Label(framename, text="کل زمان بازی شده").grid(row=3,column=0)
    lable_title = Label(framename, text='قیمت').grid(row=4,column=0)




root.mainloop()
