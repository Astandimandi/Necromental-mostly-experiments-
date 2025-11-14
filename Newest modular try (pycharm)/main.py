# dummy script for calculations, functions, messing around, etc without making it pretty

#NOTE: VARIABLES FULLY IMPORTED!!!!!
#NOTE RECIPES FULLY IMPORTED!!!!!
#NOTE: FIND CHANCES INTEGRATED!!!!!!!!
#NOTE: COULD IMPORT:
    #CRAFTING STUFF (THOUGH WE'LL SEE)
        # CRAFTING FUNCTON
        # CRAFTING UPDATES
        # RECIPE BOARD
    # INVENTORY BOARD (THOUGH I THINK THAT SHOULD BE IN ITS OWN MAIN SCRIPT (THERE'S SO MUCH HERE)
    # NEWS AND DIALOGUE SHOULD BE SEPARATE, BUT I THINK IT'LL BE A MESS TO DO, SAME AS INVENTORY
# NOTE: WHEN REDOING VENV FROM THE START, YOU NEED TO PIP INSTALL EVERYTHING (IT'S LIKE STARTING FRESH)

import tkinter as tk
import ttkbootstrap as ttk

from variables2 import Materials
from recipes import recipe_cost
from helpers import Helpers
from dig import Digging
# NOTE: SEE ABOUT HAVING VARIABLES NOT AS A SINGLETON, I DON'T UNDERSTAND WHY IT WONT WORK AS A SIMPLE CLASS

# Window setup
screen = ttk.Window(themename="darkly")
screen.title("Necromental")
screen.geometry("1100x900")

materials = Materials(screen)
checks = Helpers()
info = Digging(screen)


def knife_use(amount):
    checks.inventory(materials.rope_up, amount)
    info.update_news()
    info.update_inventory()

def with_knife():
    if materials.have_knife.get():
        knife_use(1)

def no_knife():
    message = []
    if not materials.have_knife.get():
        message.append("You need a knife first!\n")
        info.news.insert("1.0", "\n".join(message))


def use_bucket():
    checks.toggles(materials.have_bucket)
    equip_bucket_text = "Storing dirt" if materials.have_bucket.get() else "Empty the bucket"
    equip_bucket.config(text=equip_bucket_text)

def fill_bucket():
    if not materials.have_bucket.get():
        info.news.insert("1.0", "You need a bucket first!\n")
        return
    if materials.empty_buckets.get() > 0:
        capacity = materials.filled_bucket - materials.bucket_space.get()
        dirt_in = min(capacity, 50)
        stored_dirt = materials.dirt_up.get()
        dirt_in = min(dirt_in, stored_dirt)

        if dirt_in > 0:
            checks.inventory(materials.dirt_up, - dirt_in)
            materials.bucket_space.set(materials.bucket_space.get() + dirt_in)

            if materials.bucket_space.get() == 100:  # if the bucket is full
                materials.empty_buckets.set(materials.empty_buckets.get() - 1)
                materials.full_buckets.set(materials.full_buckets.get() + 1)
                materials.bucket_space.set(0)
            info.update_inventory()
            info.update_news()
        else:
            info.news.insert("1.0", "You don't have enough dirt!\n")
    else:
        info.news.insert("1.0", "You need an empty bucket!\n")

def empty_bucket():
    pass

def crate_storage():
    if materials.crates_up.get() > 0 and materials.empty_crates.get() > 0:
        materials.have_crate.set(True)

def fill_crate():
    if not materials.have_crate.get():
        info.news.insert("1.0", "You dont' have crates!\n")
        return
    if materials.empty_crates.get() <= 0:
        if not materials.have_crate.get():
            crate_storage()
        info.news.insert("1.0", "No EMPTY crates available!\n")
        return
    if materials.crate_space.get() >= materials.filled_crate:
        info.news.insert("1.0", "Crate is full!\n")
        return

    materials.crate_space.set(materials.crate_space.get() + 1)
    materials.full_buckets.set(materials.full_buckets.get() - 1)

    if materials.crate_space.get() == 4:
        materials.empty_crates.set(materials.empty_crates.get() - 1)
        materials.full_crates.set(materials.full_crates.get() + 1)
        materials.crate_space.set(0)
        info.news.insert("1.0", "You have a full crate!\n")
        info.update_inventory()
        info.update_news()
    else:
        info.news.insert("1.0", "Crate can store " + str(4 - materials.crate_space.get()) + " more buckets.\n")

def storage(action):
    if action == "fill bucket":
        if materials.have_bucket.get():
            fill_bucket()
        else:
            info.news.insert("1.0", "You need to equip a bucket first!\n")
    if action == "empty bucket":
        empty_bucket()
    if action == "fill crate":
        crate_storage()
        fill_crate()


def crafting(item):
    stored = recipe_cost.get(item)
    messages = []

    if not stored:
        messages.append(f"Couldn't craft '{item}'!")
        info.news.insert("1.0", "\n".join(messages))
        return

    if materials.stick_up.get() >= stored.get("sticks", 0) and materials.stone_up.get() >= stored.get("stones", 0) and materials.rope_up.get() >= stored.get("rope", 0):
        checks.inventory(materials.stick_up, -stored.get("sticks", 0))
        checks.inventory(materials.stone_up, -stored.get("stones", 0))
        checks.inventory(materials.rope_up, -stored.get("rope", 0))

        if item == "shovel":
            checks.inventory(materials.shovel_up, 1)
            messages.append("You made a shovel!\n")
        elif item == "knife":
            checks.inventory(materials.knife_up, 1)
            messages.append("You forged a knife!\n")
        elif item == "rope":
            if materials.have_knife.get():
                checks.inventory(materials.rope_up, 1)  # Increment rope count
                messages.append("You made rope!\n")
            else:
                no_knife()
                messages.append("You need a knife to make this!\n")
                return
        elif item == "bucket":
            checks.inventory(materials.bucket_up, 1)
            materials.empty_buckets.set(materials.empty_buckets.get() + 1)  # Increase empty bucket count
            messages.append("\nYou crafted a bucket!\n")
            messages.append("You can put stuff in here!\n")
        elif item == "crate":
            checks.inventory(materials.crates_up, 1)
            materials.empty_crates.set(materials.empty_crates.get() + 1)
            messages.append("You built a crate!\n")
        info.update_inventory()
    else:
        messages.append(f"Not enough resources to craft '{item}'!\n")

    info.news.insert("1.0", "\n".join(messages))

def update_recipe(item):
    stored = recipe_cost.get(item)
    if not stored:
        recipe_box.config(state=tk.NORMAL)
        recipe_box.delete("1.0", tk.END)
        recipe_box.config(state=tk.DISABLED)
        return

    infos = f"{item}: \nSticks: {stored.get('sticks', 0)}\nStones: {stored.get('stones', 0)}\nRope: {stored.get('rope', 0)}\n"
    recipe_box.config(state=tk.NORMAL)
    recipe_box.delete("1.0", tk.END)
    recipe_box.insert("end", infos)
    recipe_box.config(state=tk.DISABLED)

    craft_shovel.pack_forget()
    craft_knife.pack_forget()
    craft_rope.pack_forget()
    craft_bucket.pack_forget()

    if item == "shovel":
        craft_shovel.pack()
    elif item == "knife":
        craft_knife.pack()
    elif item == "rope":
        # with_knife()
        craft_rope.pack()
    elif item == "bucket":
        craft_bucket.pack()
    elif item == "crate":
        craft_crate.pack()


def hold_knife():
    checks.toggles(materials.have_knife)
    equip_knife.config(text="Using knife" if materials.have_knife.get() else "Grab knife")

def hold_shovel():
    checks.toggles(materials.have_shovel)
    equip_shovel.config(text="Using shovel" if materials.have_shovel.get() else "Grab shovel")

def autoclick():
    if materials.dev_click.get():
        info.dig()
        screen.after(materials.click_time, autoclick)


def use_click():
    checks.toggles(materials.dev_click)
    auto_button.config(text="Stop clicks" if materials.dev_click.get() else "Start clicks")
    if materials.dev_click.get():
        autoclick()


dirt_button = tk.Button(master=screen, text="Dig Dirt", command=info.dig, width=10, height=2)
dirt_button.pack(side="top", padx=10, pady=10, anchor="nw")

auto_button = tk.Button(master=screen, text="Start clicks", command=use_click, width=10, height=2)
auto_button.pack(side="bottom", padx=10, pady=10, anchor="se")

# EQUIP BUTTONS
equip_shovel = tk.Button(master=screen, text="Grab shovel", font=("Arial", 12), command=hold_shovel, width=10, height=2)
equip_shovel.pack(side="right", padx=10, pady=10)
equip_knife = tk.Button(master=screen, text="Grab knife", font=("Arial", 14), command= hold_knife)
equip_knife.pack(side="right", padx=10, pady=10)
equip_bucket = tk.Button(master=screen, text = "Grab bucket", font=("Arial", 12), command=use_bucket, width=10, height=2)
equip_bucket.pack(side="right", padx=10, pady=10)

# CRAFTING MAIN INTERACTIONS
    # recipe screen
recipe_box = tk.Text(master=screen, height=10, width=20, state=tk.DISABLED)
recipe_box.pack(side="bottom", padx=10, pady=10, anchor="w")
    # Crafting buttons
craft_knife = tk.Button(master=screen, text="Craft Knife", font=("Arial", 12), command=lambda: crafting("knife"))
craft_shovel = tk.Button(master=screen, text="Craft Shovel", font=("Arial", 12), command=lambda: crafting("shovel"))
craft_bucket = tk.Button(master=screen, text="Craft Bucket", font=("Arial", 12), command=lambda: crafting("bucket"))
craft_rope = tk.Button(master=screen, text="Craft Rope", font=("Arial", 12), command=lambda: crafting("rope"))
craft_crate = tk.Button(master=screen, text="Craft Crate", font=("Arial", 12), command=lambda: crafting("crate"))

crafting_items = ("knife", "rope", "shovel", "bucket", "crate")
    # drop down menu
pick_craft = ttk.Combobox(master=screen, state="readonly", width=20)
pick_craft.config(width=10)
pick_craft.config(values=crafting_items)
pick_craft.bind("<<ComboboxSelected>>", lambda event: update_recipe(pick_craft.get()))
pick_craft.pack(side="left", padx=10, pady=10, anchor="sw")

fill_in = tk.Button(master=screen, text="Fill Bucket",  font=("Arial", 12), command=lambda: storage("fill bucket"))
empty_out = tk.Button(master=screen, text="Empty Bucket",  font=("Arial", 12), command=lambda: storage("empty bucket")) # NOTE: STILL NEED TO FIGURE OUT FUNCTIONALITY (IF NEEDED AT ALL) --> MAYBE FOR GRAVES?
fill_in.pack(side="bottom", padx=10, pady=10, anchor="sw")
#empty_out.pack(side="left", padx=10, pady=10, anchor="w")

in_crate = tk.Button(master=screen, text="Fill Crate",  font=("Arial", 12), command=lambda: storage("fill crate"))
in_crate.pack(side="bottom", padx=10, pady=10, anchor="sw")

screen.mainloop()