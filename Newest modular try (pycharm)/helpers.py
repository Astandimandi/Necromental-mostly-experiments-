# helper functions that might get filled out more later, we'll see

from variables2 import Materials

screen = None

class Helpers:
    def __init__(self):
        self.materials = Materials(screen)

    def inventory(self, material, amount):
        material.set(material.get() + amount)

    def toggles(self, material):
        material.set(not material.get())

if __name__ == "__main__":
    screen = None



'''
When Should You Use Each?

If you want Materials to be created specifically for each instance of Diggings, use the approach in Diggings, where you create Materials inside the __init__ method.
If you want multiple classes to share the same instance of Materials, use the approach in Helpers, where you pass an already created Materials instance into the class.

In short:

If Materials is unique per object, create it in the class (Diggings style).
If Materials is shared, pass it as a parameter (Helpers style).
'''