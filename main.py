from turtle import *
import argparse

parser = argparse.ArgumentParser(description="Arguments",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-np", "--number_of_operations", required=True, default="5", type=int, help="Number of operations. Recommended 2 to 12 operations.")
args = parser.parse_args()
#config = vars(args)
#print(config)

title("DrawingBe")
color("purple", "white")
pensize(2)
speed(0)
bgcolor("black")
#actions = ["lt(90), fd(30), rt(20), fd(55), lt(200), fd(40), lt(45), fd(70), lt(33), fd(50), rt(120), fd(30), lt(30), fd(40), lt(20), fd(100), lt(50), fd(50), lt(140), fd(80)"]
#actions = ["fd(100), lt(10), fd(20)"]
#actions = ["lt(10), fd(60), lt(30), fd(50), lt(100), fd(40), rt(60), fd(30), rt(40), fd(100), lt(34), fd(44), lt(76), fd(56), lt(27), fd(25), rt(15), fd(48)"]
#setpos(-60,-100)
#actions = ["fd(10), rt(90), fd(20), rt(120), fd(40), rt(70), fd(50), lt(120), fd(70), rt(40), fd(30), rt(55), fd(45), rt(130), fd(67)"]
actions = ["fd(50), rt(30), fd(70), lt(34), fd(30), rt(210), fd(61)"]

for i in range(args.number_of_operations):
    for h in range(len(actions)):
        circle(100,180)
        exec(actions[h])
        circle(70,120)
          
done()
