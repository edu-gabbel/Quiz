import random as rand
namn=input("Vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")
slumptal=rand.randint(1,10)
gissning=int(input("Gissa ett tal mellan 1 och 10 "))
if gissning==slumptal:
    print("Rätt!")
else:
    print(f"Tyvärr, det var {slumptal}")
