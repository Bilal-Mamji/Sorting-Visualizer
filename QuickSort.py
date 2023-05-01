import time
from tkinter import *

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    global swap
    for j in range(head, tail):
        swap=0
        if data[j] < pivot:
            swap=1
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)


    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]

    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, timeTick)

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick)

    if(swap==1):
        Timecomplexitylabel = Label(text = "Time complexity: O(n^2)", font = ("new roman", 15, "italic bold"), bg = "#0E6DA5", 
                        width = 25, fg= "black",height = 2,relief = GROOVE, bd = 15) 
        Timecomplexitylabel.place(x=30,y=150)

    if(swap==0):
        Timecomplexitylabel = Label(text = "Time complexity: O(n*logn)", font = ("new roman", 15, "italic bold"), bg = "#0E6DA5", 
                        width = 25, fg= "black",height = 2,relief = GROOVE, bd = 15) 
        Timecomplexitylabel.place(x=30,y=150)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray

    