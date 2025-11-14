import tkinter as tk
import ttkbootstrap as ttk
import random


''' steps to adding and building new resources (base ones, at least):
1. create tk.intvar related to resource
2. build counter def resource_chance() with:
    * event handling tied to resource (if/when event a happens, resource is gathered)
    * resource amount
    * news_box.delete and .insert("you found resource!") NOTE: SPECIFICALLY news_box
3. encapsulate counter def in find_resource() def, that will be called by "parent" event or def
4. add event handling in update_score() accordingly; SPECIFICALLY materials_box dynamic updates (f)
5. call find_resource() where appropriate
'''

#NOTE: NEED TO FIGURE OUT STONE GAIN!!! GAINING 10 PER CLICK
# ok so not only do we set stones with random, BUT we need to invert when we get them
# LETS NOT GET BONES UNTIL WE GET A STONE SHOVEL!!!!!!!

screen = ttk.Window(themename="darkly")
screen.title("Necromental")
screen.geometry("800x600")

def dig():
    dirt_up.set(dirt_up.get() + 1)
    update_score()
    find_bones()
    find_stone()

def find_bones():
    bone_chance()


# so we have bone chance as a separate counter for randomness that we can control,
# i tried it by simply inputting chance into one find bone def but it was creating a lot of minor
# quirks that required a papyrus to fix, so this seemed the better option. in this setup, the COUNTER
# governs everything (main logic) and it exists in the find bones function which is called by the 
# clicks on the dirt button (had to do it this way as event handling isn't how i want it). this function
# also governs score update and info box updating (THIS WAS THE TRICKY PART!!!!)
def bone_chance():
    if dirt_up.get() >= 10:
        chance = random.random()
        if chance < 0.17:
            bones_up.set(bones_up.get() + 1)
            news_box.delete("1.0", tk.END)
            news_box.insert("1.0", "You found a bone shard!")

def find_stone():
    stone_chance()

def stone_chance():
    if dirt_up.get() >= 30:
        stone_up.set(stone_up.get() + 2)
        news_box.delete("1.0", tk.END)
        news_box.insert("1.0", "You found a pile of stone!")

# its tricky because the info boxes need to be separate but cohesive, so here we handle when a resource
# update SPECIFICALLY has happened, while the bone_chance handles the news_box being updated (it only needs
# to happen once, while the resource score needs to be updated dynamically)
def update_score():
    materials_box.delete("1.0", tk.END)  # Clear previous text
    materials_box.insert("1.0", f"You have dug: {dirt_up.get()} dirt")
    if bones_up.get() >= 1:
        materials_box.insert("end-1c", f"\nYou have {bones_up.get()} bone shards")
    if stone_up.get() >= 1:   # might have to use a while loop? i need to see the equivalent of continous checks...
        materials_box.insert("end-1c", f"\nYou gathered: {stone_up.get()} stones")


# tk variables to keep count
dirt_up = tk.IntVar(value=0)
bones_up = tk.IntVar(value=0)
stone_up = tk.IntVar(value=0)

# info boxes builds
materials_box = tk.Text(master=screen, width=30, height=20)
news_box = tk.Text(master=screen, width=30, height=10)
materials_box.pack(side="right", padx=10, pady=10, anchor="n")
news_box.pack(padx=5, pady=5, anchor="center")

# button config
dirt_button = tk.Button(master=screen, text="dig dirt", command=dig, width=15, height=5)
dirt_button.pack(side="left", padx=5, pady=5, anchor="n")

screen.mainloop()