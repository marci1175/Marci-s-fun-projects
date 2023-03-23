import time
import random
cs3 = ['   ¤','§','   ≈ ','•']
cs2 = ['  §      ',' ¤  ','≈ ','•']
cs = ['  ∞','≈ ','• ','     §','   ¤']
cs4 = ['   ≈ ','  • ','∞','  §  ',' ¤  ']
counter = 0
counter1 = 0
epi = input("Epilepsy warning! Press enter to countinue")
epi = input("Epilepsy warning! Press enter again to countinue")
print("Welcome to Marci's space generator!\nSpace begins in 5 seconds.")
time.sleep(5)
while(counter < 9000000):
    while(counter1 < 5000):
        pe = random.choice(cs3)
        pe1 = random.choice(cs2)
        pe3 = random.choice(cs)
        pe2 = random.choice(cs4)
        print(pe,pe2,pe3,pe1,pe,pe2,pe3,pe1,pe,pe2,pe3,pe1,pe,pe2,pe3,pe1,pe,pe2,pe3,pe1,pe,pe2,pe3,pe1)
        continue
