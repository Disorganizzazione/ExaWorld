from Xel import *
radius=100 #radius maps 
position=None #position in l_map. Must be a Xel! position.exa in order to get coordinates (EXA)
l_map=None #local map
adj_maps={'qw':None,'we':None, 'ed':None,'ds':None,'sa':None,'qa':None} #maps stored in memory
change_dir=None #POSSIBLE directions that will lead to change map

def init():
    #global initializations
    global l_map
    global position
    global adj_maps
    #instatntiate
    l_map= Xel.newHex(radius)
    position= l_map
    for i in adj_maps:
        adj_maps[i]=Xel.newHex(radius)
    
def menu(a): #a=input direction
    global position
    if is_border(a)==False:
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
    

def is_border(a): #check if position has reached the limit of the local map
    global position
    border=0
    if position.exa.e==radius or position.exa.e==-radius:
        border+=1
    if position.exa.x==radius or position.exa.x==-radius:
        border+=1
    if position.exa.a==radius or position.exa.a==-radius:
        border+=1

    global change_dir 
    if border != 0:   #reached the limit of the local map
        change_dir= [k for k,v in position.link.items() if v == None] #POSSIBLE directions that will lead to change map (none Xels)
        print("Possible new maps directions= ", change_dir)
        if border==1: #reached a edge
            print("You're in an edge")
            return change_map(a,2)
        if border==2: #reached an corner
            print("You're in a corner")
            return change_map(a,3)
    return False
        

def change_map(a, n):
    global l_map
    global position
    global change_dir
    global adj_maps
    coords = ['q', 'w', 'e', 'd', 's', 'a']
    direc=None
    if a in change_dir: #the input direction leads to change the map
        print("Direction= ",a)
        direc=change_dir[0]+change_dir[1] #n==2
        if n==3:
            piv=choose_piv() #the direction that can leads 
            if a==piv:
                direc=[k for k in adj_maps.keys() if piv in k and coords[(coords.index(piv)+1)%6] in k].pop() #ex. q (qw)
            else:
                direc= [k for k in adj_maps.keys() if piv in k and a in k].pop() #ex. w or a (qw or qa)
            mirror(a, n, direc)
            print("New Map= ",direc)
            return True
        mirror(a, n, direc)
        print("New Map= ",direc)
        return True
    else:
        return False
    
def mirror(a, n, direc):
    global l_map
    global position
    global change_dir
    global adj_maps
    pos=None #temp new position
    exa= position.exa #exa of the new position (find xel)
    coords = ['q', 'w', 'e', 'd', 's', 'a']
    if direc=='qa':
        direc='aq'
    print("------", direc, change_dir)
    if n==3: #corner
        if a==direc[0]: #-2 (q) 
            exa.a, exa.x = exa.x, exa.a
            exa.a, exa.e = exa.e, exa.a
            pos= l_map.findXel(exa) 
        elif direc[1]==coords[(coords.index(direc[0])+1)%6]: #q+1=(w)
            exa.a, exa.x = exa.x, exa.a
            exa.a, exa.e = exa.e, exa.a
            pos= l_map.findXel(exa).link[coords[(coords.index(direc[0])+2)%6]]  #q+2 - ossia q+e (w)
        else: #+2 (a)
            exa.a, exa.e = exa.e, exa.a
            exa.a, exa.x = exa.x, exa.a
            pos= l_map.findXel(exa) 
    else:  #edge
        max_coord= max(max(abs(exa.e),abs(exa.x)),abs(exa.a))
        if max_coord==abs(exa.e):
            exa.a, exa.x = exa.x, exa.a
        elif max_coord==abs(exa.x):
            exa.a, exa.e = exa.e, exa.a
        else:
            exa.e, exa.x = exa.x, exa.e
        if a==direc[0]:
            pos= l_map.findXel(exa.__neg__()) #q
        else:
            pos= l_map.findXel(exa.__neg__()).link[coords[(coords.index(direc[0])+2)%6]] #w
    if direc=='aq':
        direc='qa'
    l_map= adj_maps[direc]
    position= pos

def choose_piv():
    global position
    global change_dir
    if position.exa.e==0:
        return 'e' if 'e' in change_dir else 'a'
    if position.exa.x==0:
        return 'w' if 'w' in change_dir else 's'
    if position.exa.a==0:
        return 'q' if 'q' in change_dir else 'd'


        

    

#Main execution
init()
print(position)
print("--------------------------------------------------------------------------------")
while 1:
    a=input()
    menu(a)
    print(position)
    print("--------------------------------------------------------------------------------")
