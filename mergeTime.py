#Eliza Nip
#Summer 2020 CS 325
#HW1 - Q4 MergeTime
import time
import random

#Merge sort fuction
#Ref https://www.geeksforgeeks.org/merge-sort/
def mergeSort(array):
    if len(array) > 1:
        #Find the middle point of array
        midLen = len(array)//2
        #Divide array elements into 2 halves
        left = array[:midLen]
        right = array[midLen:]
        #Sort one half
        mergeSort(left)
        #Sort the other half
        mergeSort(right)
        #Set index to 0
        l = r = i = 0
        #Copy data to temp list left_list and right_list
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[i] = left[l]
                l += 1
            else:
                array[i] = right[r]
                r += 1
            i+= 1
        #Check if any ele left. Empty array if not empty
        while l < len(left):
            array[i] = left[l]
            l += 1
            i += 1
        while r < len(right):
            array[i] = right[r]
            r += 1
            i += 1
    return array

#Same main function as the insersort, only changing the outFile to merge.txt
def main():
    #Iterate in data.txt to move each int to newlist
    #Ref https://stackoverflow.com/questions/27222079/converting-a-single-line-string-to-integer-array-in-python
    rangeArr = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]
    index = 0
    while(index < len(rangeArr)):
        #https://www.programiz.com/python-programming/time#:~:text=time%2Drelated%20functions.-,Python%20time.,the%20point%20where%20time%20begins).
        startTime = time.time()
        #Random generate in range of 10000
        mergeSort([random.random() for _ in range(rangeArr[index])])
        endTime = time.time()
        #End- start = Delta
        delta = endTime - startTime   
        print("n = " + str(index+1), "time:" + str(delta))
        index += 1

if __name__ == '__main__':
    main()  