from Exa import *

class Xel: 
    def __init__(self, *args):
        # Constructor with 0 parameter, origin cell
        if len(args) == 0:
            self.gon = Exa()
        # Constructor with 1 parameters, clone cell
        elif len(args) == 1 and isinstance(args[0], Xel):
            self.gon = Exa(args[0].gon)
        self.w = self
        self.e = self
        self.d = self
        self.x = self
        self.z = self
        self.a = self
        print("nuovo xel=",self.gon)

    def link(self, phase): #network generation
        #one link
        if phase==0: 
            self.e= Xel() #one link (on E axis) - 0
            self.e.gon.e_()
            self.e.z= self 
            return self.e
        #two links
        elif phase==1: 
            self.d= Xel() #second link (on D axis) - 1
            self.d.gon.d_()
            self.d.a= self #double link (opposite direction) 
            self.d.z= self.x #link from D to X (using Z axis) - 1.1
            self.x.e= self.d #double link (opposite direction)
            return self.d
        elif phase==2:
            x= Xel() #third link (on X axis) - 2
            self.x.gon.x_()
            self.x.w= self #double link (opposite direction)
            self.x.a= self.z #link from X to Z (using A axis) - 2.1
            self.z.d= self.x #double link (opposite direction)
            return self.x
        elif phase==3:
            z= Xel() #fourth link (on Z axis) - 3
            self.z.gon.z_()
            self.z.e= self #double link (opposite direction) 
            self.z.w= self.a #link from Z to A (using W axis) - 3.1
            self.a.x= self.z #double link (opposite direction)
            return self.z
        elif phase==4: 
            a= Xel() #fifth link (on A axis) - 4.1
            self.a.gon.a_()
            self.a.d= self #double link (opposite direction) 
            self.a.e= self.w #link from A to W (using E axis) - 4.1
            self.w.z= self.a #double link (opposite direction) 
            return self.a
        elif phase==5:
            w= Xel() #sixth link (on W axis) - 5
            self.w.gon.w_()
            self.w.x= self #double link (opposite direction) 
            self.w.d= self.e #link from W to E (using D axis) - 5.1
            self.e.a= self.w #double link (opposite direction) 
            return self.w          
        elif phase==6:
            e= Xel() #seventh (first) link (on E axis) - 6
            self.e.gon.e_()
            self.e.z= self #double link (opposite direction) 
            self.e.x= self.d #link from E to D (using X axis) - 6.1
            self.d.w= self.e #double link (opposite direction) 
            return self.e
        #three links
        elif phase==11:
            x= Xel(self) #2
            self.x.w= self #double link
            self.x.gon.x_()
            self.x.a= self.z #2.1
            self.z.d= x #double link
            self.x.z= self.z.x #create the middle point on the link X-Z
            self.z.x.e= self.x #create link from Z to the middle point and from the middle point to X
            return self.x
        elif phase==12:
            z= Xel(self) #3
            self.z.e= self #double link
            self.z.gon.z_()
            self.z.w= self.a #3.1
            self.a.x= z #double link
            self.z.a= self.a.z #create the middle point on the link Z-A
            self.a.z.d= self.z #create link from A to the middle point and from the middle point to Z
            return self.z
        elif phase==13:
            a= Xel(self) #4
            self.a.d= self #double link
            self.a.gon.a_()
            self.a.e= self.w #4.1
            self.w.z= a #double link
            self.a.w= self.w.a #create the middle point on the  link A-W
            self.w.a.x= self.a #create link from W to the middle point and from the middle point to A
            return self.a
        elif phase==14:
            w= Xel(self) #5
            self.w.x= self #double link
            self.w.gon.w_()
            self.w.d= self.e #5.1
            self.e.a= w #double link
            self.w.e= self.e.w #create the middle point on the  link W-E
            self.e.w.z= self.w #create link from E to the middle point and from the middle point to W
            return self.w
        elif phase==15:
            e= Xel(self) #6
            self.e.z= self #double link
            self.e.gon.e_()
            self.e.x= self.d #6.1
            self.d.w= e #double link
            self.e.d= self.d.e #create the middle point on the  link E-D
            self.d.e.a= self.e #create link from D to the middle point and from the middle point to E
            return self.e
        elif phase==16:
            d= Xel(self) #1
            self.d.a= self #double link
            self.d.gon.d_()
            self.d.z= self.x #1.1
            self.x.e= d #double link
            self.d.x= self.x.d #create the middle point on the  link D-X
            self.x.d.w= self.d #create link from X to the middle point and from the middle point to D
            return self.d
        else:
            return None
    
    def move(self, phase):
        if phase == 1:
            return self.d
        elif phase == 2:
            return self.x
        elif phase == 3:
            return self.z
        elif phase == 4:
            return self.a
        elif phase == 5:
            return self.w
        else: return None
    
    def access(self, exa): #MACHECOS fa questa funzione?
        """TODO"""
        temp = self
        print("self=",self.gon)
        #print(f"Hex.__str__: t\n")
        assert isinstance(exa, Exa)
        print(f"Xel.acces: temp={temp.gon}, exa={exa}")
        while exa.get_e() != 0:
            if exa.get_e() > 0:
                exa.z_()
                temp = temp.z
            else:
                exa.e_()
                temp = temp.e
            print(f"----wh1: temp={temp.gon}, exa={exa}")
        #
        while exa.get_x() != 0:
            if exa.get_x() > 0:
                exa.w_()
                temp = temp.w
            else:
                exa.x_()
                temp = temp.x
            print(f"----wh1: temp={temp.gon}, exa={exa}")
        #
        while exa.get_a() != 0:
            if exa.get_a() > 0:
                exa.d_()
                temp = temp.d
            else:
                exa.a_()
                temp = temp.a
            print(f"----wh1: temp={temp.gon}, exa={exa}")
        print(f"Xel.acces: temp={temp.gon}, exa={exa}") #ACCESS rende exa=0,0,0, lasciando tmp=0,0,0
        return temp

cella = Xel()
tempio = cella
print("tempio",tempio.gon)
for r in range(2):
        # first one
    if r > 0:
        tempio = tempio.link(6)
        for _ in range(r-1):
            tempio = tempio.link(16)
        # 4 slices
    for v in range(1, 5):
        if r == 0 and v == 1:
            tempio = tempio.link(0)
        else:
            tempio = tempio.link(v)
        for l in range(r):
            tempio = tempio.link(v + 10)
        # last one
    tempio = tempio.link(5)
    for l in range(r+1):
        tempio = tempio.link(15)

tempio=tempio.access(Exa(0,5,0))

print(tempio.gon)
