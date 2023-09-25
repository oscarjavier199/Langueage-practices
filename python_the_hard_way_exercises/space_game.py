from sys import exit
from random import randint
from textwrap import dedent

#base class
class Scene(object):
    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()

class Death(Scene):
    quips = [
        "You die. You kinda suck at this.",
        "Your Mum would be proud... if she were smarter",
        "Such a luser!", 
        "I have a small kitty that's better at this", 
        "You're worse than your Dad's jokes"
    ]
    
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        
class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
The Gothons of Planet Percal #25 have invaded your ship
and destroyed your entire crwe. You are the last surviving
member and your last mission is to get in the bridge, and
blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons
armoury when a Gothon jumps out, red scaly skin, dark grimmy
teeth, and evil clown costume flowing around his hate 
filled body. He's blocking the door ro rhe Armoury and
about to pull a weapon to blast you"""))
        
        action = input("> ")
        
        if action == "shoot!":
            print(dedent("""
Quick on the draw you yank out your blaster and fire
it at the Gothon. His clown costume is flowing and
moving around his body. which throws off your aim.
Your laser hits his costume but misses him entirely.
This completely ruins his brand new costume his mother
bought him, which makes him fly int an insane rage
and blast you repeatedly in the face until you are
dead. Then he eats you."""))
            return "death"
        
        elif action == "dodge!":
            print(dedent("""
Like a world class boxer you dodge, weave, slip and
slide right as the Gothon's blaster cranks a laser
past your head. In the middle of your artful dodge
your foot slips and you bang your head on the metal
wall and pass out. You wake up shortly after only to
die as the Gothon stomps on your head and eats you."""))
            return "death"
        
        elif action == "tell a joke":
            print(dedent("""
the academy. You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in
the head putting him down, then jump through the
Weapon Armory door."""))
            return "Laser_weapon_armoury"
        else:
            print("DOES NOT COMPUTE!")
            return "Central_Corridor"
        
class LaserWeaponArmoury(Scene):
    def enter(self):
        print(dedent("""
You do a dive roll into the Weapon Armory, crouch and scan
the room for more Gothons that might be hiding. It's dead
quiet, too quiet. You stand up and run to the far side of
the room and find the neutron bomb in its container.
There's a keypad lock on the box and you need the code to
get the bomb out. If you get the code wrong 10 times then
the lock closes forever and you can't get the bomb. The
code is 3 digits."""))
        
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]>")
        guesses = 0
    
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses +=1
            guess = input("[keypad]>")
            
        if guess == code:
            print(dedent('''
The container clicks open and the seal breaks, letting
gas out. You grab the neutron bomb and run as fast as
you can to the bridge where you must place it in the
right spot.
'''))
            return "death"
        
class TheBridge(Scene):
    def enter(self):
        print(dedent('''
You burst onto the Bridge with the netron destruct bomb
48 under your arm and surprise 5 Gothons who are trying to
49 take control of the ship. Each of them has an even uglier
50 clown costume than the last. They haven't pulled their
51 weapons out yet, as they see the active bomb under your
52 arm and don't want to set it off.
'''))
        action = input("> ")
        if action == "throw the bomb":
            print(dedent('''
In a panic you throw the bomb at the group of Gothons
and make a leap for the door. Right as you drop it a
Gothon shoots you right in the back killing you. As
you die you see another Gothon frantically try to
disarm the bomb. You die knowing they will probably
blow up when it goes off.
'''))
            return "escape_pod"
        else:
            print("DOES NOT COMPUTE!")
            return "the bridge"
        
class EscapePod(Scene):
    def enter(self):
        print('''
You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes. It seems
like hardly any Gothons are on the ship, so your run is
clear of interference. You get to the chamber with the
escape pods, and now need to pick one to take. Some of
them could be damaged but you don't have time to look.
There's 5 pods, which one do you take?
''')
        good_pod = randint(1,5)
        guess = input("[pod #]> ")
        
        if int(guess) != good_pod:
            print(dedent('''
You jump into pod {guess} and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body into
jam jelly.
'''))
            return "death"
        else:
            print('''
You jump into pod {guess} and hit the eject button.
The pod easily slides out into space heading to the
planet below. As it flies to the planet, you look
back and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same
time. You won!
''')
            return "finished"
        
class Finished(Scene):
    def enter(self):
        print("Yu won! good jon.")
        return "finished"
            
class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armoury': LaserWeaponArmoury(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        