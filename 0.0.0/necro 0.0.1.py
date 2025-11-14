import tkinter as tk
import ttkbootstrap as ttk

screen = ttk.Window()
screen.title("Necromental")
screen.geometry("800x600")

def dig():
    dirt_up.set(dirt_up.get() + 1)
    update_score()
    #score_box.config(text=f"Dirt dug up: {dirt_up.get()}")
# this adds 1 to dirt_up to increase score, and line after updates text in widget
#the other line is commented out because it's equivalent to CALLING UPDATE FUNCTION

def update_score():
    score_box.delete("1.0", tk.END) # clear previous text
    score_box.insert("1.0", f"You have dug: {dirt_up.get()} dirt")

dirt_up = tk.IntVar(value=0)

score_box = tk.Text(master=screen, width= 35, height =30)
score_box.pack(side= "right", padx=5, pady=5, anchor="n")

dirt_button = tk.Button(master = screen, text = "dig dirt", command= dig,  width=15, height=5)
dirt_button.pack(side= "left", padx= 5, pady= 5, anchor="n")


screen.mainloop()
