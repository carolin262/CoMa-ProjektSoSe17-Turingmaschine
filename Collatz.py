
"""
Berechnet das Collatz-Problem
indem es zuerst in die Dezimalzahl umrechnet
so oft nur mögl. durch 2 Teilt,
dann (wenn noch nicht ==1) *3+1
bis die 1 erreicht ist.
Dann wird die 1 in Binär umgerechnet und
mit der Anzahl an benoetigten Schritten zurueck gegeben.

"""
number=input("Bitte gebe deine Binaerzahl ein :")
numberDezimal=int(str(number),2)
x=0

while numberDezimal != 1 :
    x+=1

    while numberDezimal%2 == 0:
        numberDezimal=numberDezimal//2
    if numberDezimal == 1:
        break
    numberDezimal=numberDezimal*3+1

print("Nach ", x, " Durchlaeufen ergibt es ",int(bin(numberDezimal)[2:]))
