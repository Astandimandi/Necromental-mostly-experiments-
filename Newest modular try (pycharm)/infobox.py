# Function to update the news box
import tkinter as tk

from variables import Materials
from recipes import recipe_cost


class Infobox:
    def __init__(self, screen):
        self.material = Materials(screen)
        self.recipe = recipe_cost
        self.screen = screen

        self.news = tk.Text(master=screen, width=30, height=10)
        self.inventory_screen = tk.Text(master=screen, width=30, height=20)

    def news_lines_config(self, material, message, messages, item=None, recipe=None):
        if material.get() > 0:
            messages.append(message)
        if item is not None and recipe is not None:
            stored = recipe.get(item)
            if stored is None:
                messages.append(f"You can't craft '{item}' yet")

    def update_news(self):
        print("Updating news...")
        self.news.delete("1.0", tk.END)
        messages = []

        self.news_lines_config(self.material.dirt_up, "You found some dirt!", messages)
        self.news_lines_config(self.material.stick_up, "You found a few sticks!", messages)
        self.news_lines_config(self.material.stone_up, "You found a stone!", messages)
        self.news_lines_config(self.material.shovel_up, "You made a shovel!", messages)
        self.news_lines_config(self.material.bone_shards_up, "You found bone shards!", messages)
        self.news_lines_config(self.material.rope_up, "You made some rope!", messages)
        self.news_lines_config(self.material.knife_up, "You made a knife!", messages)
        self.news_lines_config(self.material.bucket_up, "You made a bucket!", messages)
        self.news_lines_config(self.material.crates_up, "You built a crate!", messages)

        self.news.insert("1.0", "\n".join(messages))
        self.news.delete("1.0", tk.END)

    def update_inventory(self):
        print("Updating stuff...")
        self.inventory_screen.delete("1.0", tk.END)
        self.inventory_screen.insert("1.0", f"You dug: {self.material.dirt_up.get()} dirt")
        if self.material.stick_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou have {self.material.stick_up.get()} sticks")
        if self.material.stone_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou gathered: {self.material.stone_up.get()} stones")
        if self.material.shovel_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou made: {self.material.shovel_up.get()} shovel(s)")
        if self.material.knife_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou made: {self.material.knife_up.get()} knife(s)")
        if self.material.bone_shards_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou have found: {self.material.bone_shards_up.get()} bone shards")
        if self.material.rope_up.get() >= 1:
            self.inventory_screen.insert("end", f"\nYou have: {self.material.rope_up.get()} ropes\n")

        if self.material.empty_buckets.get() > 0:
            self.inventory_screen.insert("end", f"{self.material.empty_buckets.get()} empty bucket(s)\n")
        if self.material.full_buckets.get() > 0:
            self.inventory_screen.insert("end", f"{self.material.full_buckets.get()} full bucket(s)\n")
        if self.material.bucket_space.get() > 0:
            self.inventory_screen.insert("end", f"\nCurrent bucket is {self.material.bucket_space.get()}% full\n")

        if self.material.empty_crates.get() > 0:
            self.inventory_screen.insert("end", f"{self.material.empty_crates.get()} empty crate(s)")
        if self.material.full_crates.get() > 0:
            self.inventory_screen.insert("end", f"{self.material.full_crates.get()} full crate(s)")

        self.inventory_screen.delete("1.0", tk.END)

if __name__ == "__main__":
    screen = None