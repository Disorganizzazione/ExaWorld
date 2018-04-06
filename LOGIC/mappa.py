from Xel import *
radius=100
g_map=None
g_position=None
l_map=[]
l_position=[]
b_map={'qw':None,'we':None, 'ed':None,'ds':None,'sa':None,'aq':None}

def map():
    g_map=Xel.newHex(radius)
    g_position=Exa()
    l_map.append(Xel.newHex(radius))

def cross_map():
    l_position=mirror(l_position[0])
    if l_position.len()>0:
        if abs(l_position[0].e)==radius:
            if l_position[0].e<0:
                l_map.append(b_map('ds'))
            else:
                l_map.append(b_map('qw'))
        if abs(l_position[0].x)==radius:
            if l_position[0].x<0:
                l_map.append(b_map('aq'))
            else:
                l_map.append(b_map('ed'))
        if abs(l_position[0].a)==radius:
            if l_position[0].a<0:
                 l_map.append(b_map('we'))
            else:
                l_map.append(b_map('sa'))




def mirror(position) :
    pos=[position]
    if position.e == radius or position.e == -radius:
        pos.append(Exa(-position.e,-position.a,-position.x))
    if position.x == radius or position.x == -radius:
        pos.append(Exa(-position.e,-position.a,-position.x))
    if position.a == radius or position.a == -radius:
        pos.append(Exa(-position.e,-position.a,-position.x))
    return pos

def menu(org):
    a=input()
    if a=="q":
        lposition[0]=l_position[0].A()
        cross_map()
    if a=="w":
        lposition[0]=l_position[0].Q()
        cross_map()
    if a=="a":
        lposition[0]=l_position[0].S()
        cross_map()
    if a=="s":
        lposition[0]=l_position[0].W()
        cross_map()
    if a=="z":
        lposition[0]=l_position[0].D()
        cross_map()
    if a=="x":
        lposition[0]=l_position[0].E()
        cross_map()
    if a=="exit":
        quit()
    return org

map
