import os
import math
import sys
print("Welcome to marci's database!")
dontes30 = input("What do you want to do with your database?\n1) Create/Overwrite\n2) Open\n3) Modify\n4) Delete\n")
if dontes30 == "1":
    nevk = input("Please enter your file's name:\n")
    file1 = open(f"{nevk}.txt", "w")
    dontes60 = input("Do you want to do anyting with this file?\n1) Y\n2) N\n")
    if dontes60 == "2":
        exit()
    elif dontes60 == "1":
        os.startfile(sys.argv[0])
        sys.exit()
elif dontes30 == "2":
    fasz = input("Please enter your file's name, without file extension (ex : .txt)\n")
    file1 = open(f"{fasz}.txt", "r")
    olv = file1.read()
    print(olv)
    dontes60 = input("Do you want to do anyting with this file?\n1) Y\n2) N\n")
    if dontes60 == "2":
        exit()
    elif dontes60 == "1":
        os.startfile(sys.argv[0])
        sys.exit()
elif dontes30 == "3":
    fasz = input("Please enter your file's name, without file extension (ex : .txt)\n")
    file1 = open(f"{fasz}.txt", "r+")
    olv = file1.read()
    print(f"You can enter text now.\n")
    modi = input(f"{olv}---> ")

    file1.write(f"{', '+ modi}")
elif dontes30 == "4":
    dontes120 = input("Which file do you want to remove?\nExtension/Full name required! (Marci.txt)\n")
    os.remove(dontes120)
else:mindegy = input("Please select a number between 1 - 4!")
os.startfile(sys.argv[0])
sys.exit()
