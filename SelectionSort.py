import time
from tkinter import *

def selectionSort(array,drawData,timeTick):
    for step in range(0,len(array)):
        min_idx = step

        for i in range(step + 1, len(array)):
            swap=0
            if array[i] < array[min_idx]:
                min_idx = i
            drawData(array, ['green' if x == i else 'yellow' for x in range(len(array))])
            #drawData(array, ['green' if x <= step else 'white' for x in range(len(array))])
            time.sleep(timeTick)

        drawData(array, ['green' if x <= step  else 'yellow' for x in range(len(array))])
        (array[step], array[min_idx]) = (array[min_idx], array[step])

    if(swap==0):
        Timecomplexitylabel = Label(text = "Time complexity: O(n^2)", font = ("new roman", 15, "italic bold"), bg = "#0E6DA5", 
                        width = 25, fg= "black",height = 2,relief = GROOVE, bd = 15) 
        Timecomplexitylabel.place(x=30,y=150)


