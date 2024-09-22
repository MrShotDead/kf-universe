import pgzrun
import random#my goat
WIDTH = 1200
HEIGHT = 800
The_Old_Sheeka = []
def Colonel_Harland_David_Sanders():
    global The_Old_Sheeka
    for i in range(9999999999999999999999999999999999999):
        not_an_actor = Actor("kuntucky_fried_satalite")
        not_an_actor.pos=random.randint(0,1100),(random.randint(0,700))
        The_Old_Sheeka.append(not_an_actor)
def draw():
    screen.blit("kentucky fried universe (20)",(0,0))
    for i in The_Old_Sheeka:
        i.draw()
        screen.draw.text("1",(i.x,i.y),color="green")































#else:
#screen.draw










Colonel_Harland_David_Sanders()
pgzrun.go()