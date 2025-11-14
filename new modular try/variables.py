# variables

import tkinter as tk

def create_materials(screen):
    dirt_up = tk.IntVar(value=0)
    stick_up = tk.IntVar(value=0)
    stone_up = tk.IntVar(value=0)
    shovel_up = tk.IntVar(value=0)
    bucket_up = tk.IntVar(value=0)

    knife_up = tk.IntVar(value=0)
    rope_up = tk.IntVar(value=0)
    bone_shard_up = tk.IntVar(value=0)
    bones_up = tk.IntVar(value=0)

    worktable_up = tk.IntVar(value=0)

    # native button states for auto click, equip shovel
    auto_click = tk.BooleanVar(value=False)
    click_time = 100 # milliseconds

    have_shovel = tk.BooleanVar(value=False)

    screen = None

    return dirt_up, stick_up, stone_up, shovel_up, bucket_up, knife_up, rope_up, bone_shard_up, bones_up, worktable_up, auto_click, click_time, have_shovel