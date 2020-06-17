import numpy as np
import cv2
import math

class Spaceship:

    def __init__(self,image,x,y):    #Its called the constructor
        self.image=image
        self.x=x
        self.y=y
        # self.path = path

    def draw(self):
        frame[self.y:self.y+self.image.shape[0],self.x:self.x+spaceship.shape[1]]=self.image

    def move(self):
        """Moves the ship"""

        self.x+=np.random.choice([-1,0,1])*5
        self.y+=np.random.choice([-1,0,1])*5

        if self.x < 0 : self.x=0
        if self.y < 0 : self.y=0
        if self.x >700 : self.y=700
        if self.y >500 : self.y=500

    def __repr__(self):
        return f'spaceship at {self.x}/{self.y}'



stars = cv2.imread('stars.png')
spaceship = img = cv2.imread('ship.png')

# ships=[Spaceship(spaceship,300,300) for i in range(10)]

ship1=Spaceship(spaceship,100,100)
# ship2=Spaceship(spaceship,300,300,'path placeholder')

while True:
    frame = stars.copy()
    ship1.move()
    ship1.draw()
# # frame[100:183,100:192] =spaceship


    # # x=x+1
    # # x=round(200*math.sin(math.radians(i)))+200
    # # i+=1

    # i+=1
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
