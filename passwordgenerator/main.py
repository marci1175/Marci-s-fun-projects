import tkinter as tk
import string
import secrets
import time
import sys
import os
import time
#FILE CREATION---------------------------------------
try: file1 = open(f"passwords.txt", "r+")
except FileNotFoundError:
    file1 = open(f"passwords.txt", "w")
    file1.close()
    file1 = open(f"passwords.txt", "r+")
#FILE CREATION END-----------------------------------
#IMPORTS ----------------------------------------
m = tk.Tk()
rese = tk.StringVar()
rese.set("All generated passwords will appear here, until regeneration.")
#defs--------------------------------------------
def gett():
    global numberg
    numberg = e1.get()
    try:
        intnum = int(numberg)
        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(intnum))
        rese.set(res)
        ido = time.ctime()
        file1.write(f"{ido} : {res}\n")
        print(res)
    except ValueError:
        m.destroy()
        print("Only numbers! :)\nRestarting in four seconds!")
        time.sleep(4)
        os.startfile(sys.argv[0])
        sys.exit()
#definitions END-------------------------------------
m.geometry('500x500')
m.title("Password Generator!")
#TKINTER CONFIG ---------------------------------
tk.Label(m, text="Welcome to marci's password generator").pack()
tk.Label(m, text="ALL PASSWORD(S) GENERATED ARE LOGGED TO A FILE NAMED: passwords.txt",fg="Red").pack()
ptext = tk.Label(m, textvariable=rese,bg="Black",fg="White",pady=55)
ptext.pack()
tk.Label(m, text="Enter the amount of characters you would like in your password!",pady=30).pack()
e1 = tk.Entry(m,width=50)
e1.pack()
tk.Button(m, text="Generate!",command=gett).pack(side="bottom",pady=50)


#END----------------------------------------------
m.mainloop()
