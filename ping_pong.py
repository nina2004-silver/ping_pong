from pygame import *

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
window.fill((210, 255, 255))

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:
       display.update()
       clock.tick(FPS)
