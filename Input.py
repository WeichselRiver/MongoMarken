# Input a stamp
# required info: Gebiet + MichNr
# Auswahl: Gebiet
Gebiete = ["DDR", "Berlin (West)"]
Satz = {"DDR" : {"MnStart" : 261,
"MnEnde" : 270}}

for i in range(len(Gebiete)):
    print(i, Gebiete[i])
print("")
gebiet = int(input("Select Gebiet: "))
print(f"Auswahl {Gebiete[gebiet]}")

# Input MichNr
# Test ob vorhanden
print(Satz[Gebiete[gebiet]])
