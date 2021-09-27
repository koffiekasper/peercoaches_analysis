# Opdracht 1 (Is het deelbaar door 5)
index = 0
while index <= 50:
    if index % 5 == 0:
        print(index)
    index += 1

# Opdracht 2 (Max Verstappen)
lap = 1
while lap <= 70:
    if lap == 20 or lap == 50:
        print("Max maakt nu een pitstop")
    elif lap == 70:
        print("MAX HEEFT GEWONNEN!")
    else:
        print("Max zit nu in ronde", lap)
    lap += 1

# Opdracht 3 (Optellen van getallen)
maxNumber = int(input("Geef een getal op"))
sumNumber = 0
currentNumber = 0

while currentNumber <= maxNumber:
    sumNumber += currentNumber
    currentNumber += 1
else:
    print("Het getal is", sumNumber)