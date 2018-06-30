from direct.showbase.ShowBase import ShowBase
from panda3d.core import PandaNode, NodePath, Camera, TextNode, OrthographicLens
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
import sys
import math

from GRAPHIC import LoadLight, LoadModel
from LOGIC import *


apo=0.86603
r=1
side = r
v3s = math.sqrt(3) * side / 2
s3 = 3 * side / 2
dirs = ['q', 'w', 'e', 'd', 's', 'a']
coords = {'q': (-s3, v3s), 'w': (0, v3s * 2), 'e': (s3, v3s),
          'd': (s3, -v3s), 's': (0, -v3s * 2), 'a': (-s3, -v3s)}
cam_distance = [(0, -10, 20), (-10, 0, 20)]
cam_current = 0

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
        self.keyMap = {"restart": 0, "left": 0, "right": 0, "forward": 0, "backward": 0, "cam-left": 0, "cam-right": 0}

        # Post the instructions
        self.title = addTitle("Isometric HexaMap test")
        self.inst1 = addInstructions(0.06, "[ESC]: Quit")
        self.inst2 = addInstructions(0.12, "[Left Arrow]: Rotate char Left")
        self.inst3 = addInstructions(0.18, "[Right Arrow]: Rotate char Right")
        self.inst4 = addInstructions(0.24, "[Up Arrow]: Run char Forward")
        self.inst5 = addInstructions(0.30, "[Down Arrow]: Run char Backward")
        self.inst6 = addInstructions(0.36, "[A]: Rotate Camera Left")
        self.inst7 = addInstructions(0.42, "[S]: Rotate Camera Right")
        #self.inst8 = addInstructions(0.48, "[R]: Restart")

        # Accept the control keys for movement and rotation
        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.setKey, ["left", True])
        self.accept("arrow_right", self.setKey, ["right", True])
        self.accept("arrow_up", self.setKey, ["forward", True])
        self.accept("arrow_down", self.setKey, ["backward", True])
        self.accept("a", self.setKey, ["cam-left", True])
        self.accept("s", self.setKey, ["cam-right", True])
        self.accept("arrow_left-up", self.setKey, ["left", False])
        self.accept("arrow_right-up", self.setKey, ["right", False])
        self.accept("arrow_up-up", self.setKey, ["forward", False])
        self.accept("arrow_down-up", self.setKey, ["backward", False])
        self.accept("a-up", self.setKey, ["cam-left", False])
        self.accept("s-up", self.setKey, ["cam-right", False])
        # self.accept("restart", self.char.setPos(0,0,0))

        taskMgr.add(self.move, "moveTask")

        # Game state variables
        self.isMoving = False

        # Set up the camera with isometric perspective
        self.disableMouse()
        self.camera.setPos(self.char.getPos() + cam_distance[cam_current])
        self.camera.lookAt((0,0,0))
        lens = OrthographicLens()
        lens.setFilmSize(30, 25)
        base.cam.node().setLens(lens)

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
        if self.keyMap["cam-left"]:
            cam_current = 1
        if self.keyMap["cam-right"]:
            #self.camera.setX(self.camera, +20 * dt)
            cam_current = 0

        # save char's initial position so that we can restore it,
        # in case he falls off the map or runs into something.
        startpos = self.char.getPos()

        # If a move-key is pressed, move char in the specified direction.
        if self.keyMap["left"]:
            self.char.setH(self.char.getH() + 300 * dt)
        if self.keyMap["right"]:
            self.char.setH(self.char.getH() - 300 * dt)
        if self.keyMap["forward"]:
            self.char.setY(self.char, -25 * dt)
        if self.keyMap["backward"]:
            self.char.setY(self.char, +25 * dt)

        self.camera.setPos(self.char.getPos()+cam_distance[cam_current])
        self.camera.lookAt(self.char)

        return task.cont

    def restartGame(self):
        pass



app = MyApp()
app.run()
