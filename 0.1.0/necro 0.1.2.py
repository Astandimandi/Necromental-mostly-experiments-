#necro 0.1.2
import tkinter as tk
import ttkbootstrap as ttk
import random


# Window setup
screen = ttk.Window(themename="darkly")
screen.title("Necromental")
screen.geometry("800x600")

# tk variables to keep count
dirt_up = tk.IntVar(value=0)
stick_up = tk.IntVar(value=0)
stone_up = tk.IntVar(value=0)
shovel_up = tk.IntVar(value=0)
bucket_up = tk.IntVar(value=0)

    #NOTE: ADD ALL THESE!!!!
knife_up = tk.IntVar(value=0)
bone_knife_up = tk.IntVar(value=0)
rope_up = tk.IntVar(value=0)
bone_shard_up = tk.IntVar(value=0)
bones_up = tk.IntVar(value=0)

worktable_up = tk.IntVar(value=0)

# autoclick setup
auto_click = tk.BooleanVar(value=False)
click_time = 50 # milliseconds


# EQUIPMENT TOGGLES
have_shovel = tk.BooleanVar(value=False)
#have_bucket = tk.BooleanVar(value=False)
#have_knife = tk.BooleanVar(value=False)

# Set how many resources are needed for each item
pay_for_item = {
    "shovel": {"sticks": 10, "stones": 5},
    "knife": {"sticks": 3, "stones": 1},
    "bone knife": {"bone shards": 3, "stones": 2, "rope": 1},  #NOTE: ADD THIS!!!!
    "bucket": {"sticks": 20},
    "rope": {"sticks": 6, "knife": 1}, #NOTE: ADD THIS!!!!
    "worktable": {"sticks": 30, "stones": 20}, #NOTE: ADD THIS!!!!
    "bone": {"buckets": 1, "bones shards": 5},
    "skeleton": {"buckets": 1, "bones shards": 25, "dirt": 10},
    # Add other items as needed
}


# BASIC DIGGING FUNCTION
def dig():
    if have_shovel.get():
        dirt_up.set(dirt_up.get() + 3)  # Extra dirt if holding shovel
        if dirt_up.get() <= 3:
            if random.random() < 0.3:
                bone_shard_up.set(bone_shard_up.get() + 1)  # and you can start finding bone shards
    else:
        dirt_up.set(dirt_up.get() + 1)  # Regular dirt without shovel
    find_stone()
    find_stick()
    update_materials()
    update_news()

def find_stone():
    if dirt_up.get() >= 30:
        if random.random() < 0.13:
            stone_up.set(stone_up.get() + 1)

def find_stick():
    if dirt_up.get() >= 10:
        if random.random() < 0.10:
            stick_up.set(stick_up.get() + 2)


# INFO BOXES SETUP AND UPDATES
def update_news():
    news_box.config(state=tk.NORMAL)
    news_box.delete("1.0", tk.END)
    messages = []
    if stick_up.get() > 0:
        messages.append("You found a few sticks!")
    if stone_up.get() > 0:
        messages.append("You found a stone!")
    if shovel_up.get() > 0:
        messages.append("You made a shovel!")
    if bucket_up.get() > 0:
        messages.append("You made a bucket!")
    if bone_shard_up.get() > 0:
        messages.append("You found some bone shards!")
    if bone_knife_up.get() > 0:
        messages.append("You made a knife!")
    news_box.insert("end", "\n".join(messages))
    news_box.config(state=tk.DISABLED)

def update_materials():
    materials_box.config(state=tk.NORMAL)
    materials_box.delete("1.0", tk.END)
    messages = []
    if dirt_up.get() >= 1:
        messages.append(f"You have: {dirt_up.get()} dirt")
    if stick_up.get() >= 1:
        messages.append(f"You have: {stick_up.get()} sticks")
    if stone_up.get() >= 1:
        messages.append(f"You have: {stone_up.get()} stones")
    if shovel_up.get() >= 1:
        messages.append(f"You have: {shovel_up.get()} shovels")
    if bucket_up.get() >= 1:
        messages.append(f"You have: {bucket_up.get()} buckets")
    if bone_shard_up.get() >= 1:
        messages.append(f"You have: {bone_shard_up.get()} bone shards")
    if bone_knife_up.get() >= 1:
        messages.append(f"You have: {knife_up.get()} knives")
    materials_box.insert("end", "\n".join(messages))
    materials_box.config(state=tk.DISABLED)

def news_board():
    if dirt_up.get() > 0:
        news_box.pack(side="right", padx=5, pady=5, anchor="n")
        news_box.config(state=tk.DISABLED)
    else:
        news_box.pack_forget()
dirt_up.trace_add("write", lambda *args: news_board())
# this is to make the info box appear only if there is dirt (so button click)

def materials_board():
    if dirt_up.get() > 0:
        materials_box.pack(side="right", padx=10, pady=10, anchor="n")
        materials_box.config(state=tk.DISABLED)
    else:
        materials_box.pack_forget()
dirt_up.trace_add("write", lambda *args: materials_board())
# same here


# CRAFTING MENU AND LOGIG
def crafting(item_name):
    raw_materials = pay_for_item.get(item_name)
    if not raw_materials:
        return  # Item not found
    if item_name == "shovel":  # these refer to items in pay_for_item dict
        if (stick_up.get() >= raw_materials.get("sticks", 0) and 
            stone_up.get() >= raw_materials.get("stones", 0)):   # this is where we count resources
            stick_up.set(stick_up.get() - raw_materials.get("sticks", 0))
            stone_up.set(stone_up.get() - raw_materials.get("stones", 0))   # this sis where we pay for the item
            shovel_up.set(shovel_up.get() + 1)  # add item
            print("have shovel")
    if item_name == "bucket":
        if (stick_up.get() >= raw_materials.get("sticks", 0)):
            stick_up.set(stick_up.get() - raw_materials.get("sticks", 0))
            bucket_up.set(bucket_up.get() + 1)
            print("have bucket")
    if item_name == "bone":  # FIGURE BUTTON!!!!
        if (bone_shard_up.get() >= raw_materials.get("shards", 0)):
            bone_shard_up.set(bone_shard_up.get() - raw_materials.get("shards", 0))
            bones_up.set(bones_up.get() + 1)
            print("have bone")
    if item_name == "bone knife":  # FIGURE BUTTON!!!!
        if bone_shard_up.get() >= raw_materials.get("shards", 0) and stone_up.get() >= raw_materials.get("stones", 0) and rope_up.get() >= raw_materials.get("rope", 0):
            bone_shard_up.set(bone_shard_up.get() - raw_materials.get("shards", 0))
            stone_up.set(stone_up.get() - raw_materials.get("stones", 0))
            rope_up.set(rope_up.get() - raw_materials.get("rope", 0))
            knife_up.set(knife_up.get() + 1)
            print("have bone knife") 
            update_materials()
            update_news()

def craft_menu():  # thi is literally just to toggle the menu on when you have enough resources
    if stick_up.get() >= 18 and stone_up.get() >= 8:
        craft_box.pack(side="left", padx=5, pady=5, anchor="nw")
# Bind visibility of crafitng menu to amount of sticks and stones (or whatever variable)
stick_up.trace_add("write", lambda *args: craft_menu())
stone_up.trace_add("write", lambda *args: craft_menu())


def auto_click_dirt():
    if auto_click.get():
        dig()
        screen.after(click_time, auto_click_dirt) #NOTE: DO NOT CALL FUNCTION....PASS IT!!!!!


# BUTTON TOGGLES
def toggle_click():
    if auto_click.get():
        auto_click.set(False)
        auto_click_button.config(text="Start clicks")
    else:
        auto_click.set(True)
        auto_click_button.config(text="stop click")
        auto_click_dirt()

def toggle_shovel():
    if have_shovel.get():
        have_shovel.set(False)  # Unequip the shovel
        equip_shovel.config(text="Not holding shovel")
        print("Shovel unequipped")
    else:
        have_shovel.set(True)  # Equip the shovel
        equip_shovel.config(text="Holding shovel")
        print("Shovel equipped")


# Auto-click toggle button
auto_click_button = tk.Button(master=screen, text="Start Auto-Click", command=toggle_click, width=15, height=2)
auto_click_button.pack(side="top", padx=10, pady=10, anchor="nw")

craft_box = tk.Text(master=screen)
# in a text box for easier handling, i can't get any grid to be more than 3x3
shovel_button = tk.Button(master=craft_box, text="Craft shovel", cursor="hand2", command=lambda: crafting("shovel"))
shovel_button.pack(pady=5)
# Equip shovel button
equip_shovel = tk.Button(master=screen, text="Not holding shovel", command=toggle_shovel, width=10, height=2)
equip_shovel.pack(side="top", padx=10, pady=10, anchor="nw")

bucket_button = tk.Button(master=craft_box, text="Craft bucket", cursor="hand2", command=lambda: crafting("bucket"))
bucket_button.pack(pady=5)
#in_bucket_button = tk.Button(master=screen, text="Not holding bucket", command=toggle_bucket, width=10, height=2)
#in_bucket_button.pack(side="top", padx=10, pady=10, anchor="nw")

# Info box for resources
materials_box = tk.Text(master=screen, width=30, height=20)
news_box = tk.Text(master=screen, width=30, height=10)

# Dig button
dirt_button = tk.Button(master=screen, text="Dig Dirt", command=dig, width=10, height=2)
dirt_button.pack(side="top", padx=10, pady=10, anchor="nw")

# Run the main event loop
screen.mainloop()