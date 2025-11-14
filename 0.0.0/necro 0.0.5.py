import tkinter as tk
import ttkbootstrap as ttk
import random

# Initialize the main window
screen = ttk.Window(themename="darkly")
screen.title("Necromental")
screen.geometry("800x600")

# tk variables to keep count
dirt_up = tk.IntVar(value=0)
stick_up = tk.IntVar(value=0)
stone_up = tk.IntVar(value=0)

# Function to simulate digging
def dig():
    dirt_up.set(dirt_up.get() + 1)  
    update_score() 
    find_stone() 
    find_stick() 
    update_news()  

# Function to check and find stone
def find_stone():
    stone_chance()

# Function to determine the chance of finding stone
def stone_chance():
    if dirt_up.get() >= 30: 
        chance = random.random()  
        if chance < 0.13:  
            stone_up.set(stone_up.get() + 1)  

# Function to check and find stick
def find_stick():
    stick_chance()

# Function to determine the chance of finding stick
def stick_chance():
    if dirt_up.get() >= 10: 
        chance = random.random()  
        if chance < 0.10: 
            stick_up.set(stick_up.get() + 2)  

# Function to update the news box
def update_news():
    news_box.delete("1.0", tk.END)  
    messages = []
    if stick_up.get() > 0:
        messages.append("You found a few sticks!")  
    if stone_up.get() > 0:
        messages.append("You found a stone!")
    news_box.insert("1.0", "\n".join(messages))  

# Function to update the materials box
def update_score():
    materials_box.delete("1.0", tk.END)  
    materials_box.insert("1.0", f"You have dug: {dirt_up.get()} dirt") 
    if stick_up.get() >= 1:
        materials_box.insert("end", f"\nYou have {stick_up.get()} sticks") 
    if stone_up.get() >= 1:
        materials_box.insert("end", f"\nYou gathered: {stone_up.get()} stones")  

# Info box for displaying resources
materials_box = tk.Text(master=screen, width=30, height=20)
materials_box.pack(side="right", padx=10, pady=10, anchor="n")

# News box for displaying updates
news_box = tk.Text(master=screen, width=30, height=10)
news_box.pack(side="right", padx=5, pady=5, anchor="n")

# Button for digging dirt
dirt_button = tk.Button(master=screen, text="dig dirt", command=dig, width=15, height=5)
dirt_button.pack(side="top", padx=10, pady=10, anchor="nw")

# Run the main event loop
screen.mainloop()
