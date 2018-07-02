from direct.showbase.ShowBase import ShowBase
from panda3d.core import PandaNode, NodePath, Camera, TextNode, OrthographicLens
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
import sys
import math

from GRAPHIC import LoadLight, LoadModel
from LOGIC import *


apo = 0.86603
r = 1
PI = math.pi
side = r
v3s = math.sqrt(3) * side / 2
s3 = 3 * side / 2
dirs = ['q', 'w', 'e', 'd', 's', 'a']
coords = {'q': (-s3, v3s), 'w': (0, v3s * 2), 'e': (s3, v3s),
          'd': (s3, -v3s), 's': (0, -v3s * 2), 'a': (-s3, -v3s)}

# distance of each char's step in dt
step = 5
# distance between camera and char in x,y plane
cam_dist = 5
# distance between camera and char in z axis
cam_dz = 10
# angles (in rad) that the camera can assume.
# In deg: {-120, 180, 120, 60, 0, -60}
cam_angle = {'q': -PI*2/3, 'w': PI, 'e': PI*2/3, 'd': PI/3, 's': 0, 'a': -PI/3}
cam_current = 's'
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
    def __init__(self):
        ShowBase.__init__(self)

        # Load Lights
        self.light = LoadLight.Light
        self.light.setupLight(self)

        # Load Environment
        self.model = LoadModel.Model
        hex0 = self.model.loadModels(self, 0, 0, 0)
        hexs = list()
        x, y = hex0.getX(), hex0.getY()
        for i in range(6):
            center = (x + coords[dirs[i]][0],
                      y + coords[dirs[i]][1])
            hexs.append(self.model.loadModels(self, center[0], center[1], hex0.getZ()+i*0.2))

        # Create the main character
        self.char = self.model.loadCharacter(self, 0, 0, 0)

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

        taskMgr.add(self.move, "moveTask")

        # Game state variables
        self.isMoving = False

        # Set up the camera with isometric perspective
        self.disableMouse()
        lens = OrthographicLens()
        lens.setFilmSize(20, 16)
        self.cam.node().setLens(lens)
        self.camera.setPos(self.char.getPos() +
                           (math.sin(cam_angle[cam_current]) * cam_dist,
                            -math.cos(cam_angle[cam_current]) * cam_dist,
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
        global cam_current
        if self.keyMap["cam-q"]:
            cam_current = 'q'
            print(self.camera.getH())
        if self.keyMap["cam-w"]:
            print(self.camera.getH())
            cam_current = 'w'
        if self.keyMap["cam-e"]:
            print(self.camera.getH())
            cam_current = 'e'
        if self.keyMap["cam-d"]:
            cam_current = 'd'
            print(self.camera.getH())
        if self.keyMap["cam-s"]:
            print(self.camera.getH())
            cam_current = 's'
        if self.keyMap["cam-a"]:
            print(self.camera.getH())
            cam_current = 'a'

        # save char's initial position so that we can restore it,
        # in case he falls off the map or runs into something.
        startpos = self.char.getPos()

        # If a move-key is pressed, move char in the specified direction.
        # Movements in 2D plane depend on camera's position-orientation
        ang = (self.camera.getH())/180 * math.pi
        delta_cos = math.cos(ang) * step * dt
        delta_sin = math.sin(ang) * step * dt

        if self.keyMap["forward"]:
            self.char.setH(self.camera.getH())
            self.char.setPos(self.char.getPos() + (-delta_sin, delta_cos, 0))
        if self.keyMap["backward"]:
            self.char.setH(self.camera.getH() - 180)
            self.char.setPos(self.char.getPos() - (-delta_sin, delta_cos, 0))
        if self.keyMap["left"]:
            self.char.setH(self.camera.getH() + 90)
            self.char.setPos(self.char.getPos() - (delta_cos, delta_sin, 0))
        if self.keyMap["right"]:
            self.char.setH(self.camera.getH()-90)
            self.char.setPos(self.char.getPos() + (delta_cos, delta_sin, 0))

        self.camera.setPos(self.char.getPos() +
                           (math.sin(cam_angle[cam_current])*cam_dist,
                            -math.cos(cam_angle[cam_current])*cam_dist,
                            cam_dz))
        self.camera.lookAt(self.char)

        return task.cont

    def restartGame(self):
        pass



app = MyApp()
app.run()
