from sense_hat import SenseHat
from time import sleep
import random

class jump:
    
    def __init__(self):
        
        # Variablen deklarieren
        self.sense = SenseHat()
        self.player = {
                        "color": (104, 0, 0),
                        "x": 1,
                        "y": 5,
                        "jump": 0,
                        "fall": 0
                    }
        self.speed = 0.2
        self.stone = {}
        
    def start(self):
        
        while True:
            
            self.__init__()
            self.sense.clear()
            self.gameloop()

    def gameloop(self):
        
        while True:
            
            sleep(self.speed)
            self.control()
            self.create_stone()
            self.set_player_position()
            self.set_stone_position()
            if self.collision() == 1:
                return 1
            self.update_matrix()
    
    def create_stone(self):
        
        if random.randint(0, 100) < 90:
            return 0
        
        self.stone[len(self.stone)] = {
                                        "x": 8,
                                        "y": 5,
                                        "color": (64, 64, 64)
                                    }
    
    def set_stone_position(self):
        
        for a, b in self.stone.items():
            
            if (b["x"]-1) >= 0:
                b["x"] -= 1
            else:
                b["color"] = (0, 0, 0)
    
    def collision(self):
        
        for a, b in self.stone.items():
            
            if b["x"] == self.player["x"] and b["y"] == self.player["y"]:
                sleep(1)
                return 1
    
    def control(self):
        
        events = self.sense.stick.get_events()
        
        for event in events:
            
            if event.direction == "up" and self.player["jump"] == 0 and self.player["fall"] == 0:
                self.player["jump"] = 1
                self.player["fall"] = 2
                
            if event.direction == "down" and self.player["fall"] != 0:
                self.player["jump"] = 5
                self.player["fall"] = 2
    
    def set_player_position(self):
        
        if self.player["jump"] == 5 and self.player["fall"] == 0:
            self.player["jump"] = 0
            self.player["fall"] = 0
        
        elif self.player["jump"] < 3 and self.player["jump"] > 0:
            self.player["y"] -= 1
            self.player["jump"] += 1
            
        elif self.player["jump"] != 5 and self.player["jump"] > 0:
            self.player["jump"] += 1
        
        elif self.player["fall"] != 0 and self.player["jump"] == 5 and self.player["y"] != 5:
            self.player["y"] += 1
            self.player["fall"] -= 1
        
        elif self.player["fall"] != 0 and self.player["y"] == 5:
            self.player["fall"] = 0

    def update_matrix(self):
        
        self.sense.clear()
        self.sense.set_pixel(self.player["x"], self.player["y"], self.player["color"])
        self.sense.set_pixel(self.player["x"], self.player["y"]-1, self.player["color"])
        self.sense.set_pixel(self.player["x"], self.player["y"]-2, self.player["color"])
        
        for i in range(8):
            
            self.sense.set_pixel(i, 6, (0, 51, 102))
        
        for a, b in self.stone.items():
            
            self.sense.set_pixel(b["x"], b["y"], b["color"])