#necro 0.1.3
import tkinter as tk
import ttkbootstrap as ttk
import random

#NOTE: SHOVEL BUTTON APPEARs AT THE START

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
bone_knife_up = tk.IntVar(value=0)   #ADDED
rope_up = tk.IntVar(value=0)
bone_shard_up = tk.IntVar(value=0)   #ADDED
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
    "rope": {"sticks": 6}, #NOTE: ADD THIS!!!! i want to use knife to make these
    "worktable": {"sticks": 30, "rope": 5, "stones": 5}, # ADD #NOTE: ADD THIS!!!!
    "bone": {"buckets": 1, "bones shards": 5},
    "crates": {"sticks": 20, "rope": 4}, # ADD
    "skeleton": {"buckets": 1, "bones shards": 25, "dirt": 10},
    # Add other items as needed
}


# BASIC DIGGING FUNCTION
def with_shovel():
    if have_shovel.get():
        dirt_up.set(dirt_up.get() + 3)
        find_bone_shard()

def no_shovel():
    dirt_up.set(dirt_up.get() + 1)

def dig():
    if have_shovel.get():
        with_shovel()
        print("Digging with shovel")
    else:
        no_shovel()
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

def find_bone_shard():
    if dirt_up.get() > 1:
        if random.random() < 0.1:
            bone_shard_up.set(bone_shard_up.get() + 1)

# INFO BOXES SETUP AND UPDATES
def update_news():
    news_box.config(state=tk.NORMAL)
    news_box.delete("1.0", tk.END)
    messages = []
    if dirt_up.get() > 0:
        messages.append("You found some dirt!")
    if stick_up.get() > 0:
        messages.append("You found a few sticks!")
    if stone_up.get() > 0:
        messages.append("You found a stone!")
    if shovel_up.get() > 0:
        messages.append("You're using the shovel!") #NOTE: THIS IS MORE OF A WORK AROUND AND DOESN'T REALLY DO WHAT I WANT, BUT IT'S STILL WORKING OUT PRETTY WELL, JUST BEAR IN MIND THIS NOW UPDATES TO TELL YOU IF YOU'RE USING AN ITEM, NOT THAT YOU HAVE IT
# this can become superfluous, i'm trying to see how i want to organize this
    if bucket_up.get() > 0:
        messages.append("You HUHU'D the bucket!")
    if bone_shard_up.get() > 0:
        messages.append("You found some bone shards!")
    if bone_knife_up.get() > 0:
        messages.append("You HUHU'D the knife!")
    news_box.insert("end", "\n".join(messages))
    news_box.config(state=tk.DISABLED)
    news_board()

def update_materials():
    materials_box.delete("1.0", tk.END)  
    materials_box.insert("1.0", f"You have dug: {dirt_up.get()} dirt") 
    if stick_up.get() >= 1:
        materials_box.insert("end", f"\nYou have {stick_up.get()} sticks") 
    if stone_up.get() >= 1:
        materials_box.insert("end", f"\nYou gathered: {stone_up.get()} stones")
    if shovel_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {shovel_up.get()} shovels")
    if bucket_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {bucket_up.get()} buckets")
    if bone_shard_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {bone_shard_up.get()} bone shards")
    if bone_knife_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {bone_knife_up.get()} bone knife")
    materials_board()

def update_equipment():
    if shovel_up.set(shovel_up.get() >= 1) or bucket_up.set(bucket_up.get() >= 1):
        equipment_box.pack(side="bottom", padx=10, pady=10, anchor="s")
shovel_up.trace_add("write", lambda *args: update_equipment())
bucket_up.trace_add("write", lambda *args: update_equipment())

# this box is entirely superfluous now, as i figured out how to update the other boxes, but i'm thinking of keeping it for later, just in case

def news_board():
    if dirt_up.get() > 0 or stick_up.get() > 0 or stone_up.get() > 0:
        news_box.pack(side="right", padx=5, pady=5, anchor="n")
    else:
        news_box.pack_forget()

def materials_board():
    if dirt_up.get() > 0 or stick_up.get() > 0 or stone_up.get() > 0:
        materials_box.pack(side="right", padx=10, pady=10, anchor="n")
    else:
        materials_box.pack_forget()

def equipment_board():
    if shovel_up.get() > 0 or bucket_up.get() > 0:
        equipment_box.pack(side="bottom", padx=10, pady=10, anchor="s")
    else:
        equipment_box.pack_forget()
shovel_up.trace_add("write", lambda *args: equipment_board())


# CRAFTING MENU AND LOGIG
def crafting(item_name):
    raw_materials = pay_for_item.get(item_name)
    if not raw_materials:
        return  # Item not found
    if item_name == "shovel":  # these refer to items in pay_for_item dict
        if (stick_up.get() >= raw_materials.get("sticks", 0) and 
            stone_up.get() >= raw_materials.get("stones", 0)):   # this is where we count resources
            stick_up.set(stick_up.get() - raw_materials.get("sticks", 0))
            stone_up.set(stone_up.get() - raw_materials.get("stones", 0))   # this is where we pay for the item
            shovel_up.set(shovel_up.get() + 1)  # add item
            print("have shovel")
            update_equipment() #NOTE: THIS IS WHERE WHE CORRECTLY UPDATE CRAFTING AND EQUIPMENT
            update_materials()
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
            update_equipment()  # CALL THESE SPECIFICALLY AFTER EACH ITEM, IT'S TOO GENERIC OTHERWISE


# TOGGLES FOR MENUS AND BUTTONS
def craft_menu():  # this is literally just to toggle the menu on when you have enough resources
    if stick_up.get() >= 19 and stone_up.get() >= 9:
        craft_box.pack(side="left", padx=5, pady=5, anchor="nw")
# Bind visibility of crafitng menu to amount of sticks and stones (or whatever variable)
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

def toggle_shovel():
    if have_shovel.get():
        have_shovel.set(False)  # Unequip the shovel
        equip_shovel.config(text="Not holding shovel") # this could just be a toggle with no text, we'll see
        print("Shovel unequipped")
        update_news()
    else:
        have_shovel.set(True)  # Equip the shovel
        equip_shovel.config(text="Holding shovel")
        print("Shovel equipped")
        update_news()
    update_equipment() 



# Auto-click toggle button
auto_click_button = tk.Button(master=screen, text="Start Auto-Click", command=toggle_click, width=15, height=2)
auto_click_button.pack(side="top", padx=10, pady=10, anchor="nw")

craft_box = tk.Text(master=screen)
# in a text box for easier handling, i can't get any grid to be more than 3x3
shovel_button = tk.Button(master=craft_box, text="Craft shovel", cursor="hand2", command=lambda: crafting("shovel"))
shovel_button.pack(pady=5)

# Equip shovel button
equipment_box = tk.Text(screen, height=10, width=40, state=tk.DISABLED)
equip_shovel = tk.Button(master=equipment_box, text="Sans shovel", command=toggle_shovel, width=10, height=2)
equip_shovel.pack(side="left", padx=10, pady=10, anchor="nw")

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