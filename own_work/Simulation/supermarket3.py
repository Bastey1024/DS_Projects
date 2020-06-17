import numpy as np
import cv2
import math
import random


market = cv2.imread("./data/market.png")
customer = cv2.imread("./data/customer.png")
thiev = cv2.imread("./data/thiev.png")
moneycustomer = cv2.imread("./data/moneycustomer.png")
ghost = cv2.imread("./data/ghost.png")
ghostbuster = cv2.imread("./data/ghostbuster.png")

current_location = {"entrance": [860 - (random.randint(0, 150)), 635]}
entrance = [860 - (random.randint(0, 150)), 635]
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
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > 900:
            self.x = 900
        if self.y > 635:
            self.y = 635

    ########
    #         def move_up(self):
    #         if isinstance(self.location.n(), Square):
    #             self.location = self.location.n()
    #         else:
    #             pass
    #
    #     def move_right(self):
    #         if isinstance(self.location.e(), Square):
    #             self.location = self.location.e()
    #         else:
    #             pass
    #
    #     def move_down(self):
    #         if isinstance(self.location.s(), Square):
    #             self.location = self.location.s()
    #         else:
    #             pass
    #
    #     def move_left(self):
    #         if isinstance(self.location.w(), Square):
    #             self.location = self.location.w()
    #         else:
    #             pass
    # ###############
    #   # Movement suite
    #     def move(self):
    #         if self.location == self.square_map[12] or \
    #         self.location == self.square_map[13]:
    #             self.location = self.location.n()
    #
    #         elif self.location == self.square_map[14] or \
    #         self.location == self.square_map[24]:
    #             self.location = self.location.e()
    #
    #         elif self.location == self.square_map[33] or \
    #         self.location == self.square_map[34]:
    #             self.location = self.location.s()
    #
    #         elif self.location == self.square_map[32] or \
    #         self.location == self.square_map[22]:
    #             self.location = self.location.w()

    # def move_dairy(self):
    #
    #
    #     if self.x != dairy[0]:
    #
    #
    #
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
        ghost, 860 * i - (random.randint(0, 150)), 635 * i, current_location="entrance"
    )
    for i in range(30)
]
# [Spaceship(spaceship, 50*i + 250, i*100 + 50) for i in range(5)]
# customer1 = Customer(moneycustomer,500-(random.randint(0,150)), 300,current_location='entrance')
peter = Customer(ghostbuster, 860, 533, current_location="entrance")
moneycustomer = Customer(
    moneycustomer,
    235 - (random.randint(0, 50)),
    400 - (random.randint(0, 250)),
    current_location="drinks",
)

while True:
    frame = market.copy()

    # customer1.move_dairy(dairy)
    # customer1.draw(frame)

    peter.move()
    peter.draw(frame)

    moneycustomer.draw(frame)

    for c in Customers:
        c.move()
        c.draw(frame)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()
