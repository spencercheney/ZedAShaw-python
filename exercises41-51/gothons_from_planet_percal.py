##This is a simple text-based game where the player is stuck in a spaceship
##that was taken over by aliens and is trying to escape

from sys import exit
from random import randint

#A base class for all of the different rooms and scenes
class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

#Controls the movement of the player from room to room
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n---------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

#The scene the player will encounter when they die
class Death(Scene):
    
    quips = [
        "You're the saddest bunch I've ever met.",
        "So pack up, go home, you're through",
        "How can I...make a man...out of you."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

#The first scene the player will see. The player will encounter the evil Gothon alien
#and have to find a way to defeat it.
class CentralCorridor(Scene):
    
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "Your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruction bomb from the Weapons Armory,"
        print "put it in the bridge, and blow up the ship after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, dressed like a evil, "
        print "creepy, hate filled clown. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown suit is flowing and moving around his body, which throws"
            print "off your aim. Your laser goes through his suit but misses him entirely. This"
            print "completely ruins his brand new suit his mother bought him, which"
            print "makes him fly into a rage and blast you repeatedly in the face until"
            print "you are dead. Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artistic dodge you foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn the Gothon language in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't control himself."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, and then you jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

#in this scene the user will have to figure out a random 3 digit code
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. Ther's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits."
        code = "%d%d%d" %(randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print "BZZZZEDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting has out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'

        else:
            print "The lock buzzes one last time and then you hear the"
            print "sickening soung of the mechanism being fused together."
            print "You decide to sit there and enjoy a peaceful death,"
            print "as the Gothons blew up your ship with a missle fired from their ship"
            return 'death'

#the player discovers 5 gothans and has to figure out how to place the bomb and 
#escape the evil aliens
class TheBridge(Scene):
    
    def enter(self):
        print "You burst onto the Bridge holding the neutron destruction bomb"
        print "under your arm and suprising 5 Gothons who are trying to"
        print "take control of the ship. Each of them have an even uglier clown"
        print "suit then the previous one. Gothan's are smart creatures and"
        print "when they see the active bomb under your arm they holster their"
        print "blasters because they don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door. As soon as the Gothons see"
            print "you release the bomb one shoots you in the back, killing you."
            print "As your dieing you see another Gothan franctically trying to"
            print "disarm the bomb. You die a hero knowing that the bomb will go"
            print "off, killing all of the Gothans."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to seat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then walk back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to th escape pod to"
            print "get off this tin can."
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'

#the player makes it to the escape pods but has to guess which ones are damaged
#and which one is safe to take
class EscapePod(Scene):
    
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the scape pod before the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now you need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." %guess
            print "The pod escapes out into the spaces, but then"
            print "implodes as the hull ruptures and crushes you body"
            print "in the process."
            return 'death'

        else:
            print "You jump into pod %s and hit th eject button." %guess
            print "The pod easily slides out into space, heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode and explode like a"
            print "bright star, taking out the Gothon ship next to it"
            print "at the same time. You Won!!"

            return 'finished'

#stores all the scenes into a dictionary and provides
#functions to move from room to room
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }    

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()