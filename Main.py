import pgzrun
import random
WIDTH=1000
HEIGHT=500
actor=Actor('alien.png')
message='Click Alien'
def move():
    actor.x=random.randint(100,900)
    actor.y=random.randint(100,400)
def on_mouse_down(pos):
    global message
    if actor.collidepoint(pos):
        move()
        message='Good'
    else:
        
        message='Missed'
  

    
def draw():
    screen.clear()
    actor.draw()
    screen.draw.text(message,(500,250),fontsize=20)

pgzrun.go()