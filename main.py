import random as rand
namn=input("Vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")
slumptal=rand.randint(1,10)
antal_försök=1
for i in range(1,4):
    gissning=int(input(f"Försök {antal_försök}: Gissa talet: "))
    if gissning==slumptal:
        print("Rätt gissat!")
        break
    else:
        print("Fel gissat.")
        antal_försök+=1
if antal_försök==4:
    print(f"Tyvärr, det var {slumptal}")