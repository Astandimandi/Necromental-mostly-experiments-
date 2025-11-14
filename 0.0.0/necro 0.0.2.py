import tkinter as tk
import ttkbootstrap as ttk
import random


screen = ttk.Window(themename="darkly")
screen.title("Necromental")
screen.geometry("800x600")


# main click + score update
def dig():
    dirt_up.set(dirt_up.get() + 1)
    update_score()
    find_bones()


# resource keeping/counting
def update_score():
    materials_box.delete("1.0", tk.END) # clear previous text
    materials_box.insert("1.0", f"\nYou have dug: {dirt_up.get()} dirt \n")


# bone collecting and updating ONLY for right now
def find_bones():
    if dirt_up.get() >= 5:
        bones_up.set(bones_up.get() + 1)
        news_box.delete("1.0", tk.END)
        news_box.insert("1.0", "You found a bone shard!")
        materials_box.insert("1.0", f"\nYou collected: {bones_up.get()} bone shards")


# tk variables to keep count
dirt_up = tk.IntVar(value=0)
bones_up = tk.IntVar(value=0)


# info boxes builds
materials_box = tk.Text(master=screen, width= 30, height =20)
news_box= tk.Text(master=screen, width= 30, heigh = 10)
materials_box.pack(side= "right", padx=10, pady=10, anchor="n")
news_box.pack(padx=5,pady=5, anchor="center")


# button config
dirt_button = tk.Button(master = screen, text = "dig dirt", command= dig,  width=15, height=5)
dirt_button.pack(side= "left", padx= 5, pady= 5, anchor="n")


screen.mainloop()