import random
from variables2 import Materials
from helpers import Helpers

screen = None

class Finds:
    def __init__(self, screen):
        self.materials = Materials(screen)
        self.checks = Helpers()
        self.screen = screen

    def find_stick(self):
        if self.materials.dirt_up.get() >= 8:
            self.checks.inventory(self.materials.stick_up, 2)
            print("Found stick")

    def find_stone(self):
        if self.materials.dirt_up.get() >= 30:
            self.checks.inventory(self.materials.stone_up, 1)
            print("Found stone")

    def find_bone_shards(self):
        if self.materials.have_shovel.get() and self.materials.dirt_up.get() > 30:
            if random.random() < 0.05:
                self.checks.inventory(self.materials.bone_shards_up, 1)
                print("Found bone shards")


if __name__ == "__main__":
    screen = None



'''
    # Initialize the Diggings class with the screen
    diggings = Diggings(screen)

    # Example usage:
    diggings.find_stick()
    diggings.find_stone()
    diggings.find_bone_shards()

    # Example inventory updates
    diggings.inventory(diggings.materials.dirt_up, 1)
    diggings.inventory(diggings.materials.stick_up, 1)
    diggings.inventory(diggings.materials.stone_up, 1)
    diggings.inventory(diggings.materials.bone_shards_up, 1)
'''


'''
and random.random() < 0.15
 and random.random() < 0.13

Dependency Injection: By initializing Boards (or any class) inside the __init__ 
method of another class (Diggings in this case), you provide it with the dependencies it needs 
(e.g., screen and materials)


def storage2(action):
    storage_actions = {
        "fill bucket": fill_bucket,
        "empty bucket": empty_bucket,
        "fill crate": fill_crate
    }
    if action in storage_actions:
        storage_actions[action]()
    else:
        news_box.insert("1.0", f"Unknown action: {action}\n")

def dig_finds(amount, materials):
    inventory(materials.dirt_up, amount)
    find_stick()
    find_stone()

# Example call
dig_finds(10, materials)


    def count_check(self, var, amount, description="Item"):
        before = var.get()  # Get the current value before the update
        self.inventory(var, amount)  # Update the inventory
        after = var.get()  # Get the value after the update

        # Print debug message
        if after == before + amount:
            print(f"{description} updated successfully: {before} -> {after}")
        else:
            print(f"Failed to update {description}: {before} -> {after}")

'''