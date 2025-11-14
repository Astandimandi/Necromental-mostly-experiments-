# autoclick
import tkinter as tk
import ttkbootstrap as tbs
import sys
print(sys.path)
sys.path.insert(0, 'c:/Users/carol/OneDrive/Desktop/necromental/scrap3.py')
import scrap3 


screen=None

auto_click = tk.BooleanVar(value=False)
click_time = 100  # milliseconds

def click_dirt():
    if auto_click.get():
        dig() # how/where to import this from? shouldn't be difficult
        screen.after(click_time, click_dirt) # PASS, do not call

def toggle_click():
    if click_dirt.get():
        click_dirt.set(False)
        print("Stop Auto-Click")
        auto_click_button.config(text="Start Auto-Click")
    else:
        click_dirt.set(True)
        auto_click_button.config(text="Stop Auto-Click")
        click_dirt()

auto_click_button = tbs.Button(master=screen, text="Start Auto-Click", command=toggle_click, width=15, height=2)
auto_click_button.pack(side="bottom", anchor= "s")

