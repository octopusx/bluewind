class Configurinator:
    address = ""
    cmd = ""
    speed = ""
 
    def __init__(self):
        pass

    def load_config(self, address, cmd, speed):
        self.address = address
        self.cmd = cmd
        self.speed = speed
