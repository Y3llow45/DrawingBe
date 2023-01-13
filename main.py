from turtle import *
import argparse

parser = argparse.ArgumentParser(description="Arguments",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# add argument for colors
# add argument for setup
# setup(width=1920, height=1080, startx=0, starty=0)
parser.add_argument("-r", "--rotate", required=True, default="cw", help="rotate clockwise or counterclockwise")
parser.add_argument("-s", "--size", required=True, default="d", help="Line size and thickness. Small (s) default (d) big (b)")
parser.add_argument("-np", "--number_of_operations", required=True, default="5", type=int, help="Number of operations. Recommended 2 to 12 operations.")
args = parser.parse_args()
#config = vars(args)
#print(config)

title("DrawingBe")
color("purple", "white")
pensize(2)
speed(0)
bgcolor("black")#196 500
actions = ["left(90)", "forward(20)"]

#for i in range(args.number_of_operations):
#for h in range(len(actions)):
    #exec(actions[h])
#right(180)
for i in range(args.number_of_operations):
    print("Now will run: "+str(actions))
    for h in range(len(actions)):
        if "right" in actions[h]:
            x = actions[h].replace("right(", "")
            parsed_number = x.replace(")", "")
            #print("left({})".format(parsed_number))
            actions.append("left({})".format(parsed_number))
            exec("left({})".format(parsed_number))
        if "left" in actions[h]:
            x = actions[h].replace("left(", "")
            parsed_number = x.replace(")", "")
            #print("right({})".format(parsed_number))
            actions.append("right({})".format(parsed_number))
            exec("right({})".format(parsed_number))
        else:
            actions.append(actions[h])
            exec(actions[h])        
    
#right(180)
#for h in range(len(actions)):
    #if "right" in actions[h]:
        #x = actions[h].replace("right(", "")
        #parsed_number = x.replace(")", "")
        #print("left({})".format(parsed_number))
        #exec("left({})".format(parsed_number))
    #if "left" in actions[h]:
        #x = actions[h].replace("left(", "")
        #parsed_number = x.replace(")", "")
        #print("right({})".format(parsed_number))
        #exec("right({})".format(parsed_number))
    #else:
        #exec(actions[h])
#Notes:
#6.record action/s in a list
#7.rotate
#8.draw actions backwards from the list
#9.repeat 6/7/8 number times
#10. sleep 3 seconds and close
done()