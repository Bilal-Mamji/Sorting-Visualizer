import time
from tkinter import *

def heapify(arr, N, i, drawData, timeTick):

	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2


	if l < N and arr[largest] < arr[l]:
		largest = l
		# drawData(arr, ['red' if x == i else 'yellow' for x in range(len(arr))])
		# time.sleep(timeTick)		

	if r < N and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap
		drawData(arr, ['green' if x == i else 'yellow' for x in range(len(arr))])
		time.sleep(timeTick)

		# Heapify the root.
		heapify(arr, N, largest, drawData, timeTick)


def heapSort(arr, drawData, timeTick):
	N = len(arr)
	for i in range(N//2 - 1, -1, -1):
		heapify(arr, N, i, drawData, timeTick)


	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		drawData(arr, ['yellow' if x == i else 'yellow' for x in range(len(arr))])
		time.sleep(timeTick)
		heapify(arr, i, 0, drawData, timeTick)

	Timecomplexitylabel = Label(text = "Time complexity: O(n*logn)", font = ("new roman", 15, "italic bold"), bg = "#0E6DA5", 
                        width = 25, fg= "black",height = 2,relief = GROOVE, bd = 15) 
	Timecomplexitylabel.place(x=30,y=150)

