from Xel import *
radius=10#radius maps
g_map=None#pointer to origin of the global map
g_position=None #global position
l_map=list()#map where your are in (max 3)
l_position=list()#your position in l_map (max 3)
b_map={'qw':None,'we':None, 'ed':None,'ds':None,'sa':None,'aq':None}#map stored in memory

def init():
    g_map=Xel.newHex(radius)
    g_position=Exa()
    l_map.append(Xel.newHex(radius))
    l_position.append(Exa())
    for i in b_map :
        b_map[i]=Xel.newHex(radius)

def mirror() :
    print("ciao")
    if l_position[0].e == radius or l_position[0].e == -radius:
        l_position.append(Exa(-l_position[0].e,-l_position[0].a,-l_position[0].x))

    if l_position[0].x == radius or l_position[0].x == -radius:
        l_position.append(Exa(-l_position[0].a,-l_position[0].x,-l_position[0].e))

    if l_position[0].a == radius or l_position[0].a == -radius:
        l_position.append(Exa(-l_position[0].e,-l_position[0].a,-l_position[0].x))

def cross_map():
    mirror()
    if l_position.__len__()>0:
        if abs(l_position[0].e)==radius:
            if l_position[0].e<0:
                l_map.append(b_map['ds'])
            else:
                l_map.append(b_map['qw'])
        if abs(l_position[0].x)==radius:
            if l_position[0].x<0:
                l_map.append(b_map['aq'])
            else:
                l_map.append(b_map['ed'])
        if abs(l_position[0].a)==radius:
            if l_position[0].a<0:
                 l_map.append(b_map['we'])
            else:
                l_map.append(b_map['sa'])

def menu(a):
    if a=="q":
        l_position[0]=l_position[0].Q()
        cross_map()
    if a=="w":
        l_position[0]=l_position[0].W()
        cross_map()
    if a=="e":
        l_position[0]=l_position[0].E()
        cross_map()
    if a=="d":
        l_position[0]=l_position[0].D()
        cross_map()
    if a=="s":
        l_position[0]=l_position[0].S()
        cross_map()
    if a=="a":
        l_position[0]=l_position[0].A()
        cross_map()
    if a=="exit":
        quit()

def rolling_map(a):
    if a=='q' or a=='w':
    if a=='q' or a=='w':
    if a=='q' or a=='w':
    if a=='q' or a=='w':
    if a=='q' or a=='w':
    if a=='q' or a=='w':
        

init()
print(l_position[0])
while 1:
    a=input()
    rolling_map(a)
    menu(a)
    print("--------------------------------------------------------------------------------")
    try:
        print(l_position[0],'mappa2',l_position[1],'mappa3', l_position[2])
    except :
        print(l_map[0],l_position[0])
