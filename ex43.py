from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print('This scene is not yet configured.  Subclass it and implement enter().')
        exit(1)


class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print('\n---------')
            next_scene_name = current_scene.enter()
            current_scene   = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

    quips = [
        'You died. You kinda suck at this.',
        'Your mom would be proud...if she were smarter.',
        'Such a luser.',
        'I have a small puppy that\'s better at this.'
    ]

    def enter(self):
        print( Death.quips[randint(0,len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print('The Gothons of Planet Percal #25 have invated your ship and blah blah blah...')
        print('You\'re running down the central corridor to the Weapons Armory when')
        print('a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume')
        print('flowing around his hate filled body. He\'s blocking the door to the')
        print('Armory and about to pull a weapon to blast you.')

        action = input('> ')

        if action == "shoot":
            print('You fire your blaster at the Gothon.  You are dead and he eats you.')
            return 'death'
        elif action == "dodge":
            print('You dodge, but bump your head.  You are eaten.')
            return 'death'
        elif action == "tell a joke":
            print('You tell a joke and get away.')
            return 'laser_weapon_armory'
        else:
            print('No idea what that means...')
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print('You do a dive roll, then find a bomb. You must enter the correct 3 digits...')
        code    = '%d%d%d' % (randint(1,9),randint(1,9),randint(1,9))
        guess   = input('[keypad]> ')
        guesses = 0

        while guess != code and guesses < 10:
            print('Bzzzzzed!')
            guesses += 1
            guess = input('[keypad]> ')

        if guess == code:
            print('The container opens and the neutron bomb becomes visible.  You grab it and run to the bridge.')
            return 'the_bridge'
        else:
            print('The lock buzzes one last time, and you die.')
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print('You run into bridge with the bomb. Do you want to throw it or place it?')

        action = input('> ')

        if action == 'throw the bomb':
            print('You stupidly throw the bomb.  It goes off.  You die.')
            return 'death'
        elif action == 'slowly place the bomb':
            print('You place the bomb slowly and run for the escape pod')
            return 'escape_pod'
        else:
            print('No idea what that means...')
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print('There are 5 escape pods.  Which one do you take?')

        good_pod = randint(1,5)
        guess = input('[pod #]> ')

        if int(guess) != good_pod:
            print('You jump into pod %s and hit the eject button.' % guess)
            print('You chose poorly and you die.')
            return 'death'
        else:
            print('You jump into pod %s and it works. Congratulations.' % guess)
            return 'finished'


class Finished(Scene):
    def enter(self):
        print('You won!  Neat!')
        exit(1)


class Map(object):

    scenes = {
        'central_corridor'      : CentralCorridor(),
        'laser_weapon_armory'   : LaserWeaponArmory(),
        'the_bridge'            : TheBridge(),
        'escape_pod'            : EscapePod(),
        'death'                 : Death(),
        'finished'              : Finished()
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map   = Map('escape_pod')
a_game  = Engine(a_map)
a_game.play()
