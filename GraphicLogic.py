from direct.showbase.ShowBase import ShowBase
from panda3d.core import PandaNode, NodePath, TextNode, OrthographicLens, Camera, VBase2, VBase3
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerQueue, CollisionRay, CollideMask
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
import sys
import math
import random

from GRAPHIC import LoadLight, LoadModel
from LOGIC import Map as Map
from LOGIC import Exa as Exa

CHAR_MAX_ZGAP = 0.3
apo = 0.86603

PI = math.pi
# factor to convert angles from rad to deg
RAD_DEG = 180.0/PI
# factor to convert angles from deg to rad
DEG_RAD = PI/180.0
side = 1
v3s = math.sqrt(3) * side / 2.0
s3 = 1.5*side
dirs = ['q', 'w', 'e', 'd', 's', 'a']
coords = {'qw': (-s3, v3s), 'we': (0, v3s * 2), 'ed': (s3, v3s),
          'ds': (s3, -v3s), 'sa': (0, -v3s * 2), 'qa': (-s3, -v3s)}

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




class MyApp(ShowBase):
    def drawMap(self, x_center, y_center):
        
        Map.init()
        hexI = self.model.loadModels(self, x_center, y_center, 0) #Z= prevedi!
        
        #hex_n= (Map.radius+1)**3 - (Map.radius)**3 -1
        


        print(Map.l_map)
        #dirs = ['q', 'w', 'e', 'd', 's', 'a']
        for i in range(1, Map.radius+1): #scorre gli anelli
            Map.l_map= Map.l_map.link['s']
            for m in Map.adj_maps.values():
                m= m.link['s']
                print("--", m)
            print(Map.l_map)
            
            for j in range(6): #scorre gli esagoni
                for k in range(i): #scorre le posizioni
                    Map.l_map= Map.l_map.link[dirs[j]]
                    print(Map.l_map)
                    (q,r)= VBase2(Map.l_map.exa.x, Map.l_map.exa.a)
                    v_center= VBase3(s3*q, v3s*2*(q/2+r), random.uniform(0, CHAR_MAX_ZGAP*0.99)) #z=random
                    hexI= self.model.loadModels(self, v_center[0], v_center[1], v_center[2])
                    #adj maps
                    for k,m in Map.adj_maps.items():
                        m= m.link[dirs[j]]
                        hexI_adj= self.model.loadModels(self, v_center[0]+ coords[k][0]*Map.radius, v_center[1]+coords[k][1]*Map.radius, v_center[2])
                        print("--", m)




    def __init__(self):
        ShowBase.__init__(self)

        # Load Lights
        self.light = LoadLight.Light
        self.light.setupLight(self)

        # Load Environment
        self.model = LoadModel.Model
        
        #hexs = list()
        #x, y = hex0.getX(), hex0.getY()
        self.drawMap(0,0)



        # Create the main character
        self.char = self.model.loadCharacter(self, 0, 0, 0)

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
        # self.cTrav.showCollisions(render)

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
                v_rot += (-1, 0, 0)
            if self.keyMap["right"]:
                v_rot += (1, 0, 0)

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

            

            #QUIIIIIII




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
