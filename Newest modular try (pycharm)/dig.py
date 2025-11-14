import tkinter as tk
from variables2 import Materials
from finds import Finds
from recipes import recipe_cost
from helpers import Helpers


class Digging:
    def __init__(self, screen):
        self.materials = Materials(screen)
        self.find = Finds(screen)
        self.checks = Helpers()
        self.screen = screen
        self.recipe = recipe_cost

        # Initialize text boxes
        self.news = tk.Text(master=screen, width=30, height=10)
        self.news.pack(side="left", padx=5, pady=5, anchor="nw")

        self.inventory_screen = tk.Text(master=screen, width=30, height=20)
        self.inventory_screen.pack(side="left", padx=10, pady=10, anchor="nw")

    def dig_finds(self, amount):
        self.checks.inventory(self.materials.dirt_up, amount)
        self.find.find_stick()
        self.find.find_stone()

    def with_shovel(self):
        self.dig_finds(2)
        self.find.find_bone_shards()
        self.update_news()
        self.update_inventory()

    def no_shovel(self):
        self.dig_finds(1)

    def dig(self):
        if self.materials.have_shovel.get():
            self.with_shovel()
        else:
            self.no_shovel()
        self.update_news()
        self.update_inventory()

    def news_lines_config(self, material, message, messages, item=None):
        if material.get() > 0:
            messages.append(message)
        if item is not None:
            stored = self.recipe.get(item)
            if stored is None:
                messages.append(f"You can't craft '{item}' yet")

    def update_news(self):
        self.news.delete("1.0", tk.END)
        messages = []

        self.news_lines_config(self.materials.dirt_up, "You found some dirt!", messages)
        self.news_lines_config(self.materials.stick_up, "You found a few sticks!", messages)
        self.news_lines_config(self.materials.stone_up, "You found a stone!", messages)
        self.news_lines_config(self.materials.shovel_up, "You made a shovel!", messages)
        self.news_lines_config(self.materials.bone_shards_up, "You found bone shards!", messages)
        self.news_lines_config(self.materials.rope_up, "You made some rope!", messages)
        self.news_lines_config(self.materials.knife_up, "You made a knife!", messages)
        self.news_lines_config(self.materials.bucket_up, "You made a bucket!", messages)
        self.news_lines_config(self.materials.crates_up, "You built a crate!", messages)

        self.news.insert("1.0", "\n".join(messages))

    def update_inventory(self):
        self.inventory_screen.delete("1.0", tk.END)
        self.inventory_screen.insert("1.0", f"You dug: {self.materials.dirt_up.get()} dirt")
        if self.materials.stick_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou have {self.materials.stick_up.get()} sticks")
        if self.materials.stone_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou gathered: {self.materials.stone_up.get()} stones")
        if self.materials.shovel_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou made: {self.materials.shovel_up.get()} shovel(s)")
        if self.materials.knife_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou made: {self.materials.knife_up.get()} knife(s)")
        if self.materials.bone_shards_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou have found: {self.materials.bone_shards_up.get()} bone shards")
        if self.materials.rope_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou have: {self.materials.rope_up.get()} ropes\n")

        if self.materials.empty_buckets.get() > 0:
            self.inventory_screen.insert("end", f"{self.materials.empty_buckets.get()} empty bucket(s)\n")
        if self.materials.full_buckets.get() > 0:
            self.inventory_screen.insert("end", f"{self.materials.full_buckets.get()} full bucket(s)\n")
        if self.materials.bucket_space.get() > 0:
            self.inventory_screen.insert("end", f"\nCurrent bucket is {self.materials.bucket_space.get()}% full\n")

        if self.materials.empty_crates.get() > 0:
            self.inventory_screen.insert("end", f"{self.materials.empty_crates.get()} empty crate(s)")
        if self.materials.full_crates.get() > 0:
            self.inventory_screen.insert("end", f"{self.materials.full_crates.get()} full crate(s)")

if __name__ == "__main__":
    screen = None

