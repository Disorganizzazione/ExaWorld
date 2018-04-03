from Xel import *

radius=5
ra=6
org=[0,1]
org[0]= Exa()
org[1]= Xel()

org[1].newHex(radius)

result=""

def menu(org):
    print("origine" + str(org[1].exa))
    print("posizione" + str(org[0]))
    a=input()
    if a=="q":
        org[0]=org[0].Q()
        org[1]=org[1].link[a]
    if a=="w":
        org[0]=org[0].W()
        org[1]=org[1].link[a]
    if a=="e":
        org[0]=org[0].E()
        org[1]=org[1].link[a]
    if a=="d":
        org[0]=org[0].D()
        org[1]=org[1].link[a]
    if a=="s":
         org[0]=org[0].S()
         org[1]=org[1].link[a]
    if a=="a":
        org[0]=org[0].A()
        org[1]=org[1].link[a]
    return [org[0], org[1]]

while True :
    a=ra
    result=""
    for i in range(-radius, radius+1):
        for j in range(abs(i)):
            result += " "
        for j in range(a):
            if org[1].exa == org[0] :
                result += "o "
            else:
                result += ". "
        if i < 0:
            a += 1
        else:
            a -= 1
        result += "\n"
    print(result)
    org=menu(org)



