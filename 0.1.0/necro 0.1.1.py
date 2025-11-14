import tkinter as tk
import ttkbootstrap as ttk
import random

#NOTE: we'll do labels when we start touching on custom tk etc...it's pointless to do now i think

#NO AUTOCLICK HERE

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

knife_up = tk.IntVar(value=0)
rope_up = tk.IntVar(value=0)
bone_shard_up = tk.IntVar(value=0)
bones_up = tk.IntVar(value=0)

worktable_up = tk.IntVar(value=0)

# autoclick setup
auto_click = tk.BooleanVar(value=False)
click_time = 50 # milliseconds

# Set how many resources are needed for each item
pay_for_item = {
    "shovel": {"sticks": 10, "stones": 5},
    "knife": {"sticks": 3, "stones": 1},  #NOTE: ADD THIS!!!!
    "bucket": {"sticks": 20},
    "rope": {"sticks": 6, "knife": 1}, #NOTE: ADD THIS!!!!
    "worktable": {"sticks": 30, "stones": 20}, #NOTE: ADD THIS!!!!
    "bone": {"bones shards": 5}
    # Add other items as needed
}


# Function to simulate digging
def dig():
    dirt_up.set(dirt_up.get() + 1)
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
            update_materials()
            update_news()

def craft_menu():
    if stick_up.get() >= 18 and stone_up.get() >= 8:
        craft_box.pack(side="left", padx=5, pady=5, anchor="nw")
# Bind the changes of resources to the visibility toggle function
stick_up.trace_add("write", lambda *args: craft_menu())
stone_up.trace_add("write", lambda *args: craft_menu())


def auto_click_dirt():
    if auto_click.get():
        dig()
        screen.after(click_time, auto_click_dirt) #NOTE: DO NOT CALL FUNCTION....PASS IT!!!!!

def toggle_click():
    if auto_click.get():
        auto_click.set(False)
        auto_click_button.config(text="Start clicks")
    else:
        auto_click.set(True)
        auto_click_button.config(text="stop click")
        auto_click_dirt()
# Auto-click toggle button
auto_click_button = tk.Button(master=screen, text="Start Auto-Click", command=toggle_click, width=15, height=2)
auto_click_button.pack(side="top", padx=10, pady=10, anchor="nw")

craft_box = tk.Text(master=screen)
# in a text box for easier handling, i can't get any grid to be more than 3x3
shovel_button = tk.Button(master=craft_box, text="Craft shovel", cursor="hand2", command=lambda: crafting("shovel"))
shovel_button.pack(pady=5)
bucket_button = tk.Button(master=craft_box, text="Craft bucket", cursor="hand2", command=lambda: crafting("bucket"))
bucket_button.pack(pady=5)

# Info box for resources
materials_box = tk.Text(master=screen, width=30, height=20)
news_box = tk.Text(master=screen, width=30, height=10)

# Dig button
dirt_button = tk.Button(master=screen, text="Dig Dirt", command=dig, width=10, height=2)
dirt_button.pack(side="top", padx=10, pady=10, anchor="nw")

# Run the main event loop
screen.mainloop()