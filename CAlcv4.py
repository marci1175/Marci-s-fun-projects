import math
import os
file1 = open(f"pymateelozmenyAUHSAD.txt", "r+")
realy = file1.read()
file1.close()
file1 = open(f"pymateelozmenyAUHSAD.txt","r+")
print("Welcome to marci's calculator Version 3!\n")
szam = int(input("Please enter the first number you'd like to use!\n"))
os.system('cls')
print(f"Your first number is : {math.ceil(szam)}")
szam1 = int(input("Please enter the second number you'd like to use!\n"))
os.system('cls')
print(f"Your first number is : {math.ceil(szam)}")
print(f"Your second number is : {math.ceil(szam1)}")
while True:
    try:
        val1 = int(input("Which calculation do you choose?\n 1) +\n 2) -\n 3) *\n 4) :\n 5) n!\n\n\n\n If you pick n! calculations, it is only going to use the first number.\n"))
        if val1 in (1, 2 ,3, 4, 5):
                break
        else:print("Please enter a number between 1 and 5!")
        raise ValueError
    except ValueError:
        print("Please enter a number between 1 and 5!")
if val1 == 1:
    megoldas = szam + szam1
    file1.write(f"{realy}\n {megoldas} = {szam} + {szam1}")
elif val1 == 2:
    megoldas = szam - szam1
    file1.write(f"{realy}\n {megoldas} = {szam} - {szam1}")
elif val1 == 3:
    megoldas = szam * szam1
    file1.write(f"{realy}\n {megoldas} = {szam} * {szam1}")
elif val1 == 4:
    megoldas = szam / szam1
    file1.write(f"{realy}\n {megoldas} = {szam} / {szam1}")
elif val1 == 5:
    dont80 = int(input("Modify your current number\n"))
    if dont80 >= 0:
        megoldas = math.factorial(szam)
        file1.write(f"{realy}\n {szam}! = {megoldas}")
    elif dont80 <= 0:
        print("You cannot enter a negative number to calculate factorial with.\n")
        dont100 = input("Do you still want the negative result?\n1) Y\n2) N (Exit)\n")
        if dont100 == "1":
            print(f"Answer: -{math.ceil(math.factorial(abs(szam)))}")
            megoldas = math.factorial(szam)
            file1.write(f"{realy}\n {szam}! = -{megoldas}")
            var = input("")
            exit()
        else:exit()



print(f"Answer: {math.ceil(megoldas)}")
end = input(" ")