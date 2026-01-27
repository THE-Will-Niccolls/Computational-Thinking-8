import turtle, time, random
from utils import *

set_background(cookie1)

cookies = 0
jars = 0



def get_cookies():
    global cookies
    cookies += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("cardinal3",x,y)
window.onkeypress(get_cookie, "space")
window.onkeypress(get_jar, "c")





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()