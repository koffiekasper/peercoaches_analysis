# While loops

# basis while loop
# De index variable slaat op in welke ronde je zit
index = 0

while index < 11: # Dit is een statement en zolang deze statement waar is zal hij de code in de while loop blijven herhalen
    # Dit is de "body" van de while loop. Hierin staat jouw code die je wilt laten uitvoeren
    print("We zitten nu op ronde ", i)
    # Deze line zorgt ervoor dat de index geupdatet wordt en dat de statement uiteindelijk niet meer waar is
    # LET OP: Als je deze line niet hebt krijg je een oneindige loop
    index += 1

# while loop met gebruikers input
aantalRondes = int(input("Hoeveel rondes moeten er gedaan worden? "))
naam = input("Wat is uw naam?")

start = 1

while start <= aantalRondes:
    print("Beste", naam, "je zit nu op ronde", start)
    start += 1

# While loop met een else statement
i = 0
while i < 10:
    print(i)
else: # De else wordt aangeroepen zodra de statement van de while loop niet langer meer waar (True) is
    print("De while loop is afgelopen!")

# oneindige while loop
while True: # Dit is een oneindige while loop omdat de statement altijd waar (True) is
    print("Ik zal niet stoppen zolang jij mij niet stopt")
    print("Stop mij met Ctrl + C!")