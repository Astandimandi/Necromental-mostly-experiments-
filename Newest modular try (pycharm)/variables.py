# variables for tk

import tkinter as tk

class Materials:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Materials, cls).__new__(cls)
        return cls._instance

    def __init__(self, screen):
        if not hasattr(self, 'initialized'):
            self.dirt_up = tk.IntVar(value=0)
            self.stick_up = tk.IntVar(value=0)
            self.stone_up = tk.IntVar(value=0)
            self.knife_up = tk.IntVar(value=0)
            self.rope_up = tk.IntVar(value=0)
            self.shovel_up = tk.IntVar(value=0)
            self.bone_shards_up = tk.IntVar(value=0)

            self.bucket_up = tk.IntVar(value=0)
            self.empty_buckets = tk.IntVar(value=0)
            self.bucket_space = tk.IntVar(value=0)
            self.filled_bucket = 100
            self.full_buckets = tk.IntVar(value=0)

            self.crates_up = tk.IntVar(value=0)
            self.empty_crates = tk.IntVar(value=0)
            self.crate_space = tk.IntVar(value=0)
            self.filled_crate = 4
            self.full_crates = tk.IntVar(value=0)

            self.have_shovel = tk.BooleanVar(value=False)
            self.have_knife = tk.BooleanVar(value=False)
            self.have_bucket = tk.BooleanVar(value=False)
            self.have_crate = tk.BooleanVar(value=False)

            self.click_time = 50  # ms
            self.dev_click = tk.BooleanVar(value=False)
            self.initialized = True



if __name__ == "__main__":
    screen = None
