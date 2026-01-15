# Section 1 - Your code
from utils import *
set_background("SEA")

s1 = create_sprite("Flag", 100, 100)
s2 = create_sprite("Soccer", -100, 100)
s3 = create_sprite("Kirk", -100, -100)
s4 = create_sprite("Nuggets", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Will",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("I lick ice cream",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()