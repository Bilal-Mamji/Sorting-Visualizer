import time
from tkinter import *
def insertion_Sort(array,drawData,timeTick):
    swap=0
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # swap=0
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            swap=1
            drawData(array, ["green" if x == j else "yellow" for x in range(len(array))])
            time.sleep(timeTick)
        
        array[j + 1] = key
        drawData(array, ["green" if x == j else "yellow" for x in range(len(array))])
        time.sleep(timeTick) 
        
    drawData(array, ['green' for x in range(len(array))])

    if(swap==1):
        Timecomplexitylabel = Label(text = "Time complexity: O(n^2)", font = ("new roman", 15, "italic bold"), bg = "#0E6DA5", 
                        width = 25, fg= "black",height = 2,relief = GROOVE, bd = 15) 
        Timecomplexitylabel.place(x=30,y=150)

    if(swap==0):
        Timecomplexitylabel = Label(text = "Time complexity: O(n)", font = ("new roman", 15, "italic bold"), bg = "#0E6DA5", 
                        width = 25, fg= "black",height = 2,relief = GROOVE, bd = 15) 
        Timecomplexitylabel.place(x=30,y=150)