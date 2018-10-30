from direct.showbase.ShowBase import ShowBase
from panda3d.core import PandaNode, NodePath, TextNode, OrthographicLens, Camera, VBase2, VBase3
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerQueue, CollisionRay, CollideMask
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
import sys
import math
import random
from opensimplex import OpenSimplex
from ExaRandomMachine import ExaRandom
import Submap

from GRAPHIC import LoadLight, LoadModel
from LOGIC import Map as Map
from LOGIC import Exa as Exa
from LOGIC import Xel as Xel

CHAR_MAX_ZGAP = 11  # temporary value
apo = 0.86603

PI = math.pi
# factor to convert angles from rad to deg
RAD_DEG = 180.0/PI
# factor to convert angles from deg to rad
DEG_RAD = PI/180.0
side = 1
R= Map.radius
v3s = math.sqrt(3) * side / 2.0
v3R = math.sqrt(3) * R / 2.0
s3 = 1.5*side
dirs = ['q', 'w', 'e', 'd', 's', 'a']

scale= math.sqrt(3)

#coords = {'qw': ((-v3R*scale -s3).__round__(1), (1.5*R*scale +apo).__round__(1)), 'we': ((v3R*scale +0).__round__(1), (1.5*R*scale +2*apo).__round__(1)), 'ed': ((2*v3R*scale +s3).__round__(1), (0*scale +apo).__round__(1)),
#          'ds': ((v3R*scale +s3).__round__(1), (-1.5*R*scale -apo).__round__(1)), 'sa': ((-v3R*scale +0).__round__(1), (-1.5*R*scale -2*apo).__round__(1)), 'qa': ((-2*v3R*scale -s3).__round__(1), (0*scale -apo).__round__(1))}

coords = {'qw': (-v3R*scale -s3, 1.5*R*scale +apo), 'we': (v3R*scale +0, 1.5*R*scale +2*apo), 'ed': (2*v3R*scale +s3, 0*scale +apo),
          'ds': (v3R*scale +s3, -1.5*R*scale -apo), 'sa': (-v3R*scale +0, -1.5*R*scale -2*apo), 'qa': (-2*v3R*scale -s3, 0*scale -apo)}

v3= math.sqrt(3)
print(coords)
#print(coords1)
#previous exa position
pix_pos_tmp= VBase3(0,0,0)

# NodePath container
all_nodes = set() # useless (TODO: consider if it'll be useful)

# list of stored submaps
stored_submaps_list = {}
# array of on-screen submaps
rendered_submaps = []
# current submap
current_submap = None
# temporary submap for map movement
new_submap = None

# distance of each char's step in dt (delta time)
step = 5    
# distance between camera and char in x,y plane
cam_dist = 5
# distance between camera and char in z axis
cam_dz = 10
# angles (in rad) that the camera can assume.
# In deg: {-120, 180, 120, 60, 0, -60}
cam_angle = {'q': -PI*2/3.0, 'w': PI, 'e': PI*2/3.0, 'd': PI/3.0, 's': 0, 'a': -PI/3.0}
cam_view = 's'
# camera's task frequency: pause between spinCameraTasks call (seconds)
cam_task_time = 0.01  # 0.01 is the min value accepted
# related to camera's rotation speed (degrees)
cam_delta_angle = 5
# used to check if the camera rotation task is running
cam_rotating = False
# char's rotation angle
char_angle = 0


# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1), scale=.05,
                        shadow=(0, 0, 0, 1), parent=base.a2dTopLeft,
                        pos=(0.08, -pos - 0.04), align=TextNode.ALeft)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1, 1, 1, 1), scale=.07,
                        parent=base.a2dBottomRight, align=TextNode.ARight,
                        pos=(-0.1, 0.09), shadow=(0, 0, 0, 1))

# Function to put runtime data on the screen.
def addInfo(pos, text):
    return OnscreenText(text=text, style=1, fg=(1, 1, 1, 1), scale=.07,
                        parent=base.a2dBottomLeft, align=TextNode.ALeft,
                        pos=(0.08, pos + 0.04), shadow=(0, 0, 0, 1))

# NodePath definition
def SubmapNode(name="set_N"):
    n = NodePath(name)
    all_nodes.add(n)
    return n

class MyApp(ShowBase):

    def insertTile(self, node, submap_center, xel:Xel.Xel, tile_z):
        dx, dy = submap_center
        (q,r) = xel.exa.x, xel.exa.e
        v_center = VBase2(s3*q, v3s*2*(q/2+r))

        tile_color = "green" #TODO
        if q == r == 0:
            tile_color = "red"
        elif abs(q) == Map.radius or abs(r) == Map.radius or abs(xel.exa.a) == Map.radius:
            tile_color = "yellow"
        else:  #temporary
            if tile_z > 3:
                tile_color = "brown"
            elif tile_z<0:
                tile_color = "blue"
        
        return self.model.loadExaTile(node, v_center[0] + dx, v_center[1] + dy, tile_z, tile_color)

    def drawTriangle(self, node, submap_center, submap_xel, triangle_index, nodes_Z, open_simplex):
        center_map = submap_xel
        for d in range(1, Map.radius+1):  # distance from center moving along triangle side t
            center_map = center_map.link[dirs[triangle_index]]
            tmp_map = center_map
            for n in range(0, d):  # each cell from triangle_index triangle edge (included) to next triangle edge (excluded)
                if d==Map.radius and n==0: 
                    cell_z = nodes_Z[triangle_index]
                else:
                    cell_z = ExaRandom.interpolate(self, (nodes_Z[6], nodes_Z[triangle_index], nodes_Z[(triangle_index+1)%6]), Map.radius, (tmp_map.exa.e, tmp_map.exa.x, tmp_map.exa.a))
                
                cell_z += open_simplex.noise2d(tmp_map.exa.x, tmp_map.exa.e)/5
                self.insertTile(node, submap_center, tmp_map, cell_z)
                tmp_map = tmp_map.link[dirs[(triangle_index+2)%6]]

    def drawSubmap(self, submap):
        l_map = Map.l_map  # TODO: chose if letting this way or pass l_map as parameter

        open_s = OpenSimplex(submap.noise_seed)

        #Center
        self.insertTile(submap.node, submap.centerXY, l_map, submap.array_Z[6])

        ### Graphic map construction, triangle-by-triangle way
        center_map = l_map
        for t in range(6):  # scan each triangle
            self.drawTriangle(submap.node, submap.centerXY, center_map, t, submap.array_Z, open_s)
        ###
        return submap

    def drawMap(self, submap):
        global current_submap
        global stored_submaps_list
        global rendered_submaps

        new_seven_centers = []
        for d,v in coords.items():
            temp_c = ((v[0]+submap.centerXY[0]), (v[1]+submap.centerXY[1]))
            #print("-----------------------",v, submap.centerXY, temp_c) #BUGGONE
            new_seven_centers.append(temp_c)
        new_seven_centers.append(submap.centerXY)

        if len(rendered_submaps)==0:  # Starting case
            submap.node = SubmapNode("0")
            submap.node.reparentTo(self.render)
            center= self.drawSubmap(submap)
            rendered_submaps.append(center)
            tmp_rendered_submaps=[None, None, None, None, None, None, center]
        else:
            tmp_rendered_submaps=[None, None, None, None, None, None, None]

        useful_values = []
            
        for i in range(7):
            draw=True #check if a sub_map in new_seven_centers has to be drawn.
            #print all rendenew_seven_centersred maps
            """print("Rendered:")
            for s in rendered_submaps:
                print(s, end='')
            print("")"""
            c = new_seven_centers[i]
            for s in rendered_submaps:
                #diff = (abs(c[0] - s.centerXY[0]), abs(c[1] - s.centerXY[1]))
                print("_--------------",c,s)
                print("DIFF= ", math.isclose(c[0], s.centerXY[0], abs_tol=0.1) and math.isclose(c[1],s.centerXY[1], abs_tol=0.1))
                if math.isclose(c[0], s.centerXY[0], abs_tol=0.1) and math.isclose(c[1],s.centerXY[1], abs_tol=0.1):
                    draw=False #if a map in new_seven_centers is already in rendered_submaps set draw to false
                    tmp_rendered_submaps[i] = s
                    # prova
                    useful_values.append(s)
                    break
            if draw==True: #if draw is still True, then draw the map in new_seven_centers
                if c in stored_submaps_list.keys():
                    s_map = stored_submaps_list[c]
                else:
                    s_map = ExaRandom().create_submap(c)
                    stored_submaps_list[c] = s_map
                s_map.node = SubmapNode("1")
                s_map.node.reparentTo(self.render)
                tmp_rendered_submaps[i] = self.drawSubmap(s_map)
                #rendered_submaps.append(self.drawSubmap(self.render, s_map))
                print(c, "drawn\n")
            else:
                print(c, "NOT drawn\n")
        # identify no-longer loaded submaps and clear their nodes
        for s in rendered_submaps:
            if s not in tmp_rendered_submaps:
                self.clear_node(s.node)
                s.node.removeNode() # needs to be tested (TODO)
                s.node = None # if previous line doesn't remove it automatically

        rendered_submaps= tmp_rendered_submaps
        current_submap = submap
        print("Rendered:")
        for s in rendered_submaps:
            print(s, end='')
        print("")

    def clear_node(self, nodepath):
        if not nodepath.isEmpty():
            for model in nodepath.getChildren():
                model.removeNode()

    def clear_all_nodes(self):
        self.clear_node(rendered_submaps[random.randint(0,5)].node) # temporary madness
        #for n in all_nodes:
        #    self.clear_node(n)
        #    n.remove_node()

    def print_all_nodes(self):
        string = ""
        for n in all_nodes:
            string += str(n)+ "; "
        print(string)

    def __init__(self):
        ShowBase.__init__(self)

        # Load Lights
        self.light = LoadLight.Light
        self.light.setupLight(self)

        # Load Environment
        self.model = LoadModel.Model()
        self.model.initialize(self)

        Map.init()
        map_center = (0,0)
        subprova = Submap.Submap(map_center)
        global stored_submaps_list
        global current_submap
        stored_submaps_list[map_center] = subprova
        current_submap = subprova
        print("stored in init:", stored_submaps_list)
        self.drawMap(subprova)

        

        self.model.loadAnimal(5,6,0, "bear")
        self.model.loadAnimal(12,-6,0, "cow")
        self.model.loadAnimal(7,-9,0, "panther")
        self.model.loadAnimal(-17,5,0, "rabbit")
        self.model.loadAnimal(-7,5,0, "wolf")
        
        self.model.loadPlant(8,-2,0, "fir")
        self.model.loadPlant(-3,-2,0, "grass")
        self.model.loadPlant(-4,2,0, "oak")
        self.model.loadPlant(-1,17,0, "berry_bush")
        
        
        # Text on screen
        self.text_char_pos = None
        self.text_submap = None
        self.text_lock = None

        # Create the main character
        self.char = self.model.loadCharacter(0, 0, 0)

        # We will detect the height of the terrain by creating a collision
        # ray and casting it downward toward the terrain.  One ray will
        # start above char's head, and the other will start above the camera.
        # A ray may hit the terrain, or it may hit a rock or a tree.  If it
        # hits the terrain, we can detect the height.  If it hits anything
        # else, we rule that the move is illegal.
        self.cTrav = CollisionTraverser()

        self.charGroundRay = CollisionRay()
        self.charGroundRay.setOrigin(0, 0, 9)
        self.charGroundRay.setDirection(0, 0, -1)
        self.charGroundCol = CollisionNode('charRay')
        self.charGroundCol.addSolid(self.charGroundRay)
        self.charGroundCol.setFromCollideMask(CollideMask.bit(0))
        self.charGroundCol.setIntoCollideMask(CollideMask.allOff())
        self.charGroundColNp = self.char.attachNewNode(self.charGroundCol)
        self.charGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.charGroundColNp, self.charGroundHandler)

        # Uncomment this line to see the collision rays
        self.charGroundColNp.show()

        # Uncomment this line to show a visual representation of the
        # collisions occuring
        self.cTrav.showCollisions(render)

        # This is used to store which keys are currently pressed.
        self.keyMap = {"restart": 0, "left": 0, "right": 0, "forward": 0, "backward": 0,
                       "cam-q": 0, "cam-w": 0, "cam-e": 0, "cam-d": 0, "cam-s": 0, "cam-a": 0}

        # Post the instructions
        self.title = addTitle("Isometric HexaMap test")
        self.inst1 = addInstructions(0.06, "[ESC]: Quit")
        self.inst2 = addInstructions(0.12, "[Arrow Keys]: Move char")
        self.inst3 = addInstructions(0.18, "[Q,W,E,D,S,A]: Change camera's angle of view")
        #self.inst8 = addInstructions(0.48, "[R]: Restart")

        # Accept the control keys for movement and rotation
        self.accept("escape", sys.exit)
        self.accept("n", self.print_all_nodes)
        self.accept("k", self.clear_all_nodes)
        self.accept("arrow_left", self.setKey, ["left", True])
        self.accept("arrow_right", self.setKey, ["right", True])
        self.accept("arrow_up", self.setKey, ["forward", True])
        self.accept("arrow_down", self.setKey, ["backward", True])
        self.accept("q", self.setKey, ["cam-q", True])
        self.accept("w", self.setKey, ["cam-w", True])
        self.accept("e", self.setKey, ["cam-e", True])
        self.accept("d", self.setKey, ["cam-d", True])
        self.accept("s", self.setKey, ["cam-s", True])
        self.accept("a", self.setKey, ["cam-a", True])
        self.accept("arrow_left-up", self.setKey, ["left", False])
        self.accept("arrow_right-up", self.setKey, ["right", False])
        self.accept("arrow_up-up", self.setKey, ["forward", False])
        self.accept("arrow_down-up", self.setKey, ["backward", False])
        self.accept("q-up", self.setKey, ["cam-q", False])
        self.accept("w-up", self.setKey, ["cam-w", False])
        self.accept("e-up", self.setKey, ["cam-e", False])
        self.accept("d-up", self.setKey, ["cam-d", False])
        self.accept("s-up", self.setKey, ["cam-s", False])
        self.accept("a-up", self.setKey, ["cam-a", False])
        # self.accept("restart", self.char.setPos(0,0,0))

        self.taskMgr.add(self.move, "moveTask")

        # Game state variables
        self.isMoving = False

        # Set up the camera with isometric perspective
        self.disableMouse()
        lens = OrthographicLens()
        lens.setFilmSize(20, 16)
        lens.setNear(-1)
        self.cam.node().setLens(lens)
        self.camera.setPos(self.char.getPos() +
                           (math.sin(cam_angle[cam_view]) * cam_dist,
                            -math.cos(cam_angle[cam_view]) * cam_dist,
                            cam_dz))
        self.camera.lookAt(self.char)

    # Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value

    def move(self, task):
        # Get the time that elapsed since last frame.  We multiply this with
        # the desired speed in order to find out with which distance to move
        # in order to achieve that desired speed.
        dt = globalClock.getDt()

        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.
        global cam_view
        temp_cam = cam_view
        if self.keyMap["cam-q"]:
            cam_view = 'q'
        if self.keyMap["cam-w"]:
            cam_view = 'w'
        if self.keyMap["cam-e"]:
            cam_view = 'e'
        if self.keyMap["cam-d"]:
            cam_view = 'd'
        if self.keyMap["cam-s"]:
            cam_view = 's'
        if self.keyMap["cam-a"]:
            cam_view = 'a'

        global cam_rotating
        final_angle = int(round((cam_angle[cam_view] * RAD_DEG))) % 360
        current_angle = int(round(self.camera.getH())) % 360

        # Camera rotation task is triggered when a different angle of view is selected.
        # The direction of rotation is chosen by comparing the two angles
        # and changing the sign of the camera rotation angle: cam_delta_angle
        if final_angle != current_angle:
            if not self.taskMgr.hasTaskNamed("SpinCameraTask"):
                global cam_delta_angle
                diff = final_angle - current_angle
                cam_delta_angle = math.copysign(cam_delta_angle, diff)
                if diff > 180:
                    cam_delta_angle = math.copysign(cam_delta_angle, -1)
                elif diff < -180:
                    cam_delta_angle = math.copysign(cam_delta_angle, 1)
                self.taskMgr.doMethodLater(cam_task_time, self.spinCameraTask, "SpinCameraTask")
            cam_rotating = True

        if not cam_rotating:
            # save char's initial position so that we can restore it,
            # in case he falls off the map or runs into something.
            startpos = self.char.getPos()
            # If a move-key is pressed, turn and move char in the relative direction.
            # The pressure of multiple keys at the same time is handled by the v_rot vector
            # Movements in 2D plane depend on camera's position & orientation
            v_rot = VBase3(0, 0, 0)

            if self.keyMap["forward"]:
                v_rot += (0, 1, 0)
            if self.keyMap["backward"]:
                v_rot += (0, -1, 0)
            if self.keyMap["left"]:
                v_rot += (-v3, 0, 0)
            if self.keyMap["right"]:
                v_rot += (v3, 0, 0)
            
            if v_rot.normalize():
                self.char.lookAt(self.char.getPos() + v_rot)
                self.char.setH(self.char.getH() + self.camera.getH())
                self.char.setY(self.char, step*dt)

            # Normally, we would have to call traverse() to check for collisions.
            # However, the class ShowBase that we inherit from has a task to do
            # this for us, if we assign a CollisionTraverser to self.cTrav.
            self.cTrav.traverse(render)

            # Adjust char's Z coordinate.  If char's ray hit terrain,
            # update his Z. If it hit anything else, or didn't hit anything, put
            # him back where he was last frame.
            entries = list(self.charGroundHandler.getEntries())
            entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
            if (len(entries) > 0
                    and entries[0].getIntoNode().getName() == "ExaTile"
                    and entries[0].getSurfacePoint(render).getZ()-self.char.getZ() <= CHAR_MAX_ZGAP):
                self.char.setZ(entries[0].getSurfacePoint(render).getZ())
            else:
                self.char.setPos(startpos)

            # Put on screen the lock's value
            #if self.text_lock != None:
            #    self.text_lock.destroy()
            #self.text_lock = addInfo(0.15, "Lock: "+str(Map.new_dir_lock))

            #QUIIIIIII+
            global pix_pos_tmp 
            pix_pos= self.char.getPos()

            

            exa_pos= None
            
            #if (math.isclose(abs(pix_pos[0])%(apo+0.05), apo, rel_tol=0.05) or math.isclose(abs(pix_pos[1])%(apo+0.05), apo,rel_tol=0.05)):
            
            exa_pos= -1/3 *pix_pos[0] + math.sqrt(3)/3*pix_pos[1], 2/3 * pix_pos[0]
            

            pix_pos= VBase3(round(exa_pos[0]), round(exa_pos[1]), 0)
            pix_pos+= VBase3(0,0, round(-pix_pos[0] - pix_pos[1]))

            
            pix_pos_diff= VBase3(abs(pix_pos[0] - exa_pos[0]), abs(pix_pos[1] - exa_pos[1]), abs(pix_pos[2] - (-exa_pos[0] - exa_pos[1])))


            if pix_pos_diff[0] > pix_pos_diff[1] and pix_pos_diff[0] > pix_pos_diff[2]:
                pix_pos[0]= -pix_pos[1]-pix_pos[2]
            elif pix_pos_diff[1] > pix_pos_diff[2]:
                pix_pos[1]= -pix_pos[0]-pix_pos[2]
            else:
                pix_pos[2]= -pix_pos[0]-pix_pos[1]

            if pix_pos_tmp != pix_pos:
                direc= pix_pos - pix_pos_tmp
                directions= {VBase3(1,-1,0): 'q', VBase3(1,0,-1): 'w', VBase3(0,1,-1): 'e', VBase3(-1,1,0): 'd', VBase3(-1,0,1): 's', VBase3(0,-1,1): 'a'}
                Map.menu(directions.get(direc))
                print(Map.position)
                #print(self.char.getPos())
                if self.text_char_pos != None:
                    self.text_char_pos.destroy()
                self.text_char_pos = addInfo(0, "Char position: ("+str(round(self.char.getX(),2))+" , "+str(round(self.char.getY(),2))+")")

                #Map.new_dir_lock=False
                # New submap check
                if Map.new_dir != None:
                    global current_submap
                    global new_submap
                    #Map.new_dir_lock=True
                    d = Map.new_dir
                    Map.new_dir = None
                    new_center = (current_submap.centerXY[0] + coords[d][0], current_submap.centerXY[1] + coords[d][1])
                    for c,s in stored_submaps_list.items():
                        if math.isclose(c[0], new_center[0], abs_tol=0.1) and math.isclose(c[1], new_center[1], abs_tol=0.1):
                            new_submap = s
                            break
                    self.drawMap(new_submap)  # TODO: maybe we can give direction as parameter
                    global rendered_submaps
                    print("Rendered.length = "+str(len(rendered_submaps)))
            
            pix_pos_tmp= pix_pos

            #Map.position= l_map.findXel()
        
            #print(Exa.Exa(pix_pos[0], pix_pos[1], -pix_pos[2]))

            # Camera position handling: it depends on char's position
            self.camera.setX(self.char.getX() + math.sin(current_angle*DEG_RAD) * cam_dist)
            self.camera.setY(self.char.getY() - math.cos(current_angle*DEG_RAD) * cam_dist)
            self.camera.setZ(self.char.getZ() + cam_dz)
            self.camera.lookAt(self.char)

        else:  # cam is rotating
            if final_angle == current_angle:
                print("CAM IN PLACE!")
                self.taskMgr.remove("SpinCameraTask")
                cam_rotating = False
        #print("curr: ", self.camera.getH())
        #print("dest: ", cam_angle[cam_view]*RAD_DEG)
        return task.cont

    # Task to animate the camera when user changes the angle of view.
    # Make the camera rotate counterclockwise around the character in x,y plane
    # TODO: add cam's "shortest path". The direction of rotation must be chosen according to the final angle of view
    def spinCameraTask(self, task):
        angle_deg = int(round(self.camera.getH())) + cam_delta_angle
        angle_rad = angle_deg * DEG_RAD
        delta_v = VBase3(self.char.getX() + cam_dist*math.sin(angle_rad),
                         self.char.getY() - cam_dist*math.cos(angle_rad),
                         self.camera.getZ())
        self.camera.setPos(delta_v)
        self.camera.lookAt(self.char)
        return task.done

    def restartGame(self):
        pass


app = MyApp()
app.run()
