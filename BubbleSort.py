import time
from tkinter import *

def bubbleSort(data, drawData, timeTick):
    swap=0
    for i in range(len(data) - 1):
        drawData(data, ["green" if x == i else "yellow" for x in range(len(data))])
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                swap=1
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, ['green' if x == j or x == j + 1 else 'yellow' for x in range(len(data))])
                time.sleep(timeTick)     

    drawData(data, ['green' for x in range(len(data))])        

    if(swap==1):
        Timecomplexitylabel = Label(text = "Time complexity: O(n^2)", font = ("new roman", 15, "italic bold"), bg = "#0E6DA5", 
                        width = 25, fg= "black",height = 2,relief = GROOVE, bd = 15) 
        Timecomplexitylabel.place(x=30,y=150)
        
    if(swap==0):
        Timecomplexitylabel = Label(text = "Time complexity: O(n)", font = ("new roman", 15, "italic bold"), bg = "#0E6DA5", 
                        width = 25, fg= "black",height = 2,relief = GROOVE, bd = 15) 
        Timecomplexitylabel.place(x=30,y=150)