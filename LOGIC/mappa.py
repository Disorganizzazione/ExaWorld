from Xel import *
radius=10#radius maps
g_map=None#pointer to origin of the global map
g_position=None #global position
l_map=[None, None, None]#map where your are in (max 3) [0:origin map, 1 or 2: other cross map]
l_position=[None, None, None]#your position in l_map (max 3)
b_map={'qw':None,'we':None, 'ed':None,'ds':None,'sa':None,'aq':None}#map stored in memory

def init():
    g_map=Xel.newHex(radius)
    g_position=Exa()
    l_map[0]=Xel.newHex(radius)
    l_position[0]=Exa()
    for i in b_map :
        b_map[i]=Xel.newHex(radius)

def mirror() :
    print("ciao")
    if l_position[0].e == radius or l_position[0].e == -radius:
        l_position[1]= Exa(-l_position[0].e,-l_position[0].a,-l_position[0].x)
        
    if l_position[0].x == radius or l_position[0].x == -radius:
        i= 2 if abs(l_position[0].x) == abs(l_position[0].e) else 1
        l_position[i] =Exa(-l_position[0].a,-l_position[0].x,-l_position[0].e)

    if l_position[0].a == radius or l_position[0].a == -radius:
        l_position[2]= Exa(-l_position[0].e,-l_position[0].a,-l_position[0].x)

def cross_map():
    mirror()
    direc=[False]
    if l_position.__len__()>0:
        if abs(l_position[0].e)==radius:
            direc[0]=True
            if l_position[0].e<0:
                l_map[1]= b_map['ds']
                direc.append('ds')
            else:
                l_map[1]= b_map['qw']
                direc.append('qw')
        if abs(l_position[0].x)==radius:
            direc[0]=True
            i= 2 if abs(l_position[0].x) == abs(l_position[0].e) else 1
            if l_position[0].x<0:
                l_map[i]= b_map['aq']
                direc.append('aq')
            else:
                l_map[i]= b_map['ed']
                direc.append('ed')
        if abs(l_position[0].a)==radius:
            direc[0]=True
            if l_position[0].a<0:
                 l_map[2]= b_map['we']
                 direc.append('we')
            else:
                l_map[2]= b_map['sa']
                direc.append('sa')
    return direc


def change_map(check, a):
    print(check)


def menu(a):
    if a=="q":
        l_position[0]=l_position[0].Q()
    elif a=="w":
        l_position[0]=l_position[0].W()
    elif a=="e":
        l_position[0]=l_position[0].E()
    elif a=="d":
        l_position[0]=l_position[0].D()
    elif a=="s":
        l_position[0]=l_position[0].S()
    elif a=="a":
        l_position[0]=l_position[0].A()
    elif a=="exit":
        quit()
    check= cross_map()
    if(check[0]==True):
        if (a in check[1] or a in check[2]):
            change_map(check[1:3], a)
        


init()
print(l_position[0])
while 1:
    a=input()

    menu(a)
    print("--------------------------------------------------------------------------------")
    try:
        print(l_map, l_position[0],'mappa2',l_position[1],'mappa3', l_position[2])
    except :
        print(l_map,l_position[0])
