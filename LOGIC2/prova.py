from Xel import *

radius=5
org= Exa()
rorg= Xel()
rorg.newHex(radius)
while rorg.link["a"]!= None:
    rorg=rorg.link["a"]

result=""

def menu(org):
    a=input()
    if a=="q":
        org=org.Q()
    if a=="w":
        org=org.W()
    if a=="e":
        org=org.E()
    if a=="d":
        org=org.D()
    if a=="s":
         org=org.S()
    if a=="a":
        org=org.A()
    return org

while True :
    result=""
    temorg = rorg
    for i in range(-radius, radius+1):
        for j in range(abs(i)):
            result += " "
        while temorg.link["w"]!= None:
            if temorg.exa == org :
                result += "o "
            else:
                result += ". "
            temorg=temorg.link["w"]
        result += "\n"
        if i<0:

    print(result)
    org=menu(org)



