import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


def input():
    # root = Tk()
    # root.geometry("400x400")

    # def pri():
    #     user = e.get()
    #     print(user)
    #
    # e = Entry(root)
    # e.pack()
    #
    # b = Button(root, text="Submit", command=pri)
    # b.pack()
    bubble()

def bubble():

    lst = [2, 6, 4, 1, 3, 6, 7, 5, 2, 3, 9]
    x = np.arange(0, len(lst), 1)

    print(lst)
    print(x)
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            plt.bar(x, lst)
            plt.pause(0.001)
            plt.clf()
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    plt.show()

input()