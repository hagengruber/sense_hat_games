from sense_hat import SenseHat
from time import sleep
import random

class test:
    
    def __init__(self):
        
        self.player = {
                        "x": 1,
                        "y": 4,
                        "color": (0, 0, 104),
                        "def": 0
                    }
                    
        self.sense = SenseHat()
        
        self.comet = {}
        
    def start(self):
        
        self.sense.clear()
        
        self.gameloop()
    
    def gameloop(self):
        
        x, y, z = self.sense.get_accelerometer_raw().values()
        self.player["def"] = y*100
        
        while True:
            
            sleep(0.1)
            self.create_comet()
            self.set_player_position()
            self.set_comet_position()
            if self.collision() == 1:
                return 1
            self.update_matrix()
    
    
    def set_comet_position(self):
        
        for a, b in self.comet.items():
            
            if (b["x"]-1) >= 0:
                b["x"] -= 1
            else:
                b["color"] = (0, 0, 0)
    
    def create_comet(self):
        
        if random.randint(0, 100) < 70:
            return 0
        
        self.comet[len(self.comet)] = {
                                        "x": 8,
                                        "y": random.randint(0, 7),
                                        "color": (64, 64, 64)
                                    }
    
    
    def collision(self):
        
        for a, b in self.comet.items():
            
            if b["x"] == self.player["x"] and b["y"] == self.player["y"]:
                self.sense.set_pixel(self.player["x"], self.player["y"], (104, 0, 0))
                sleep(1)
                return 1
    
    def set_player_position(self):
        
        x, y, z = self.sense.get_accelerometer_raw().values()
        dif = round((self.player["def"]-(y*100)) / 20)
        
        y = 3-dif
        
        if y < 0:
            y = 0
        if y > 7:
            y = 6
        
        self.player["y"] = y
    
    def update_matrix(self):
        
        self.sense.clear()
        self.sense.set_pixel(self.player["x"], self.player["y"], self.player["color"])
        for a, b in self.comet.items():
            
            self.sense.set_pixel(b["x"], b["y"], b["color"])