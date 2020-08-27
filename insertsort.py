#Eliza Nip
#Summer 2020 CS 325
#HW1 - Q4 Insertsort

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

def main():
    #Open data file
    inFile = open("data.txt","r")
    #Open insert output file and write
    outFile = open("insert.txt","w")
    
    #Iterate in data.txt to move each int to newlist
    #Ref https://stackoverflow.com/questions/27222079/converting-a-single-line-string-to-integer-array-in-python
    for line in inFile:
        newlist = list(map(int,line.split()))[1::]
        
        output = insertSort(newlist)
        for i in output:
            #Write result in insert.txt with space in between int 
            outFile.write(str(i)+' ')
        outFile.write('\n')
    
if __name__ == '__main__':
    main()    