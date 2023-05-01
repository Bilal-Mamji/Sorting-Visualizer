import time
from tkinter import *

def count_sort(arr, drawData, timeTick):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1
        drawData(arr, ["green" if x == i else "white" for x in range(len(arr))])
        time.sleep(timeTick)

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]


    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
        drawData(arr, ["green" if x == i else "white" for x in range(len(arr))])
        time.sleep(timeTick)

    Timecomplexitylabel = Label(text="Time complexity: O(n+k)", font=("new roman", 15, "italic bold"), bg="#0E6DA5",
                                    width=25, fg="black", height=2, relief=GROOVE, bd=15)
    Timecomplexitylabel.place(x=30,y=150)