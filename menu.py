from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

g = (0, 104, 0)
e = (0, 0, 0)
b = (0, 0, 104)

g1 = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, e, b, e, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, e, e, e, e, e
]
g2 = [
    e, e, e, e, e, e, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, e, e, b, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, b, e, e, e, e,
    e, e, b, b, b, b, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e
]
g3 = [
    e, e, e, e, e, e, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, e, e, b, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, e, b, e, e, e,
    e, e, b, e, e, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, e, e, e, e, e, e
]
g4 = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, e, b, e, e, e,
    e, b, b, b, b, e, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, e, e, e, e, e
]

end = 0
show = 1

while end == 0:
    
    if show == 1:
        sense.set_pixels(g1)
    elif show == 2:
        sense.set_pixels(g2)
    elif show == 3:
        sense.set_pixels(g3)
    elif show == 4:
        sense.set_pixels(g4)
    
    sleep(0.5)
    
    events = sense.stick.get_events()
        
    for event in events:
        
        if event.direction == "right":
            if (show+1) != 5:
                show += 1
                del events
                break
            
        if event.direction == "left":
            if (show-1) != 0:
                show -= 1
                del events
                break
        
        if event.direction == "middle":
            start(show)
            exit()
    
    def start(game):
        
        if game == 1:
            from snake import snake
            s = snake()
            s.start()
        
        if game == 2:
            from jump import jump
            s = jump()
            s.start()
        
        if game == 3:
            from not_pong import not_pong
            s = not_pong()
            s.start()
        
        if game == 4:
            from comet import comet
            s = comet()
            s.start()