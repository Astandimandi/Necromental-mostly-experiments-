#screen
import tkinter as tk
import ttkbootstrap as tbs
import sys
sys.path.append(0, 'c:/Users/carol/OneDrive/Desktop/necromental/variables.py')
import variables

screen  = tbs.Window(themename="darkly")
variables = variables.create_materials(screen)

screen.mainloop()
#Check your IDE or linter settings