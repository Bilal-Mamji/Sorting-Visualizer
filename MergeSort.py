import time
from tkinter import *
s=0
def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data,0, len(data)-1, drawData, timeTick)
    if (s == 1):
        Timecomplexitylabel = Label(text="Time complexity: O(n*logn)", font=("new roman", 15, "italic bold"), bg="#0E6DA5",
                                    width=25, fg="black", height=2, relief=GROOVE, bd=15)
        Timecomplexitylabel.place(x=30,y=150)
    if (s == 0):
        Timecomplexitylabel = Label(text="Time complexity: O(n*logn)", font=("new roman", 15, "italic bold"), bg="#0E6DA5",
                                    width=25, fg="black", height=2, relief=GROOVE, bd=15)
        Timecomplexitylabel.place(x=30,y=150)

def merge_sort_alg(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
    global s
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):

            if leftPart[leftIdx] <= rightPart[rightIdx]:

                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    (s, [1 if x >= left and x <= right else 0 for x in range(len(data))])
    time.sleep(timeTick)

def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")
    return colorArray