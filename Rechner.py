print ("""

============================================================

==                Der mächtige giga rechner               ==

============================================================

""")

oper = input(" was ausrechnen \n U -> d | U -> r \n r -> d | d -> U \n A -> r | A -> d \n Km -> m| m -> Km \n cm->Km | x / y \n x * y  | x + y \n x - y:")

if (oper == "U mit d"):
    num = input("Gib durchmesser: ")
    num = float(num)
    (PI) = 3.1415926535
    print("Ergebnis: \n", round(PI * num, 2))
if (oper == "U mit r"):
    num = input("Gib radius: ")
    num = float(num)
    (PI) = 3.1415926535
    mall2 = 2
    Ergebnis = mall2 * PI * num
    print("Ergebnis: \n", round(Ergebnis, 2))
if (oper == "r mit d"):
    num = input("Gib durchmesser: ")
    num = float(num)
    geteilt2 = 2
    Ergebnis = num / geteilt2
    print("Ergebnis: \n", round(Ergebnis, 2))
if (oper == "d mit U"):
    num = input("Gib Umfang: ")
    num = float(num)
    (PI) = 3.1415926535
    Ergebnis = num / (PI)
    print("Ergebnis: \n", round(Ergebnis, 2))
if (oper == "A mit r"):
    num = input("Gib Umfang: ")
    num = float(num)
    (PI) = 3.1415926535
    Ergebnis = num * num * (PI)
    print("Ergebnis in Quadratzentimeter: \n", round(Ergebnis, 2))
if (oper == "A mit d"): 
    num = input("Gib Umfang: ")
    num = float(num)
    geteilt2 = 2
    (PI) = 3.1415926535
    (gerechnet) = num / geteilt2
    Ergebnis = gerechnet * gerechnet * (PI)
    print("Ergebnis in Quadratzentimeter: \n", round(Ergebnis, 2))
if (oper == "Km mit m"):
    num = input("Gib meter: ")
    num = float(num)
    kilo = 1000
    ErgebrnisKmmm = num / kilo
    print("Ergebnis: \n", round(ErgebrnisKmmm, 4))
if (oper == "m mit Km"):
    num = input("Gib kilometer: ")
    num = float(num)
    kilo = 1000
    ErgebrnismmKm = num / kilo
    print("Ergebnis: \n", round(ErgebrnismmKm, 5))
if (oper == "cm mit Km"):
    num = input("Gib kilometer: ")
    num = float(num)
    ErgebrnismmKm = num / 100000
    print("Ergebnis: \n", round(ErgebrnismmKm, 5))
if (oper == "x + y"):
    num1 = input("gib x:")
    num1 = float(num1)
    num2 = input("gib y:")
    num2 = float(num2)
    Ergebrnisxpluy = num1 + num2
    print("Ergebnis: \n", round(Ergebrnisxpluy, 2))
if (oper == "x - y"):
    num1 = input("gib x:")
    num1 = float(num1)
    num2 = input("gib y:")
    num2 = float(num2)
    Ergebrnisxminy = num1 + num2
    print("Ergebnis: \n", round(Ergebrnisxminy, 2))
if (oper == "x * y"):
    num1 = input("gib x:")
    num1 = float(num1)
    num2 = input("gib y:")
    num2 = float(num2)
    Ergebrnisxmaly = num1 * num2
    print("Ergebnis: \n", round(Ergebrnisxmaly, 2))
if (oper == "x / y"):
    num1 = input("gib x:")
    num1 = float(num1)
    num2 = input("gib y:")
    num2 = float(num2)
    Ergebrnisxgety = num1 / num2
    print("Ergebnis: \n", round(Ergebrnisxgety, 2))