from cgitb import text
import math
from tkinter import *
from datetime import datetime
import datetime as dt
from tkinter.ttk import Labelframe
from tkinter import ttk, messagebox





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
    objectLablelsForStopTime[lbl].config(text='')
    TotalPlayedTime[lbl].config(text='')
    
def InsertStopTime(lbl): # here we Specific  the lable to Insert the Stop Time data
    Time = GetCurrentTime()
    LableLenStopTime = len(objlbllist[int(lbl)].cget('text'))
    if int(LableLenStopTime) == 0:
        messagebox.showwarning('Hi','Set start and Stop Time First')
    else:
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
    if price.isnumeric():
        if len(price) <= 1:
            messagebox.showwarning('Hi', 'Enter Price First')
        else:
                if len(TotalPlayedTime[ButtonNum].cget('text')) < 1:
                    messagebox.showwarning('Hi','Click Start First')
                    PriceInput[ButtonNum].delete(0,END)
                else:
                    Time = TotalPlayedTime[ButtonNum].cget('text')
                    h,m,s = Time.split(':')
                    time = (int(h) * 3600) + (int(m) * 60) + (int(s))
                    #print((math.ceil(time/60)*int(price))/60)
    else:
        messagebox.showwarning('Hi', 'Enter integer value')
        PriceInput[ButtonNum].delete(0,END)




def clear(data):
    if len(TextBoxList[data].get(1.0, END)) <= 1:
        messagebox.showwarning('Hi', 'The Box Is Already Empty!!!')
    else:
        TextBoxList[data].delete(1.0,END)

def Reset(ButtonNumber):
    objlbllist[ButtonNumber].config(text='')
    objectLablelsForStopTime[ButtonNumber].config(text='')
    TotalPlayedTime[ButtonNumber].config(text='')
    PriceInput[ButtonNumber].delete(0,END)
    TextBoxList[ButtonNumber].delete(1.0,END)

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
    StartButton = Button(framename, text="Start", padx=30 , pady=10, command=lambda mydata = i: InsertTime(mydata)).grid(row=0, column=0)
    StopButton = Button(framename, text="Stop", padx=30, pady=10, command= lambda mydata = i:InsertStopTime(mydata) ).grid(row=0, column=1)
    CalcButoon = Button(framename,text="Calc", padx=30,pady=10, command=lambda mydata = i:CalcPrice(mydata)).grid(row=0,column=2)
    ResetButton = Button(framename,text='Reset',padx=30,pady=10,command=lambda mydata = i:Reset(mydata)).grid(row=0,column=3)
    

    global temp #temp for Defind Label 
    temp = lblnames
    temp = Label(framename, text="")
    temp.grid(row=1,column=1)
    objlbllist.append(temp)

    global temp2 # temp2 for Defind Label
    temp2 = lblnames
    temp2 = Label(framename, text="")
    temp2.grid(row=2, column=1)
    objectLablelsForStopTime.append(temp2)

    global PlayedTimeLabel # Defind Label 
    PlayedTimeLabel = lblnames
    PlayedTimeLabel = Label(framename,text="")
    PlayedTimeLabel.grid(row=3,column=1)
    TotalPlayedTime.append(PlayedTimeLabel)

    e = Entry(framename ,width=15) # Entry for Price Value
    e.grid(row=4,column=1, pady= 10)
    PriceInput.append(e)


    lable_title = Label(framename, text="زمان شروع بازی").grid(row=1,column=0)
    lable_title = Label(framename, text="زمان اتمام بازی").grid(row=2,column=0)
    lable_title = Label(framename, text="کل زمان بازی شده").grid(row=3,column=0)
    lable_title = Label(framename, text='قیمت').grid(row=4,column=0)

    TextBox = Text(framename, width=30,height=15,font=('Helvetica', 10))
    TextBox.grid(row=5, column=0, columnspan=6)
    TextBoxList.append(TextBox)
    clear_button = Button(framename, text="CLEAR BOX", command= lambda mydata = i:clear(mydata))
    clear_button.grid(row=6,column=1,pady=10)
    i += 1




root.mainloop()
