from tkinter import *
from tkinter import ttk
import random
import time
import tkinter as tk
from BubbleSort import bubbleSort
from MergeSort import merge_sort
from QuickSort import quick_sort
from SelectionSort import selectionSort
from CountingSort import count_sort
from BucketSort import bucketSort
from InsertionSort import insertion_Sort
from HeapSort import heapSort
from RadixSort import radixSort


root = Tk()
root.title('Sorting Algorithm Visualisation')
# root.geometry('900x600+200+70')
root.geometry('1150x670+100+30')
root.config(bg='#00001B')

# variables
selected_algorithm=StringVar()
selected_file=StringVar()
data = []

# function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 520
    c_width = 1120
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 10
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0,anchor=SW, text=str(data[i]),
        font=("new roman", 15, "italic bold"), fill = "orange")
        
    root.update_idletasks()

def FileGenerate():
    global data

    data=[]

    if(inputfilescale.get()== 'File1.txt'):
        my_file = open(r"C:\Users\Dell\Desktop\File1.txt")
        data = my_file.read()

        data_into_list = data.replace('\n', ' ').split(",")
        File1 = [eval(i) for i in data_into_list]

        data=File1

    if(inputfilescale.get()== 'File2.txt'):
        my_file = open(r"C:\Users\Dell\Desktop\File2.txt")
        data = my_file.read()

        data_into_list_2 = data.replace('\n', ' ').split(",")
        File2 = [float(i) for i in data_into_list_2]

        data=File2

    if(inputfilescale.get()== 'File3.txt'):
        my_file = open(r"C:\Users\Dell\Desktop\File3.txt")
        data = my_file.read()

        data_into_list_2 = data.replace('\n', ' ').split(",")
        File3 = [eval(i) for i in data_into_list_2]

        data=File3

    if(inputfilescale.get()== 'File4.txt'):
        my_file = open(r"C:\Users\Dell\Desktop\File4.txt")
        data = my_file.read()

        data_into_list_2 = data.replace('\n', ' ').split(",")
        File4 = [eval(i) for i in data_into_list_2]

        data=File4

    drawData(data, ['white' for x in range(len(data))])


# def Generate():
#     global data

#     minVal = int(minvalue.get())
#     maxVal = int(maxvalue.get())
#     size = int(sizevalue.get())

#     data = []
#     for _ in range(size):
#         data.append(random.randrange(minVal, maxVal + 1))

#     drawData(data, ['white' for x in range(len(data))])  # ['red', 'red' ,....]

def StartAlgorithm():
    global data

    # data2 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.9876, 0.1234, 0.3245, 0.3214, 0.4354, 0.5434]
    if not data:
        return
    if(algMenu.get()== ' Quick Sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedscale.get()) 
        drawData(data, ['green' for x in range(len(data))])

    elif algMenu.get() == " Bubble Sort":
        bubbleSort(data, drawData, speedscale.get())

    elif algMenu.get() == " Selection Sort":
        selectionSort(data, drawData, speedscale.get())
    
    elif algMenu.get() == " Counting Sort":
        count_sort(data, drawData, speedscale.get())

    elif algMenu.get() == " Merge Sort":
        merge_sort(data, drawData, speedscale1.get())

    elif algMenu.get() == " Insertion Sort":
        insertion_Sort(data, drawData, speedscale.get())   

    elif algMenu.get() == " Bucket Sort":
        bucketSort(data, drawData, speedscale.get())   

    elif algMenu.get() == " Heap Sort":
        heapSort(data, drawData, speedscale.get())   
    
    elif algMenu.get() == " Radix Sort":
        radixSort(data,drawData, speedscale.get())  

def callbackFunc(event):
    country = event.widget.get()
    print(country)

inputfilelabel = Label(text="Design And Analysis of Alogrithm Project", font=("new roman", 15, "italic bold"), bg="#05897A",
relief = RAISED, width=38, bd=15, fg="black" )
inputfilelabel.place(x=270, y=5)

mainlabel=Label(root, text= "ALGORITHM ",font = ("new roman",12,"italic bold"),bg='#05897A',
               width= 13,height=1,bd=15, fg="black",relief=RAISED)
mainlabel.place(x=450,y=70)

algMenu=ttk.Combobox(root, width=13, font = ("new roman",25,"italic bold"),textvariable=selected_algorithm,values=[' Insertion Sort',
 ' Bubble Sort', ' Merge Sort',' Heap Sort', ' Quick Sort', ' Selection Sort', ' Radix Sort',' Bucket Sort', ' Counting Sort'])

algMenu.place(x=620,y=71)
algMenu.current(0)

inputfilelabel = Label(text="READ FROM FILE", font=("new roman", 12, "italic bold"), bg="#05897A",
relief = RAISED, width=15, bd=15, fg="black" )
inputfilelabel.place(x=5, y=70)

inputfile = Button (root, text="GENERATE", bg = "#0E6DA5", font = ("arial",13,"italic bold"),
relief = GROOVE, activebackground="#05945B", activeforeground = "white", bd = 15, width = 15,command = FileGenerate)
inputfile.place(x=950,y=2)

inputfilescale=ttk.Combobox(root, width=8, font = ("new roman",25,"italic bold"),
textvariable=selected_file,values=['File1.txt', 'File2.txt', 'File3.txt', 'File4.txt'])

inputfilescale.place(x=195,y=71)
inputfilescale.current(0)

start = Button (root, text="START", bg = "#0E6DA5", font = ("arial",13,"italic bold"), relief = GROOVE, 
activebackground="#05945B", activeforeground = "white", bd = 15, width = 15,command = StartAlgorithm)
start.place(x=950,y=65)


speedscale = Scale (root,from_ = 0.1, to = 3.0, resolution = 0.1, length=200 , orient = HORIZONTAL,
 font = ("arial", 14, "italic bold"), relief = GROOVE, bd = 2, width = 12)

speedscale1 = Scale (root,from_ = 0.001, to = 3.0, resolution = 0.1, length=200 , orient = HORIZONTAL,
 font = ("arial", 14, "italic bold"), relief = GROOVE, bd = 2, width = 12)

canvas = Canvas (root, width= 1120, height = 520, bg = "#152238") 
# canvas = Canvas (root, width= 1120, height = 520, bg = "black") 
canvas.place(x=10,y=130)

root.mainloop()
