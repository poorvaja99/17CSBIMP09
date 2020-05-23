import tkinter
from tkinter import *
import random
answers = [1,1,1,1,3,1,0,1,3,3]
user_answer = [2,1,3,2,3,0,3,1,3,3]

def calc():
    global indexes,user_answer,answers 
    x = 0
    score = 0
    indexes = 5
    for i in range(indexes):
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
calc()        
