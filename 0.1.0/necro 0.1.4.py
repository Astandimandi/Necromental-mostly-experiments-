#necro 0.1.4
import tkinter as tk
import ttkbootstrap as ttk
import random

# knife crafting appears in terminal but not box; toggle equip doesn't work at all (button updates)
# rope doesn't update at all
# same for bone knife, only thing that updates is button
# crates are totally non functional
# give info about pay_for_item

# Window setup
screen = ttk.Window(themename="darkly")
screen.title("Necromental")
screen.geometry("800x600")

#tk variables to keep count
dirt_up = tk.IntVar(value=0)
stick_up = tk.IntVar(value=0)
stone_up = tk.IntVar(value=0)
shovel_up = tk.IntVar(value=0)
bucket_up = tk.IntVar(value=0)
bone_knife_up = tk.IntVar(value=0)
bone_shard_up = tk.IntVar(value=0)
knife_up = tk.IntVar(value=0)
rope_up = tk.IntVar(value=0)
bones_up = tk.IntVar(value=0) # need to add 
worktable_up = tk.IntVar(value=0) # i think this too

crates_up = tk.IntVar(value=0) # same here
skeleton_up = tk.IntVar(value=0)

# autoclick setup
auto_click = tk.BooleanVar(value=False)
click_time = 50 # milliseconds

# EQUPMENT TOGGLES
have_shovel = tk.BooleanVar(value=False) #none of these have been set, i did some of the variables but right now they're only collectable
have_bucket = tk.BooleanVar(value=False) #none of these have been set, i did some of the variables but right now they're only collectable
have_knife = tk.BooleanVar(value=False) #none of these have been set, i did some of the variables but right now they're only collectable
have_bone_knife = tk.BooleanVar(value=False)   #none of these have been set, i did some of the variables but right now they're only collectable

# CRAFTING HR
pay_for_item = {
    "shovel": {"sticks": 10, "stones": 5},
    "knife": {"sticks": 3, "bones": 1},  # ADD
    "rope": {"sticks": 6, "knife": 1},  # ADD
    "bucket": {"sticks": 10, "rope": 2}, 
    "crates": {"sticks": 20, "rope": 4}, # ADD
    "worktable": {"sticks": 30, "rope": 5, "stones": 5}, # ADD
    "bone knife": {"bone shards": 2, "stones": 1, "rope": 1}, 
    "bone": {"bone shards": 5}, 
    "skeleton": {"bones": 5, "buckets": 1, "dirt": 10}, # ADD
    # plus whatever else
}

# DIGGING LOGIC AND MATERIAL FIND CHANCE
def with_shovel():
    if have_shovel.get():
        dirt_up.set(dirt_up.get() + 3)
        find_bone_shard()

def no_shovel():
    dirt_up.set(dirt_up.get() + 1)

def dig():
    if have_shovel.get():
        with_shovel()
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


# INFO BOXES - SETUP AND UPDATES, MAIN INTERFACE OF GAME
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
    if bucket_up.get() > 0:
        messages.append("You invented the bucket!")
    if knife_up.get() > 0:
        messages.append("You're using the knife!")
    if bone_shard_up.get() > 0:
        messages.append("You found some bone shards!")
    if bone_knife_up.get() > 0:
        messages.append("You're using the bone knife!")
    if rope_up.get() > 0:
        messages.append("You made some rope!")
    if crates_up.get() > 0:
        messages.append("You made some crates!")
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
    if knife_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {knife_up.get()} knives")
    if rope_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {rope_up.get()} ropes")
    if bone_shard_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {bone_shard_up.get()} bone shards")
    if bone_knife_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {bone_knife_up.get()} bone knife")
    if rope_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {rope_up.get()} ropes")
    if crates_up.get() >= 1:
        materials_box.insert("end", f"\nYou have: {crates_up.get()} crates")
    materials_board()

def update_equipment_board():
    if shovel_up.get() > 0 or bucket_up.get() > 0:
        equipment_box.pack(side="bottom", padx=10, pady=10, anchor="s")
    else:
        equipment_box.pack_forget()

# Updated triggers
shovel_up.trace_add("write", lambda *args: update_equipment_board())
bucket_up.trace_add("write", lambda *args: update_equipment_board())


# CRAFTING MENU AND LOGIC
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
            update_equipment_board() #NOTE: THIS IS WHERE WHE CORRECTLY UPDATE CRAFTING AND EQUIPMENT
            update_materials()

    if item_name == "bucket":
        if (stick_up.get() >= raw_materials.get("sticks", 0)):
            stick_up.set(stick_up.get() - raw_materials.get("sticks", 0))
            bucket_up.set(bucket_up.get() + 1)
            print("have bucket")
            update_equipment_board()
            update_materials()

    if item_name == "bone":  # FIGURE BUTTON!!!!
        if (bone_shard_up.get() >= raw_materials.get("shards", 0)):
            bone_shard_up.set(bone_shard_up.get() - raw_materials.get("shards", 0))
            bones_up.set(bones_up.get() + 1)
            print("have bone")
            update_equipment_board()
            update_materials()

    if item_name == "knife":  
        if stick_up.get() >= raw_materials.get("sticks", 0) and stone_up.get() >= raw_materials.get("stones", 0) and rope_up.get() >= raw_materials.get("rope", 0):
            stick_up.set(stick_up.get() - raw_materials.get("sticks", 0))
            stone_up.set(stone_up.get() - raw_materials.get("stones", 0))
            rope_up.set(rope_up.get() - raw_materials.get("rope", 0))
            print("have knife")
            update_equipment_board()
            update_materials()

    if item_name == "rope":
        if stick_up.get() >= raw_materials.get("sticks", 0):
            stick_up.set(stick_up.get() - raw_materials.get("sticks", 0))
            print("have rope")
            update_equipment_board()
            update_materials()
            update_news()

    if item_name == "bone knife":  # FIGURE BUTTON!!!!
        if bone_shard_up.get() >= raw_materials.get("shards", 0) and stone_up.get() >= raw_materials.get("stones", 0) and rope_up.get() >= raw_materials.get("rope", 0):
            bone_shard_up.set(bone_shard_up.get() - raw_materials.get("shards", 0))
            stone_up.set(stone_up.get() - raw_materials.get("stones", 0))
            rope_up.set(rope_up.get() - raw_materials.get("rope", 0))
            knife_up.set(knife_up.get() + 1)
            print("have bone knife") 
            update_equipment_board() 
            update_materials()

    if item_name == "worktable":
        if stick_up.get() >= raw_materials.get("sticks", 0) and rope_up.get() >= raw_materials.get("rope", 0) and stone_up.get() >= raw_materials.get("stones", 0):
            stick_up.set(stick_up.get() - raw_materials.get("sticks", 0))
            rope_up.set(rope_up.get() - raw_materials.get("rope", 0))
            stone_up.set(stone_up.get() - raw_materials.get("stones", 0))
            worktable_up.set(worktable_up.get() + 1)
            print("have worktable")
            update_equipment_board()
            update_materials()

    if item_name == "crates":
        if stick_up.get() >= raw_materials.get("sticks", 0) and rope_up.get() >= raw_materials.get("rope", 0):
            stick_up.set(stick_up.get() - raw_materials.get("sticks", 0))
            rope_up.set(rope_up.get() - raw_materials.get("rope", 0))
            crates_up.set(crates_up.get() + 1)
            print("have crates")
            update_equipment_board()
            update_materials()

    if item_name == "skeleton":
        if bucket_up.get() >= raw_materials.get("buckets", 0) and bones_up.get() >= raw_materials.get("shards", 0) and dirt_up.get() >= raw_materials.get("dirt", 0):
            bucket_up.set(bucket_up.get() - raw_materials.get("buckets", 0))
            bones_up.set(bones_up.get() - raw_materials.get("shards", 0))
            dirt_up.set(dirt_up.get() - raw_materials.get("dirt", 0))
            skeleton_up.set(skeleton_up.get() + 1)
            print("have skeleton")
            update_equipment_board()
            update_materials()


# MENU TOGGLES
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
# i think it's ok not to have a trace_add here as it happens basically immediately

def craft_menu():  # this is literally just to toggle the menu on when you have enough resources
    if stick_up.get() >= 20 and stone_up.get() >= 10:
        craft_box.pack(side="left", padx=5, pady=5, anchor="nw")
# Bind visibility of crafitng menu to amount of sticks and stones (or whatever variable)
stick_up.trace_add("write", lambda *args: craft_menu())
stone_up.trace_add("write", lambda *args: craft_menu())


# BUTTON TOGGLES
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
        update_news()
    else:
        have_shovel.set(True)  # Equip the shovel
        equip_shovel.config(text="Holding shovel")
        update_news()
    update_equipment_board() 

def toggle_bucket():
    if have_bucket.get():
        have_bucket.set(False)  # Unequip the bucket
        update_news()
    else:
        have_bucket.set(True)
        equip_bucket.config(text="With bucket")
        update_news()
    update_equipment_board()

def toggle_knife():
    if have_knife.get():
        have_knife.set(False)  # Unequip the knife
        update_news()
    else:
        have_knife.set(True)
        equip_knife.config(text="With knife")
        update_news()
    update_equipment_board()

def toggle_bone_knife():
    if have_bone_knife.get():
        have_bone_knife.set(False)  # Unequip the knife
        update_news()
    else:
        have_bone_knife.set(True)
        equip_bone_knife.config(text="With bone knife")
        update_news()
    update_equipment_board()


# BUTTONS AND BOXES
auto_click_button = tk.Button(master=screen, text="Start clicks", command=toggle_click)
auto_click_button.pack(side="bottom", padx=10, pady=10, anchor="se")

dirt_button = tk.Button(master=screen, text="Dig Dirt", command=dig, width=10, height=2)
dirt_button.pack(side="top", padx=10, pady=10, anchor="nw")

materials_box = tk.Text(master=screen, width=30, height=20)
news_box = tk.Text(master=screen, width=30, height=10)


craft_box = tk.Text(screen)
shovel_button = tk.Button(master=craft_box, text="Craft shovel", cursor="hand2", command=lambda: crafting("shovel"))
shovel_button.pack(pady=5)
bucket_button = tk.Button(master=craft_box, text="Craft bucket", cursor="hand2", command=lambda: crafting("bucket"))
bucket_button.pack(pady=5)
knife_button =tk.Button(master= craft_box, text="Craft knife", cursor="hand2", command=lambda: crafting("knife"))
knife_button.pack(pady=5)
bone_knife_button = tk.Button(master= craft_box, text="Craft bone knife", cursor="hand2", command=lambda: crafting("bone_knife"))
bone_knife_button.pack(pady=5)
crates_button = tk.Button(master= craft_box, text="Craft crates", cursor="hand2", command=lambda: crafting("crates"))
crates_button.pack(pady=5)
rope_button = tk.Button(master= craft_box, text="Craft rope", cursor="hand2", command=lambda: crafting("rope"))
rope_button.pack(pady=5)
worktable_button =tk.Button(master= craft_box, text="Craft worktable", cursor="hand2", command=lambda: crafting("worktable")) 

skeleton_button = tk.Button(master= craft_box, text="Craft skeleton", cursor="hand2", command=lambda: crafting("skeleton"))

equipment_box = tk.Text(screen, height=10, width=40, state=tk.DISABLED)
equip_shovel = tk.Button(master=equipment_box, text="Sans shovel", command=toggle_shovel, width=10, height=2)
equip_shovel.pack(side="left", padx=10, pady=10, anchor="nw")
equip_bucket = tk.Button(master=equipment_box, text="Sans bucket", command=toggle_bucket, width=10, height=2)
equip_bucket.pack(padx=5)
equip_knife = tk.Button(master=equipment_box, text="Sans knife", command=toggle_knife, width=10, height=2)
equip_knife.pack(padx=5)
equip_bone_knife = tk.Button(master=equipment_box, text="Sans bone knife", command=toggle_bone_knife, width=10, height=2)
equip_bone_knife.pack(padx=5)


screen.mainloop()