import turtle, time, random
from utils import *

set_background("cookie1")

cookies = 0
jars = 0



def get_cookies():
    global cookies
    cookies += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("cookie",x,y)
window.onkeypress("get_cookie", "space")





def buy_jar():
    global cookies, jars
    if cookies >= 50:
        jar += 1
        cookies -= 50
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        create_sprite("cookiejar.gif",x,y)
window.onkeypress(buy_jar, "c")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()