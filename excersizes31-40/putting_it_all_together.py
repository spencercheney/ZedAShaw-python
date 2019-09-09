from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?" 

    next = raw_input("> ")
    how_much = int(next)

    if how_much < 50:
        print "Nice job. I proud of you for only taking what you need."
        exit(0)
    else:
        dead("Don't be greedy")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you and fights you for the honey. You lose.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("You make the bear mad and he eats you.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I don't know what that means."

def sully_room():
    print "You encounter a gaint, terrifying blue monster with purple polka dots."
    print "His name is Sully."
    print "Do you scream and run home or do you play with his tail and call him kitty?"

    next = raw_input("> ")

    if "play" in next or "kitty" in next:
        print "He is more scared of you than you are of him."
        print "You walk back through the door you entered."
        print "-----------"
        start()
    elif "scream" in next:
        dead("You get so scared you have a heart attack and die.")
    else:
        sully_room()


def dead(why):
    print why, "Good job!"
    exit(0) 

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        sully_room()
    else:
        print "You can't find anything besides the two doors."
        print "-----------"
        start()

start()