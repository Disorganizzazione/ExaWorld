from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.obj1 = self.loader.loadModel("untitled.egg")
        self.obj1.reparentTo(self.render)

        self.obj1.setPos(-3,7,5)
        self.useDrive()

app = MyApp()
app.run()