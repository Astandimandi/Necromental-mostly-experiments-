# sandbox 4 rewrite.py
import tkinter as tk
import ttkbootstrap as ttk
import random

#NOTE: equip bucket won't pack correctly for some reason, i can't use more than like...2 subframes in the same frame?
# i'm so sick of this i want to progress but i never can because of this stupid bullshit

# window
screen = ttk.Window(themename="darkly")
screen.title("Necromental")
screen.geometry("800x600")

# notebook
notebook = ttk.Notebook(screen)
notebook.pack(expand=1, fill="both")
    #tabs
home_page =ttk.Frame(notebook)
craft_page = ttk.Frame(notebook)
notebook.add(home_page, text="Home")
notebook.add(craft_page, text="Crafting")
notebook.forget(craft_page)

# tk variables
dirt_up = tk.IntVar(value=0)
stick_up = tk.IntVar(value=0)
stone_up = tk.IntVar(value=0)
shovel_up = tk.IntVar(value=0)
knife_up = tk.IntVar(value=0)
rope_up = tk.IntVar(value=0)
bone_shards_up = tk.IntVar(value=0)

bucket_up = tk.IntVar(value=0)
full_bucket = 100
in_bucket = tk.IntVar(value=0)

# equips/toggles
have_shovel = tk.BooleanVar(value=False)
have_knife = tk.BooleanVar(value=False)
have_bucket = tk.BooleanVar(value=False)

dev_click = tk.BooleanVar(value=False)
click_time = 50  # ms

recipe_cost = {
    "shovel": {"sticks": 10, "stones": 5},
    "knife": {"sticks": 5, "stones": 3},
    "rope": {"sticks": 3},
    "bucket": {"sticks": 15, "rope": 10},
}

# player stuff
def inventory(var, value):
    var.set(var.get() + value)
#it's the same as dirt_up.set(dirt_up.get() + 1) = but said as the mathematical expression
def toggles(var):
    var.set(not var.get())

# DIGGING
def dig_finds(amount):
    inventory(dirt_up, amount)
    find_stick()
    find_stone()
    update_news()
    update_inventory()

def with_shovel():
    dig_finds(2) # dirt
    find_bone_shards()

def no_shovel():
    dig_finds(1)

def dig():
    if have_shovel.get():
        with_shovel()
    else:
        no_shovel()
    
    news_board()  # Add this line to show the news_box after digging

def find_stick():
    if dirt_up.get() >= 8 and random.random() < 0.15:
        inventory(stick_up, 2)

def find_stone():
    if dirt_up.get() >= 30 and random.random() < 0.13:
        inventory(stone_up, 1)

def find_bone_shards():
    if have_shovel.get() and dirt_up.get() > 30 and random.random() < 0.05:
        inventory(bone_shards_up, 1)

# ROPE MAKING
def knife_use(amount):
    inventory(rope_up, amount)
    update_news()
    update_inventory()

def no_knife():
    update_news() # ADD THIS MESSAGE!!!!

def with_knife():
    knife_use(1)

# BUCKET FUNCTIONS
def fill_bucket():
    if in_bucket.get() < full_bucket:
        remaining_bucket_capacity = full_bucket - in_bucket.get()
        units_to_fill = min(remaining_bucket_capacity, 50)

        # Ensure you have enough dirt to fill the bucket
        available_dirt = dirt_up.get()
        units_to_fill = min(units_to_fill, available_dirt)

        # Update inventory and bucket
        inventory(dirt_up, -units_to_fill)
        in_bucket.set(in_bucket.get() + units_to_fill)
        
        update_inventory()

def empty_bucket():
    pass # this function will make more sense when i add other functionality, right now it's pointless


def crafting(item):
    stored = recipe_cost.get(item)
    if not stored:
        update_news() # ADD MESSAGE!!!!

    if stick_up.get() > stored.get("sticks", 0) and stone_up.get() > stored.get("stones", 0) and rope_up.get() > stored.get("rope", 0):
        inventory(stick_up, -stored.get("sticks", 0))
        inventory(stone_up, -stored.get("stones", 0))
        inventory(rope_up, -stored.get("rope", 0))

    if item == "shovel":
        inventory(shovel_up, 1)
        update_inventory()
    elif item == "knife":
        inventory(knife_up, 1)
        update_inventory()
    elif item == "rope":
        if have_knife.get():
            with_knife()
            inventory(rope_up, 1)
            update_inventory()
        else:
            no_knife()
            update_inventory()
            return
    elif item == "bucket":
        inventory(bucket_up, 1)

    update_news()
    equipment_board()
    print(f"have {item}")

def craft_menu():
    if craft_page not in notebook.tabs():
        notebook.add(craft_page, text= "Crafting")
    else:
        if craft_page in notebook.tabs():
            notebook.forget(craft_page)
stone_up.trace_add("write", lambda *args: craft_menu())

def update_recipe(item):
    stored = recipe_cost.get(item)
    if not stored:
        recipe_box.config(state=tk.NORMAL)
        recipe_box.delete("1.0", tk.END)
        recipe_box.config(state=tk.DISABLED)
        return

    info = f"{item}: \nSticks: {stored.get('sticks', 0)}\nStones: {stored.get('stones', 0)}\nRope: {stored.get('rope', 0)}\n"
    recipe_box.config(state=tk.NORMAL)
    recipe_box.delete("1.0", tk.END)
    recipe_box.insert("end", info)
    recipe_box.config(state=tk.DISABLED)
# i think this can be a different function?
    craft_shovel.pack_forget()
    craft_knife.pack_forget()
    craft_rope.pack_forget()

    if item == "shovel":
        craft_shovel.pack()
    elif item == "knife":
        craft_knife.pack()
    elif item == "rope":
        craft_rope.pack()
    elif item == "bucket":
        craft_bucket.pack()


def news_message(items):
    messages = []
    for item, message in items:
        if globals()[item].get() > 0:
            messages.append(message)
    # add a clear method to make the updates dynamic (not just static on the screen)
    return messages
# this is where we pass dict items as globals to the update_news 

def update_news():
    news_box.config(state=tk.NORMAL)
    news_box.delete("1.0", tk.END)
    messages = news_message([
        ('dirt_up', "You found some dirt!"),
        ('stick_up', "You found a few sticks!"),
        ('stone_up', "You found a stone!"),
        ('shovel_up', "You made a shovel!"),
        ('knife_up', "you forged a knife!"),
        ('rope_up', "You made some rope!"),
        ('bucket_up', "You made a bucket!"),
        ('bone_shards_up', "You found bone shards!"),
    ])
    news_box.insert("end", "\n".join(messages))
    news_box.config(state=tk.DISABLED)
    news_board()

def news_board():
    if dirt_up.get() > 0:
        news_box.pack(side="right", padx=5, pady=5, anchor="n")
    else:
        news_box.pack_forget()


def update_inventory():
    inventory_screen.delete("1.0", tk.END)
    inventory_screen.insert("1.0", f"You have dug: {dirt_up.get()} dirt")
    if stick_up.get() >= 1:
        inventory_screen.insert("end", f"\nYou have {stick_up.get()} sticks")
    if stone_up.get() >= 1:
        inventory_screen.insert("end", f"\nYou have: {stone_up.get()} stones")
    if shovel_up.get() >= 1:
        inventory_screen.insert("end", f"\nYou have {shovel_up.get()} shovels")
    if knife_up.get() >= 1:
        inventory_screen.insert("end", f"\nYou have the simple knife")
    if bucket_up.get() >= 1:
        inventory_screen.insert("end", f"\nYou have {bucket_up.get()} buckets")
    if rope_up.get() >= 1:
        inventory_screen.insert("end", f"\nYou have {rope_up.get()} ropes")
    if bone_shards_up.get() >= 1:
        inventory_screen.insert("end", f"\nYou have {bone_shards_up.get()} bone shards")
# why can't i rewrite this like the news box? i went through this once already in the other builds and it just did NOT work the same lol

def inventory_board():
    if dirt_up.get() >1:
        inventory_screen.pack(side="right", padx=10, pady=10, anchor="n")
    else:
        inventory_screen.pack_forget()

def equipment_board():
    equipment_box.config(state=tk.NORMAL)
    equipment_box.delete("1.0", tk.END)
    
    if shovel_up.get() > 0:
        equip_shovel.pack(side="left", padx=10, pady=10, anchor="nw")

    
    if knife_up.get() > 0:
        equip_knife.pack(side="left", padx=10, pady=10, anchor="nw")

    
    if bucket_up.get() > 0:
        equip_bucket.pack(side="left", padx=10, pady=10, anchor="nw")

    
    equipment_box.config(state=tk.DISABLED)
    equipment_box.pack(side="bottom", padx=10, pady=10, anchor="s")

shovel_up.trace_add("write", lambda *args: equipment_board())
knife_up.trace_add("write", lambda *args: equipment_board())
bucket_up.trace_add("write", lambda *args: equipment_board())


def hold_knife():
    toggles(have_knife)
    equip_knife.config(text="Using knife" if have_knife.get() else "No knife")
    print("stabby stab" if have_knife.get() else "NOT stabby")

def hold_shovel():
    toggles(have_shovel)
    equip_shovel.config(text="Using shovel" if have_shovel.get() else "No shovel")
    print("equipped" if have_shovel.get() else "unequipped")

def hold_bucket():
    toggles(have_bucket)
    equip_bucket.config(text="Holding bucket" if have_bucket.get() else "No bucket")
    print("equipped" if have_bucket.get() else "unequipped")

def autoclick():    
    if dev_click.get():
        dig()
        screen.after(click_time, autoclick)
        #print(f"you have {dirt_up.get()}d, {stick_up.get()}w, {stone_up.get()}r, {bone_shards_up.get()}b")

def use_click():
    toggles(dev_click)
    auto_button.config(text="Stop clicks" if dev_click.get() else "Start clicks")
    if dev_click.get():
        autoclick()


# Main page/dig button
click_frame = ttk.Frame(master=home_page, borderwidth=2, relief="solid") # mother frame for dig and news box (and others later)
click_frame.pack_propagate(False)
click_frame.config(width=600, height=180)
click_frame.pack(side="top", padx=10, pady=10, anchor="nw")
dirt_button = tk.Button(master=click_frame, text="Dig Dirt", command=dig, width=10, height=2)
dirt_button.pack(side="top", padx=10, pady=10, anchor="nw")
news_box = tk.Text(master=home_page, width=30, height=10)
#news_box.pack(side="bottom", padx=10, pady=10, anchor="se")

# auto button for play testing (will be purchaseable later)
auto_button = tk.Button(master=screen, text="Start clicks", command=use_click, width=10, height=2)
auto_button.pack(side="bottom", padx=10, pady=10, anchor="se")

# Crafting frame components
menu_box = ttk.Frame(craft_page,  borderwidth=2, relief="solid") # mother frame for craft drop down, craft buttons, and recipes
menu_box.pack_propagate(False)
menu_box.config(width=300, height=300)
menu_box.pack(side="left", padx=10, pady=10, anchor="nw")
    # NOTE: REMEMBER TO ADD NEW ITEMS HERE OR THEY WON'T SHOW UP!!!!!!!!!!!
crafting_items = ("shovel", "knife", "rope", "bucket")
    # drop down menu
pick_craft = ttk.Combobox(menu_box)
pick_craft.config(width=10)
pick_craft.config(values=crafting_items)
pick_craft.bind("<<ComboboxSelected>>", lambda event: update_recipe(pick_craft.get()))
pick_craft.pack(side="top", padx=10, pady=10, anchor="w")
    # recipe screen
recipe_box = tk.Text(menu_box, height=10, width=20, state=tk.DISABLED)
recipe_box.pack(side="left", padx=10, pady=10, anchor="w")
    # Crafting buttons
craft_shovel = tk.Button(menu_box, text="Craft Shovel", command=lambda: crafting("shovel"))
craft_knife = tk.Button(menu_box, text="Craft Knife", command=lambda: crafting("knife"))
craft_rope = tk.Button(menu_box, text="Craft Rope", command=lambda: crafting("rope"))
craft_bucket = tk.Button(menu_box, text="Craft Bucket", command=lambda: crafting("bucket"))


# inventory screen (updates)
craft_click = ttk.Frame(craft_page,  borderwidth=2, relief="solid")
craft_click.pack(side="left", padx=10, pady=10, anchor="n")
inventory_screen = tk.Text(master=craft_click, width=30, height=10)
inventory_screen.pack(side="right", padx=10, pady=10, anchor="e")

# Equipment toggles (updates) box (shared for all tabs)
equipment_box = tk.Text(screen, state=tk.DISABLED, width=100, height=10)
equip_shovel = tk.Button(master=equipment_box, text="No shovel", command=hold_shovel, width=10, height=4)
equip_shovel.pack(padx=10, pady=10)
equip_knife = tk.Button(master=equipment_box, text="No knife", command= hold_knife, width=10, height=4)
equip_knife.pack(padx=10, pady=10)
equip_bucket = tk.Button(master=equipment_box, text="No bucket", command=hold_bucket, width=10, height=4)
equip_bucket.pack(padx=10, pady=10)

# separate box to store buckets/crates
wares_box = tk.Text(screen, state=tk.DISABLED, width=60, height=20)
# Run
screen.mainloop()