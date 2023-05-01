import time
from tkinter import *

def insertionSort(b):
	# global swap
	# if len(b)>1:
		# swap=1
		# print("a")
	# if len(b)<=0:
		# swap=0
		# print("b")
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1			
		b[j + 1] = up	
		
	return b	
			
def bucketSort(x,drawData,timeTick):
	arr = []
	slot_num = 10 # 10 means 10 slots, each
				# slot's size is 0.1
	for i in range(slot_num):
		arr.append([])

	# Put array elements in different buckets
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)
		drawData(x, ["green" if y == j else "yellow" for y in range(len(x))])
		time.sleep(timeTick)
		
	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])
		drawData(x, ["green" if y == i else "yellow" for y in range(len(x))])
		time.sleep(timeTick) 

	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
			drawData(x, ["green" if y == j else "yellow" for y in range(len(x))])
			time.sleep(timeTick) 

			
		Timecomplexitylabel = Label(text="Time complexity: O(n^2)", font=("new roman", 15, "italic bold"), bg="#0E6DA5",
                                    width=25, fg="black", height=2, relief=GROOVE, bd=15)
		Timecomplexitylabel.place(x=30,y=150)
	# if swap==1:
		
	# if swap==0:
		# Timecomplexitylabel = Label(text="Timecomplexity: O(n+k)", font=("new roman", 12, "italic bold"), bg="#0E6DA5",
		# 							width=20, fg="black", height=2, relief=GROOVE, bd=5)
		# Timecomplexitylabel.place(x=0, y=85)

	# if swap==2:
	# 	Timecomplexitylabel = Label(text="Timecomplexity: O(n^2)", font=("new roman", 12, "italic bold"), bg="#0E6DA5",
	# 								width=20, fg="black", height=2, relief=GROOVE, bd=5)
	# 	Timecomplexitylabel.place(x=0, y=85)	

	return x

	


	
