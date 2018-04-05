from Exa import *

class Xel:
    def __init__(self, origin=None, direction=None):
        self.values=None
        self.exa=None
        self.link= {'q':None,'w':None,'e':None,'d':None,'s':None,'a':None}

        if origin != None and direction != None :
            if direction == "q" :
                self.exa= origin.Q()
            elif direction == "w":
                self.exa= origin.W()
            elif direction == "e":
                self.exa= origin.E()
            elif direction == "d":
                self.exa= origin.D()
            elif direction == "s":
                self.exa= origin.S()
            elif direction == "a":
                self.exa= origin.A()
        else:
            self.exa=Exa()

    def __str__(self):
        return Exa.__str__(self.exa) + f" -> [   q: {self.link['q'].exa if self.link['q']!=None else None},   w: {self.link['w'].exa if self.link['w']!=None else None},   e: {self.link['e'].exa if self.link['e']!=None else None},   d: {self.link['d'].exa if self.link['d']!=None else None},   s: {self.link['s'].exa if self.link['s']!=None else None},   a: {self.link['a'].exa if self.link['a']!=None else None}   ]"

#q,w,e,d,s,a
#0,1,2,3,4,5
    @staticmethod
    def newHex(radius):
        origin = Xel()
        tmp_or = origin #scan every xel
        next_or = origin  #change origin after a final step
        lastXel=None #last created exa
        index=list(origin.link.keys())  # index of directions

        #BASIC CASE
        lastXel= tmp_or.link['q'] = Xel(origin.exa, 'q') #first link (new exa)
        tmp_or=lastXel
        lastXel= tmp_or.link['e']= Xel(lastXel.exa,'e') #second link (new exa)
        tmp_or=lastXel
        tmp_or.link['s']= origin #last link (existing exa)
        tmp_or=origin

        i=0
        j=0
        while(j<6*radius*radius-1):
            i+=1
            j+=1
            #STANDARD/FINAL FIRST LINK CASE
            tmp_or.link[index[i%6]]=lastXel #first link (existing exa)
            tmp_or=lastXel
            #STANDARD CASE         
            if next_or.link[index[(i+1)%6]]==None:   
                lastXel= tmp_or.link[index[(i+2)%6]]= Xel(lastXel.exa, index[(i+2)%6]) #second link (new exa)
                tmp_or=lastXel
                tmp_or.link[index[(i+4)%6]]=next_or #last link (existing exa)
                tmp_or=next_or
                continue #not a final case
            #FINAL CASE
            tmp_or.link[index[(i+2)%6]]= next_or.link[index[(i+1)%6]] #second link (existing exa)
            tmp_or= next_or.link[index[(i+1)%6]]
            tmp_or.link[index[(i+4)%6]]=next_or #last link (existing exa)
            next_or=tmp_or #change origin for next cycle
            i-=2

        tmp_or=lastXel # set temp_or on the edge
        i=1
        
        while(i<=6): #create external links
            if tmp_or.link[index[i%6]]==None: 
                i+=1 #change direction
            else:
                tmp_or.link[index[i%6]].link[index[(i+3)%6]]= tmp_or #go back
                tmp_or =tmp_or.link[index[i%6]] #create link
        return origin          

    # movement func
    def Q(self):
        return self.link['q']
    def W(self):
        return self.link['w']
    def E(self):
        return self.link['e']
    def D(self):
        return self.link['d']
    def S(self):
        return self.link['s']
    def A(self):
        return self.link['a']

    # Compact function for movement
    def move_to(self, direction='q'):
        assert direction in ['q', 'w', 'e', 'd', 's', 'a']
        return self.link[direction]

    def findXel(self, exa):
        # Usa un array direzioni che contiene le 6 possibili direzioni di spostamento
        # Ne prende un sottoarray di 2 direzioni in base alla coordinata maggiore di exa
        # Sceglie su quale delle due direzioni muoversi prima in base alla coord minore in modulo
        # Prima si muove in dir_1 compiendo mov_1 passi
        # Infine si muove in dir_2 compiendo mov_2 passi

        assert self.exa == Exa(0, 0, 0)
        # q,w,e,d,s,a
        # 0,1,2,3,4,5
        directions = ['q', 'w', 'e', 'd', 's', 'a']

        coord = {'e': exa.e, 'x': exa.x, 'a': exa.a}
        abcoord = {'e': abs(exa.e), 'x': abs(exa.x), 'a': abs(exa.a)}
        print(coord)
        coord = sorted(coord.items(), key=lambda coord: coord[1])
        abcoord = sorted(abcoord.items(), key=lambda abcoord: abcoord[1])
        print(coord)

        if coord[2][1]>=abs(coord[0][1]):#e o x o a
            max_coord= coord[2][0]
            inv=False
        else:
            max_coord= coord[0][0]#-e o -x o -a
            inv=True
        print("max_coord: ", max_coord)

        if max_coord is 'e':
            i = 0
        elif max_coord is 'x':
            i = 2
        else:  # max_coord is 'a':
            i = 4
        two_directions = [directions[i], directions[i+1]]
        print(two_directions)

        min_abcoord = abcoord[0][0]
        print("MIN: ", min_abcoord)

        if min_abcoord is 'e':
            i = 0
        elif min_abcoord is 'x':
            i = 2
        else:  # min_abcoord is 'a':
            i = 4
        four_directions = [directions[i], directions[i+1], directions[(i+3) % 6], directions[(i+4) % 6]]
        print(four_directions)

        if two_directions[0] in four_directions:
            dir_1 = two_directions[0]
            dir_2 = two_directions[1]
        else:
            dir_1 = two_directions[1]
            dir_2 = two_directions[0]
        print(f"dir_1: {dir_1}, dir_2: {dir_2}")

        mov_1 = abcoord[0][1]
        mov_2 = abcoord[1][1]
        print(f"mov_1: {mov_1}, mov_2: {mov_2}")

        res = origin

        while mov_1 > 0:
            res = res.move_to(dir_1)
            mov_1 -= 1

        while mov_2 > 0:
            res = res.move_to(dir_2)
            mov_2 -= 1

        return res

origin= Xel.newHex(5)
print(origin.findXel(Exa(-1,-4,5)), "\n")
print(origin.findXel(Exa(-4,-1,5)), "\n")
print(origin.findXel(Exa(-3,3,0)), "\n")
print(origin.findXel(Exa(2,-4,2)), "\n") # TODO: errore grave! Da risolvere ma ho sonno! (Francesco)
print(origin)
