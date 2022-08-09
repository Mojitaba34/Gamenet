import math
from tkinter import *
from datetime import datetime
import datetime as dt
from tkinter.ttk import Labelframe
from tkinter import ttk





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

def clear(data):
    TextBoxList[data].delete(1.0,END)

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)


# Add A Scrollbar
my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e :my_canvas.configure(scrollregion=my_canvas.bbox('all')))
# Add MouseWheel Even to the Root to scroll with Mouse Togel
root.bind_all('<MouseWheel>',lambda e : my_canvas.yview_scroll(-1*int((e.delta/120)),"units"))

# Crreate ANOTHER frame in Canvas
second_frame = Frame(my_canvas)

# Addd that new frame to window in the Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

data = 5
frameList = [] # Creating Frame
j = 0
k = 0
for i in range(1,data + 1):
    Sit1 = Labelframe(second_frame,text=f"دستگاه شماره {i}")
    Sit1.grid(row=k,column=j, padx= 10)
    frameList.append(Sit1)
    j += 1
    if j == 3:
        j = 0
        k += 1
    if k == 3:
        k =0

StartTimeLables = []

for i in range(1,data + 1):
    StartTimeLables.append('lbl'+ str(i))

global objectLablelsForStopTime # List of Label Objects
objectLablelsForStopTime = []

global objlbllist # List of Label Objects
objlbllist = []

global TotalPlayedTime # List of Label Objects
TotalPlayedTime = []

global PriceInput
PriceInput = []

global TextboxList
TextBoxList = []

i = 0
for framename, lblnames in zip(frameList, StartTimeLables):
    myButton = Button(framename, text="Start", padx=50 , pady=10, command=lambda mydata = i: InsertTime(mydata)).grid(row=0, column=0)
    mybutton = Button(framename, text="Stop", padx=50, pady=10, command= lambda mydata = i:InsertStopTime(mydata) ).grid(row=0, column=1)
    mybutt = Button(framename,text="Calc", padx=50,pady=10, command=lambda mydata = i:CalcPrice(mydata)).grid(row=0,column=2)
    

    global temp
    temp = lblnames
    temp = Label(framename, text="")
    temp.grid(row=1,column=1)
    objlbllist.append(temp)

    global temp2
    temp2 = lblnames
    temp2 = Label(framename, text="")
    temp2.grid(row=2, column=1)
    objectLablelsForStopTime.append(temp2)

    global PlayedTimeLabel
    PlayedTimeLabel = lblnames
    PlayedTimeLabel = Label(framename,text="")
    PlayedTimeLabel.grid(row=3,column=1)
    TotalPlayedTime.append(PlayedTimeLabel)

    e = Entry(framename ,width=15)
    e.grid(row=4,column=1, pady= 10)
    PriceInput.append(e)


    lable_title = Label(framename, text="زمان شروع بازی").grid(row=1,column=0)
    lable_title = Label(framename, text="زمان اتمام بازی").grid(row=2,column=0)
    lable_title = Label(framename, text="کل زمان بازی شده").grid(row=3,column=0)
    lable_title = Label(framename, text='قیمت').grid(row=4,column=0)

    TextBox = Text(framename, width=30,height=15,font=('Helvetica', 10))
    TextBox.grid(row=5, column=0, columnspan=5)
    TextBoxList.append(TextBox)
    clear_button = Button(framename, text="CLEAR BOX", command= lambda mydata = i:clear(mydata))
    clear_button.grid(row=6,column=1,pady=10)
    i += 1




root.mainloop()
