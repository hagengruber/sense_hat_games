from sense_hat import SenseHat
from time import sleep
import random

class not_pong:
    
    def __init__(self):
        
        self.sense = SenseHat()
        
        self.ball = {
                        "x": 5,
                        "y": 5,
                        "locX": 1,
                        "locY": 1,
                        "difX": 1,
                        "difY": 0,
                        "color": (104, 0, 0)
                    }
        
        self.player = {
                        "x": 1,
                        "y": 4,
                        "color": (0, 104, 0),
                        "locY": 0,
                        "prePosX": 1,
                        "prePosY": 5
                    }
        
        self.player_top = (0, 104, 0)
        self.player_bottom = (0, 104, 0)
        
        self.speed = 0.2
    
    def start(self):
        
        while True:
        
            self.__init__()
            self.sense.clear()
            self.gameloop()
    
    def gameloop(self):
        
        while True:
            sleep(self.speed)
            self.control()
            self.set_player_position()
            if self.set_ball_position() == 1:
                return 0
                
            self.collision()
            self.update_matrix()
    
    
    def collision(self):
        
        if self.ball["x"] == self.player["x"] and self.ball["y"] == self.player["y"]:
            
            self.ball["x"] = self.player["x"]+1
            self.ball["y"] = self.player["y"]
            self.player["color"] = (0, 0, 140)
            self.ball["locY"] *= -1
            self.ball["locX"] *= -1
        
        if self.ball["x"] == self.player["x"] and self.ball["y"] == (self.player["y"]-1):
            
            self.ball["x"] = self.player["x"]+1
            self.ball["y"] = self.player["y"]-1
            self.player_top = (0, 0, 140)
            self.ball["locY"] *= -1
            self.ball["locX"] *= -1
        
        if self.ball["x"] == self.player["x"] and self.ball["y"] == (self.player["y"]+1):
            
            self.ball["x"] = self.player["x"]+1
            self.ball["y"] = self.player["y"]+1
            self.player_bottom = (0, 0, 140)
            self.ball["locY"] *= -1
            self.ball["locX"] *= -1
    
    
    def control(self):
        
        events = self.sense.stick.get_events()
        
        for event in events:
            
            if event.direction == "up":
                self.player["locY"] = -1
                
            elif event.direction == "down":
                self.player["locY"] = 1
    
    
    def set_player_position(self):
        
        self.player["y"] += self.player["locY"]
    
    
    def set_ball_position(self):
        
        chDir = 0
        x = 0
        y = 0
        
        if (self.ball["y"]+self.ball["locY"]) < 0:
            #self.ball["locY"] = random.randint(1, 2)
            self.ball["locY"] *= -1
            self.ball["locX"] *= -1
            chDir = 1
            y = 1
            
        while (self.ball["y"]+self.ball["locY"]) > 7:
            #self.ball["locY"] = random.randint(1, 2)
            self.ball["locY"] *= -1
            self.ball["locX"] *= -1
            chDir = 1
            y = 1
            
        while (self.ball["x"]+self.ball["locX"]) < 0:
            sleep(1)
            return 1
           
        while (self.ball["x"]+self.ball["locX"]) > 7:
            #self.ball["locX"] = random.randint(1, 2)
            self.ball["locX"] *= -1
            self.ball["locY"] *= -1
            chDir = 1
            x = 1
    
        self.ball["x"] += self.ball["locX"]
        self.ball["y"] += self.ball["locY"]
        
        if chDir == 1:
            
            if self.ball["locX"] == 1:
                
                if random.randint(0, 1) == 0:
                
                    self.ball["y"] -= 1
                    self.ball["x"] += 1
                    
                else:
                    self.ball["y"] += 1
                    self.ball["x"] -= 1
        
            else:
                
                if random.randint(0, 1) == 0:
                
                    self.ball["y"] += 1
                    self.ball["x"] -= 1
                    
                else:
                    self.ball["y"] -= 1
                    self.ball["x"] += 1
        
            if random.randint(0, 1) == 0:
                
                if x == 0:
                    
                    self.ball["locX"] *= -1
                
                else:
                    
                    self.ball["locY"] *= -1
        
        chDir = 0
        
        if (self.ball["y"]) < 0:
            self.ball["y"] = 0
            
        if (self.ball["y"]) > 7:
            self.ball["y"] = 7
            
        if (self.ball["x"]) < 0:
            self.ball["x"] = 0
            
        if (self.ball["x"]) > 7:
            self.ball["x"] = 7
    
    def update_matrix(self):
        
        self.sense.clear()
        
        if (self.player["y"]) > 0 and (self.player["y"]+1) < 8:
            self.sense.set_pixel(self.player["x"], self.player["y"], self.player["color"])
            self.sense.set_pixel(self.player["x"], self.player["y"]-1, self.player_top)
            self.sense.set_pixel(self.player["x"], self.player["y"]+1, self.player_bottom)
            
            self.player["prePosX"] = self.player["x"]
            self.player["prePosY"] = self.player["y"]
            
        else:
            
            self.player["x"] = self.player["prePosX"]
            self.player["y"] = self.player["prePosY"]
            
            self.sense.set_pixel(self.player["x"], self.player["y"], self.player["color"])
            self.sense.set_pixel(self.player["x"], self.player["y"]-1, self.player_top)
            self.sense.set_pixel(self.player["x"], self.player["y"]+1, self.player_bottom)
        
        self.sense.set_pixel(self.ball["x"], self.ball["y"], self.ball["color"])
        self.player["locY"] = 0
        
        self.player["color"] = (0, 104, 0)
        self.player_top = (0, 104, 0)
        self.player_bottom = (0, 104, 0)