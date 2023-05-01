import time 
from tkinter import *

K=550

def modified_quicksort(A,p,r):
    global K
    limited_quicksort(A,p,r,K)
    insertion_sort(A,p,r)

def limited_quicksort(A,p,r,treshold):
    if r-p>treshold:
        q=partition(A,p,r)
        limited_quicksort(A,p,q,treshold)
        limited_quicksort(A,q+1,r,treshold)

def partition(A,p,r,drawData,timeTick):
    x=A[r-1]
    i=p
    j=p
    while(j<r-1):
        if A[j]<=x:
            tmp=A[i]
            A[i]=A[j]
            A[j]=tmp
            i=i+1
        j=j+1
        drawData(A, ['green' if x == j or x == j + 1 else 'yellow' for x in range(len(A))])
        time.sleep(timeTick)
    tmp=A[i]
    A[i]=A[r-1]
    A[r-1]=tmp
    return i

def insertion_sort(A,p,r):
    j=p+1
    while(j<r):
        key=A[j]
        i=j-1
        while(i>=p and A[i]>key):
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
        j=j+1

# data = [8, 7, 2, 1, 0, 9,6,8,55,87]
# print("Unsorted Array")
# print(data)

# size = len(data)

# modified_quicksort(data,0,size)

# print(data)
