from sense_hat import SenseHat
from time import sleep
import random

class snake:
    
    def __init__(self):
        
        # Variablen deklarieren
        self.sense = SenseHat()
        
        self.snake = {
                        "posX": 5,
                        "posY": 2,
                        "prePosX": 5,
                        "prePosY": 2
                    }
        
        self.snakeLocX = 1
        self.snakeLocY = 0
        self.applePosX = 0
        self.applePosY = 0
        self.snakeSpeed = 0.6
        self.GREEN = (0, 102, 0)
        self.RED = (102, 0, 0)
        self.tail = {}
        self.move = "right"
        self.createApple(0)
        self.update_matrix()
    
    def start(self):
        
        while True:
            
            self.__init__()
            self.sense.clear()            
            self.gameloop()

    def gameloop(self):
        
        while True:
            
            sleep(self.snakeSpeed)
            self.control()
            self.set_snake_position(self.snakeLocX, self.snakeLocY)
            if self.collision() == 1:
                return 0
            self.update_matrix()
    
    def createApple(self, addTail = 1):
        
        endLoop = 0
        
        while endLoop == 0:
        
            endLoop = 1
        
            self.applePosX = random.randint(0, 7)
            self.applePosY = random.randint(0, 7)
            
            if len(self.tail) != 0:
            
                for a, b in self.tail.items():
                    if b["posX"] == self.applePosX and b["posY"] == self.applePosY:
                        endLoop = 0
                        
        if addTail == 1:
        
            if len(self.tail) == 0:
                self.tail[len(self.tail)] = {
                                            "posX": self.snake["prePosX"],
                                            "posY": self.snake["prePosY"]
                                        }
            else:
                self.tail[len(self.tail)] = {
                                            "posX": self.tail[len(self.tail)-1]["prePosX"],
                                            "posY": self.tail[len(self.tail)-1]["prePosY"]
                                            
                                        }
        
        
        if self.snakeSpeed != 0.2:
            self.snakeSpeed -= 0.05
        
    def collision(self):
        
        if len(self.tail) != 0:
            for x, y in self.tail.items():
                if y["posX"] == self.snake["posX"] and y["posY"] == self.snake["posY"]:
                    sleep(1)
                    return 1
        
        if self.snake["posX"] == self.applePosX and self.snake["posY"] == self.applePosY:
            self.sense.set_pixel(self.applePosX, self.applePosY, (0, 0, 0))
            self.createApple()
    
    def control(self):
        
        events = self.sense.stick.get_events()
        
        for event in events:
            
            if event.direction == "left" and self.move != "left" and self.move != "right":
                
                self.snakeLocX = -1
                self.snakeLocY = 0
                # print("Move Left")
                self.move = event.direction
                
                
            elif event.direction == "right" and self.move != "right" and self.move != "left":
                self.snakeLocX = 1
                self.snakeLocY = 0
                # print("Move Right")
                self.move = event.direction
                
                
            elif event.direction == "up" and self.move != "up" and self.move != "down":
                self.snakeLocX = 0
                self.snakeLocY = -1
                # print("Move Up")
                self.move = event.direction
                
                
            elif event.direction == "down" and self.move != "down" and self.move != "up":
                self.snakeLocX = 0
                self.snakeLocY = 1
                # print("Move Down")
                self.move = event.direction
                
            
            
            
    def set_snake_position(self, x, y):
        
        if (self.snake["posY"]+y) < 0:
            self.snake["posY"] = 8
        
        if (self.snake["posY"]+y) > 7:
            self.snake["posY"] = -1
        
        if (self.snake["posX"]+x) < 0:
            self.snake["posX"] = 8
        
        if (self.snake["posX"]+x) > 7:
            self.snake["posX"] = -1
        
       
        self.snake["prePosX"] = self.snake["posX"]
        self.snake["prePosY"] = self.snake["posY"]
        self.snake["posX"] = self.snake["posX"] + x
        self.snake["posY"] = self.snake["posY"] + y
        
        if len(self.tail) != 0:

            for a, b in self.tail.items():

                if a == 0:
                    
                    self.tail[0]["prePosX"] = self.tail[0]["posX"]
                    self.tail[0]["prePosY"] = self.tail[0]["posY"]
                    self.tail[0]["posX"] = self.snake["prePosX"]
                    self.tail[0]["posY"] = self.snake["prePosY"]
                    
                    if (self.tail[0]["posY"]) < 0:
                        self.tail[0]["posY"] = 7
                    
                    if (self.tail[0]["posY"]) > 7:
                        self.tail[0]["posY"] = 0
                    
                    if (self.tail[0]["posX"]) < 0:
                        self.tail[0]["posX"] = 7
                    
                    if (self.tail[0]["posX"]) > 7:
                        self.tail[0]["posX"] = 0
                
                else:
                    self.tail[a]["prePosX"] = self.tail[a]["posX"]
                    self.tail[a]["prePosY"] = self.tail[a]["posY"]
                    self.tail[a]["posX"] = self.tail[a-1]["prePosX"]
                    self.tail[a]["posY"] = self.tail[a-1]["prePosY"]
                    
                    if (self.tail[a]["posY"]) < 0:
                        self.tail[a]["posY"] = 7
                    
                    if (self.tail[a]["posY"]) > 7:
                        self.tail[a]["posY"] = 0
                    
                    if (self.tail[a]["posX"]) < 0:
                        self.tail[a]["posX"] = 7
                    
                    if (self.tail[a]["posX"]) > 7:
                        self.tail[a]["posX"] = 0
            
            
        
    
    def update_matrix(self):
        
        self.sense.clear()
        self.sense.set_pixel(self.snake["posX"], self.snake["posY"], (213, 0, 255))
        if len(self.tail) != 0:
            
            for x, y in self.tail.items():
                
                self.sense.set_pixel(y["posX"], y["posY"], self.GREEN)
            
        self.sense.set_pixel(self.applePosX, self.applePosY, self.RED)