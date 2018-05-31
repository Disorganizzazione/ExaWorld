from Xel import *
radius=3 #radius maps 
position=None #position in l_map
l_map=None #local map
adj_maps={'qw':None,'we':None, 'ed':None,'ds':None,'sa':None,'aq':None} #map stored in memory

def init():
    #global initializations
    global l_map
    global position
    global adj_maps
    #instatntiate
    l_map= Xel.newHex(radius)
    position= Exa()
    for i in adj_maps:
        adj_maps[i]=Xel.newHex(radius)
    
def menu(a): #a=input direction
    global position
    if a=="q":
        position=position.Q()
    elif a=="w":
        position=position.W()
    elif a=="e":
        position=position.E()
    elif a=="d":
        position=position.D()
    elif a=="s":
        position=position.S()
    elif a=="a":
        position=position.A()
    elif a=="exit":
        quit()



#Main execution
init()
print(position)
while 1:
    a=input()
    menu(a)
    print("--------------------------------------------------------------------------------")
    print(position)
