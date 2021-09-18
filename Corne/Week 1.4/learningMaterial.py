# De variables om mee te testen
number = 1
boolean = True

# Bij deze if statement moet de variable number gelijk zijn (de dubbele == kijkt of beide waardes exact hetzelfde zijn) met waarde 1.
if number == 1:
    print("Number is gelijk aan één!")

# De statement kijkt of de variable number hetzelfde is als 2
if number == 2:
    print("Number is gelijk aan twee!")
# De else wordt alleen uitgevoerd als bovenstaande statement(s) niet waar zijn. Zoals je ziet heeft het ook geen statement waardoor deze altijd waar is als de rest niet klopt.
else:
    print("De waarde van number is niet gelijk aan twee")

if number == 7:
    print("Number is gelijk aan zeven!")
# De elif wordt alleen uitgevoerd als de bovenstaande statement(s) niet waar zijn. Bij een else if heb je wel een statement om te kijken of een statement klopt in tegendeel bij een else.
# LET OP: Bij de meeste programmeertalen is het else if, maar bij python is het elif!!!
elif number == 1:
    print("Number is gelijk aan één!")
else:
    print("Number is niet gelijk aan zeven of één")

# BEIDE statements moeten waar zijn om de print uit te laten voeren anders gaat hij door naar de else if
if number == 1 and number == 9:
    print("De variable number is 1 EN 9")
# Één van de statements moet waar zijn om de print uit te voeren anders gaat hij door naar de else
elif number == 1 or number == 9:
    print("De variable number is 1 OF 9")
else:
    print("de variable number is geen 1 en 9")

# De not keyword zorgt ervoor dat een statement waar is als hij niet waar is en andersom
if not number == 2: # Dit is waar
    print("De variable number heeft niet de waarde 2")
else:
    print("De variable heeft een andere waarde")

# De > (Groter dan) teken kijkt of een waarde groter is dan de opgegeven waarde
if number > 1:
    print("De variable number is groter dan 1")
# De >= (Groter of gelijk aan) teken kijkt of de waarde of GELIJK is aan de opgegeven waarde
elif number >= 1:
    print("De variable number is groter of GELIJK aan 1")

# De < (Kleiner dan) teken kijkt of een waarde kleiner is dan de opgegeven waarde
if number < 1:
    print("De variable number is kleiner dan 1")
# De <= (Kleiner of gelijk aan) teken kijkt of een waarde kleiner of GELIJK is aan de opgegeven waarde
elif number <= 1:
    print("De variable number is kleiner of GELIJK aan 1")

# De waarde van de variable boolean is true (waar) daarom hoef je dus geen boolean == True te doen
if boolean:
    print("De waarde van boolean is waar (True)")
elif not boolean:
    print("De waarde van boolean is niet waar (False)")

# Dit is een nested statement. Het zijn meerdere statements in lagen verdeeld.
# LET OP: pas op dat je niet te veel lagen maakt dit kan namelijk voor verwarring zorgen
if number == 1:
    if boolean:
        print("Boolean en number zijn beide waar!")
    else:
        print("Alleen de eerste statement is waar")
else:
    print("De waarde van variable number is niet 1")