#Eliza Nip
#Summer 2020 CS 325
#HW1 - Q4 InsertTime
import time
import random
#Insertion Sort function
#Reference https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertSort(array):
    #Traverse list 
    for n in range(1,len(array)):
        #Store current list value(temp)
        temp = array[n]
        #Move the index to 1 pos
        x = n-1
        #Current temp index is less than stored array value
        while x >= 0 and temp < array[x]:
            #Shift the value and dec index
            array[x+1] = array[x]
            x -= 1
        #Insert stored value to correct pos
        array[x+1] = temp
    return array
# def randomArray(size):
#     return [random.randint(0,10000) for _ in range(size)]

def main():
    #Iterate in data.txt to move each int to newlist
    #Ref https://stackoverflow.com/questions/27222079/converting-a-single-line-string-to-integer-array-in-python
    rangeArr = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]
    index = 0
    while(index < len(rangeArr)):
        #https://www.programiz.com/python-programming/time#:~:text=time%2Drelated%20functions.-,Python%20time.,the%20point%20where%20time%20begins).
        startTime = time.time()
        #Random generate in range of 10000
        insertSort([random.random() for _ in range(rangeArr[index])])
        endTime = time.time()
        #End- start = Delta
        delta = endTime - startTime   
        print("n = " + str(index+1), "time:" + str(delta))
        index += 1

if __name__ == '__main__':
    main()    