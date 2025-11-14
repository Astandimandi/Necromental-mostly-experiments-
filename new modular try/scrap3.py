import ttkbootstrap as tbs
import random


# Function to simulate digging
def dig():
    dirt_up.set(dirt_up.get() + 1)
    find_stone()
    find_stick()

def find_stone():
    if dirt_up.get() >= 30:
        if random.random() < 0.13:
            stone_up.set(stone_up.get() + 1)

def find_stick():
    if dirt_up.get() >= 10:
        if random.random() < 0.10:
            stick_up.set(stick_up.get() + 2)


# tk variables to keep count
dirt_up = tbs.IntVar(value=0)
stick_up = tbs.IntVar(value=0)
stone_up = tbs.IntVar(value=0)
