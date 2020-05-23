import tkinter
from tkinter import *
import random

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        print(x)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    print(indexes)     
gen()
