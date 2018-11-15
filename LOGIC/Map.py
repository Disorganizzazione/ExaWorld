from LOGIC import Xel as Xel
import gc, sys
import copy

radius=8 #radius maps
position=None #position in l_map. Must be a Xel! position.exa in order to get coordinates (EXA)
l_map=None #local map
adj_maps={'qw':None,'we':None, 'ed':None,'ds':None,'sa':None,'qa':None} #maps stored in memory
change_dir=None #POSSIBLE directions that will lead to change map
new_dir = None
#new_dir_lock= False #if false, is unlocked (you can access to drawap)

def init():
    #global initializations
    global l_map
    global position
    global adj_maps
    #instantiate
    l_map= Xel.Xel.newHex(radius)
    position= l_map
    for i in adj_maps:
        adj_maps[i]=Xel.Xel.newHex(radius)
    
def menu(a): #a=input direction
    global position
    if is_border(a)==False: #is_border -> changemap -> mirror
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
    global new_dir#, new_dir_lock
    coords = ['q', 'w', 'e', 'd', 's', 'a']
    direc=None #new map direction (ex. qw, we ...)
    if a in change_dir: #the input direction leads to change the map
        """print("Direction= ",a)"""
        direc=change_dir[0]+change_dir[1] #n==2
        if n==3:
            piv=choose_piv() #the direction that can leads 
            if a==piv:
                direc=[k for k in adj_maps.keys() if piv in k and coords[(coords.index(piv)+1)%6] in k].pop() #ex. q (qw)
            else:
                direc= [k for k in adj_maps.keys() if piv in k and a in k].pop() #ex. w or a (qw or qa)
            update_maps(direc) #update adj_maps and local_map
            mirror(a, direc, piv)
            print("New Map= ",direc)
            #if not new_dir_lock:
            new_dir = direc
            return True
        update_maps(direc) #update adj_maps and local_map
        mirror(a, direc, None) #mirror the new position
        print("New Map= ",direc)
        #if not new_dir_lock:
        new_dir = direc
        return True
    else:
        return False
    
def mirror(a, direc, piv):
    global l_map
    global position
    pos=None #temp new position
    exa= copy.copy(position.exa) #exa of the new position (for find xel)
    coords = ['q', 'w', 'e', 'd', 's', 'a']
    if direc=='qa':
        direc='aq'
    if piv!=None: #corner
        if a==piv: #-2 (q) 
            exa.a, exa.x = exa.x, exa.a
            exa.a, exa.e = exa.e, exa.a
            pos= l_map.findXel(exa) 
        elif direc[1]==coords[(coords.index(piv)+1)%6]: #q+1=(w)
            exa.a, exa.x = exa.x, exa.a
            exa.a, exa.e = exa.e, exa.a
            pos= l_map.findXel(exa).link[coords[(coords.index(direc[0])+2)%6]]  #q+2 - ossia q+e (w)
        else: #+2 (a)
            exa.a, exa.x = exa.x, exa.a
            exa.e, exa.x = exa.x, exa.e
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
    position= pos #update mirrored position

def update_maps(direc):
    global l_map
    global adj_maps
    l_map_tmp=l_map 
    l_map= adj_maps[direc]
    d= list(adj_maps.keys()) #adj_maps keys
    i=d.index(direc) #index of direc
    #switch existing maps
    adj_maps[d[(i-2)%6]]=adj_maps[d[(i-1)%6]] #sa=aq
    adj_maps[d[(i+3)%6]]=l_map_tmp #ds=qw
    adj_maps[d[(i+2)%6]]=adj_maps[d[(i+1)%6]] #ed=we
    #create last 3 map
    adj_maps[d[(i-1)%6]]=Xel.Xel.newHex(radius) #aq=new_aq
    adj_maps[d[(i)%6]]=Xel.Xel.newHex(radius) #qw=new_qw
    adj_maps[d[(i+1)%6]]=Xel.Xel.newHex(radius) #we=new_we
    """print("Collected:           ", gc.collect()," objects")"""

def choose_piv():
    global position
    global change_dir
    if position.exa.e==0:
        return 'e' if 'e' in change_dir else 'a'
    if position.exa.x==0:
        return 'w' if 'w' in change_dir else 's'
    if position.exa.a==0:
        return 'q' if 'q' in change_dir else 'd'

"""
#Main execution
init()
print("--------------------------------------------------------------------------------")
while 1:
    print(position)
    print("loc :   ", str(hex(id(l_map)))[-5:])
    for i in adj_maps:
        print(i, " :   ", str(hex(id(adj_maps.get(i))))[-5:]) 
    print("--------------------------------------------------------------------------------")
    a=input()
    menu(a)
    usage = sum(sys.getsizeof(i) for i in gc.get_objects())
    print("Mem usage:           ",usage, "bytes")
"""
