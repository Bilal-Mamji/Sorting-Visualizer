import time 

def nwaymergeSort(array,n_way,drawData,timeTick):
    if len(array) > 1:

        r = len(array)//n_way
        L = array[:r]
        M = array[r:]

        nwaymergeSort(L,2,drawData,timeTick)
        nwaymergeSort(M,2,drawData,timeTick)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
                drawData(array, ["green" if x == j else "yellow" for x in range(len(array))])
                time.sleep(timeTick)
            else:
                array[k] = M[j]
                j += 1
                drawData(array, ["red" if x == j else "yellow" for x in range(len(array))])
                time.sleep(timeTick)
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            


# def printList(array):
#     for i in range(len(array)):
#         print(array[i], end=" ")
#     print()


# array = [6, 5, 12, 10, 9, 1]

# nwaymergeSort(array,3)

# printList(array)