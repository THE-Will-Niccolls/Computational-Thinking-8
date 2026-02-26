import turtle, time, random
from utils import *

# Section 1 - setup
set_background("cookie1")

cookie = 0
cookiejar = 0
cost = 15



#Pressing "c" buys a cookiejar. Every cookiejar is 15 cookie. You try to get as many jars as possible

def get_cookiejar():
    global cookie, cookiejar, cost
    if cookie >= cost:15
        cost = cost * 2
        cookiejar += 1
        x = -400 + 120*cookiejar
        y = -250
        create_sprite("cookiejar.gif",x,y)

window.onkeypress(get_cookiejar, "space")

def get_cookie():
    global cookie
    cookie += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("cookie",x, y)

window.onkeypress(get_cookie, "c")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
   
 
    cookie += cookiejar



    time.sleep(0.01)
    window.update()