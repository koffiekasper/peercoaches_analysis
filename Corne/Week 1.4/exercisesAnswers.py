# Opdracht 1 (Stoplicht)
currentColor = "Groen"
if currentColor == "Groen":
    print("Je kan doorrijden")
elif currentColor == "Oranje":
    print("Je kan doorrijden als je niet kan stoppen")
elif currentColor == "Rood":
    print("STOPPEN!")
else:
    print("Deze stoplicht is defect, rij maar door")

# Opdracht 2 (FizzBuzz)
nummer = 70
if nummer == 100:
    print("FizzBuzz")
elif nummer <= 10:
    print("Fizz")
elif nummer > 10:
    print("Buzz")

# Opdracht 3 (Binary converter)
decimaalNummer = 3
if decimaalNummer == 1:
    print("1")
elif decimaalNummer == 2:
    print("10")
elif decimaalNummer == 3:
    print("11")
elif decimaalNummer == 4:
    print("100")
elif decimaalNummer == 5:
    print("101")
else:
    print("Dit is geen geldig getal!")