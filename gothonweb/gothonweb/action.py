from random import randrange


#this will create a rock, paper, scissors based fighting system
#blaster beats knive, knive beats dodge, dodge beats blaster
class Action(object):
    def __init__(self):
        Self = self
              

    def Blaster(self):

        gothon_action = randrange(3)            #0 = blaster, 1 = knive, 2 = dodge
        if(gothon_action == 2):
            victory = False
        else:
            victory = True

        return victory

    def Knive(self):
        gothon_action = randrange(3)

        if (gothon_action == 0):
            victory = False
        else:
            victory = True

        return victory

    def Dodge(self):
        gothon_action = randrange(3)

        if (gothon_action == 1):
            victory = False
        else:
            victory = True

        return victory

FIGHT = Action()