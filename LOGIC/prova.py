from Xel import *

radius=10
org= Exa()
origin=Xel.newHex(radius)
origin
while origin.link["a"]!= None:
    origin=origin.link["a"] 

result=""

def menu(org):
    a=input()
    if a=="q":
        org=org.A()
    if a=="w":
        org=org.Q()
    if a=="a":
        org=org.S()
    if a=="s":
        org=org.W()
    if a=="z":
        org=org.D()
    if a=="x":
        org=org.E()
    if a=="exit":
        quit()
    return org

while True :
    print("""istruzioni:
    ci si muove con q,w,a,s,z,x, purtroppo essendo l'esagono piegato di novanta gradi ho dovuto improvvisare,
    si esce scrivendo 'exit' senza apostrofi, buon divertimento""")
    realorg=origin
    result=""
    for i in range(-radius, radius+1):
        temporg = realorg
        for j in range(abs(i)):
            result += " "

        if org.e > radius or org.x > radius or org.a > radius :
            print("\nout of range\n")
            break

        while temporg != None:
            if temporg.exa == org :
                result += "o "

            else:
                result += ". "

            temporg=temporg.link["w"]
        result += "\n"
        if i<0:
            realorg=realorg.link["d"]
        else:
            realorg=realorg.link["e"]
        #print("temporg=",temporg,"\nrealorg=",realorg,"\n\n")
    print(result)
    print("position:",org)
    org=menu(org)



