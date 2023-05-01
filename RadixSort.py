import time
from tkinter import *
def countingSort(array, place, drawData, timeTick):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        drawData(array, ['white' if x == i else 'yellow' for x in range(len(array))])
        time.sleep(timeTick)
        count[index % 10] -= 1
        i -= 1


    for i in range(0, size):
        array[i] = output[i]
        drawData(array, ['green' if x == i else 'yellow' for x in range(len(array))])
        time.sleep(timeTick)
        

def radixSort(array, drawData, timeTick):
    max_element = max(array)

    place = 1
    while max_element // place > 0:
        countingSort(array, place, drawData, timeTick)
        place *= 10

    Timecomplexitylabel = Label(text="Time complexity: O(n+k)", font=("new roman", 15, "italic bold"), bg="#0E6DA5",
                                    width=25, fg="black", height=2, relief=GROOVE, bd=15)
    Timecomplexitylabel.place(x=30, y=150)

