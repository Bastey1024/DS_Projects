import numpy as np
import cv2
import math
import random
import datetime




market = cv2.imread("./data/market.png")
customer = cv2.imread("./data/customer.png")
thiev = cv2.imread("./data/thiev.png")
moneycustomer = cv2.imread("./data/moneycustomer.png")
ghost = cv2.imread("./data/ghost.png")
ghostbuster = cv2.imread("./data/ghostbuster.png")


# start = datetime.datetime(2019, 9, 4, 0, 0, 0)
# end = datetime.datetime(2019, 9,5, 0, 0, 0)
# delta = end - start


current_location={'entrance' :['x': 700,'y': 635]}
dairy = [235 - (random.randint(0, 150)), 400 - (random.randint(0, 250))]
fruits = [800 - (random.randint(0, 50)), 400 - (random.randint(0, 250))]
spices = [640 - (random.randint(0, 50)), 400 - (random.randint(0, 250))]
drinks = [235 - (random.randint(0, 50)), 400 - (random.randint(0, 250))]




class Customer:
    def __init__(self, image, x, y, current_location="entrance"):  # constructor
        self.image = image
        self.x = x
        self.y = y
        # self.enter=Pass##Pandas dataframe timestamp##
        self.current_location = current_location
        # self.moneyspent=0##row in pandas Df##

    def draw(self, frame):
        frame[
            self.y : self.y + self.image.shape[0], self.x : self.x + self.image.shape[1]
        ] = self.image

    def move(self):
        self.x += np.random.choice([-1, 0, 1]) * 1
        self.y += np.random.choice([-1, 0, 1]) * 1
        if self.x < 60:
            self.x = 60
        if self.y < 0:
            self.y = 0
        if self.x > 900:
            self.x = 900
        if self.y > 635:
            self.y = 635


    def move_dairy(self):
        if self.x>235 - (random.randint(0, 150)):
         self.x +=  -1
         if self.x < 205:
                self.y+=-1
        else:
            self.current_location='dairy'

    def move_upper_hall(self):
        if self.y>60- (random.randint(0,30)):
            self.y+=-1
            if self.x<600:
                self.x+=+1
    # def move




        # else:
        #  self.x+= +1
        #
        # if self.y < 120 + (random.randint(0, 15)):
        #      self.y+=-1

         # self.y < 500:
            # self.y += 2
         # if self.y
         # self.y+= 1
        # if self.x <235:
        #             self.x+=-1
        # else:
                # pass

    #     if self.y != dairy[1]:
    #
    #     if self x is not equal to dairy 0 then move right or left
    #
    #
    #     if self x is not equal to dairy 0 then move right or left
    #     +-1 repeat till == dairy 1
    #

    # self.x += 2
    # self.x = round(200*math.sin(math.radians(i))) + 250

    def __repr__(self):
        return f"""is in section
               {self.current_location}"""


Customers = [
    Customer(
        ghost, 860  - (random.randint(0, 150)*i), 635 * i, current_location="entrance"
    )
    for i in range(23)
]


peter = Customer(ghostbuster, 855, 460, current_location="entrance")

ghost1=Customer(ghost,890,510, current_location='entrance')
ghost2=Customer(ghost,846,520, current_location='entrance')
ghost3=Customer(ghost,861,524, current_location='entrance')
ghost4=Customer(ghost,861,424, current_location='entrance')



while True:
    frame = market.copy()

    # for i in range(delta.minute + 1):
    #     print(start + datetime.timedelta(minute=i))

    # cv2.putText(frame,str(datetime.now()),(20,10), 50,1,1,1,1,cv2.LINE_AA)

    cv2.putText(frame,str('2019-09-04 01-32')  , (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2,cv2.LINE_AA)

    # customer1.move_dairy(dairy)
    # customer1.draw(frame)

    if peter is current_location=='entrance':
        peter.move()
        peter.draw(frame)
        peter.move_dairy()
    if peter is current_location=='dairy':
        peter.move_upper_hall()




    ghost1.move()
    ghost1.move_dairy()
    ghost1.draw(frame)

    ghost2.move()
    ghost2.move_dairy()
    ghost2.draw(frame)

    ghost3.move()
    ghost3.move_dairy()
    ghost3.draw(frame)

    ghost4.move()
    ghost4.move_dairy()
    ghost4.draw(frame)
    # moneycustomer.draw(frame)
    # moneycustomer.move_dairy()

    for c in Customers:
        c.move()
        c.draw(frame)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()
