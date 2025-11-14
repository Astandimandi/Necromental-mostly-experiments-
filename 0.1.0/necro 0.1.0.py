import tkinter as tk
import ttkbootstrap as ttk
import random

#NOTE: for some reason the crafting box doesn't appear at all anymore, but it works in the next file

# window
screen = ttk.Window(themename="darkly")
screen.title("Necromental")
screen.geometry("800x600")


# tk variables to keep count
dirt_up = tk.IntVar(value=0)
stick_up =tk.IntVar(value=0)
stone_up = tk.IntVar(value=0)
shovel_up = tk.IntVar(value=0)


# autoclick setup
auto_click = tk.BooleanVar(value=False)
click_time = 100 # milliseconds


# set how many resources for what item 
pay_for_item = {
    "shovel": {"sticks": 10, "stones": 5},
    "bucket": {"sticks": 20}
# add others
}


# dig button
def dig():
    dirt_up.set(dirt_up.get() + 1)
    update_materials()
    find_stone()
    find_stick()
    update_news()
# the dig button specifically has to hold some news updates as the
# conditions are dependant on the other functions encapsulated here


def find_stone():
    if dirt_up.get() >= 30:
        if random.random() < 0.13: # i think <= would give even more different chances
            stone_up.set(stone_up.get() + 1)


def find_stick():
    if dirt_up.get() >= 10:
        if random.random() < 0.10:
            stick_up.set(stick_up.get() +2)


def update_news():
    news_box.config(state=tk.NORMAL) # this and the line below are so the textboxes are not interactable
    news_box.delete("1.0", tk.END)
    messages = [] # in a list to handle more gracefully without having to clear it each time (plus it makes a mess)
    if stick_up.get() > 0:
        messages.append("You found a few sticks!")
    if stone_up.get() > 0:
        messages.append("You found a stone!")
    if shovel_up.get() >0:
        messages.append("You made a shovel!")
    news_box.insert("end", "\n".join(messages))
    news_box.config(state=tk.DISABLED) # this is where it makes it un-interactable


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
    materials_box.insert("end", "\n".join(messages))
    materials_box.config(state=tk.DISABLED)
# because these change dynamically, they have to be indented manually


# crafting logic for payments of resources
def crafting(item_name):
    raws_fee = pay_for_item.get(item_name)
    if not raws_fee:
        return #item not found
    if (stick_up.get() >= raws_fee["sticks"] and stone_up.get()>= raws_fee["stones"]):
# if we have enough (resource.get) of stone and sticks THEN
# take (resource.SET) our resource and minus them from PAYMENT
        stick_up.set(stick_up.get() - raws_fee["sticks"])
        stone_up.set(stone_up.get() - raws_fee["stones"])
        shovel_up.set(shovel_up.get() + 1)
        update_materials()
        #update_news()

def auto_click_dirt():
    if auto_click.get(): # we set this together with other tk variables above
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


# info box for resources
materials_box = tk.Text(master=screen, width=30, height=20)
materials_box.pack(side="right", padx=10, pady=10, anchor="n")
materials_box.config(state=tk.DISABLED)

# news box setup
news_box = tk.Text(master=screen, width=30, height=10)
news_box.pack(side="right", padx=5, pady=5, anchor="n")
news_box.config(state=tk.DISABLED)

#crafting menu
def show_craft_menu():
    craft_box = tk.Frame(master=screen, width=20, height=10, borderwidth=2)
    craft_box.pack(side="bottom", padx=5, pady=5, anchor="s")

    shovel_button = tk.Button(master=craft_box, text="Craft shovel", command=lambda: crafting("shovel"))
    shovel_button.pack(pady=5)

    bucket_button = tk.Button(master=craft_box, text="Craft bucket", command=lambda: crafting("bucket"))
    bucket_button.pack(pady=5)

# Function to trigger the crafting menu appearance after a delay
def craft_menu_appear():
    if stick_up.get() > 20 and stone_up.get() >= 10:
        screen.after(3000, show_craft_menu)

dirt_button = tk.Button(master=screen, text="dig dirt", command=dig, width=10, height=2)
dirt_button.pack(side="top", padx=10, pady=10, anchor="nw")

# Auto-click toggle button
auto_click_button = tk.Button(master=screen, text="Start Auto-Click", command=toggle_click, width=15, height=2)
auto_click_button.pack(side="top", padx=10, pady=10, anchor="nw")

# Run the main event loop
screen.mainloop()
