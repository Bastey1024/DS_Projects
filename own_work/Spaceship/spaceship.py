import numpy as np
import cv2
import math

stars = cv2.imread('stars.png')
spaceship = img = cv2.imread('ship.png')

print(stars.shape)
print(spaceship.shape)

#moving part
x= 100
y= 100



i=0
while True:
    frame = stars.copy()

    # frame[100:183,100:192] =spaceship
    frame[y:y+spaceship.shape[0],x:x+spaceship.shape[1]]=spaceship
    # x=x+1
    # x=round(200*math.sin(math.radians(i)))+200
    # i+=1
    x+=np.random.choice([-1,0,1])*5
    y+=np.random.choice([-1,0,1])*5
    i+=1
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
