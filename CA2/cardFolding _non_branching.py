import os
import sys
import time

def punchcard(punchcard):
    #read in file parameters
    rows = ""
    cols=""
    divideAt = ""
    file = open(os.path.join(sys.path[0], punchcard), "r")
    x = file.read(1)
    while x != "x" and x != "o": #read in for number of rows
        if x != " ":
            rows += x
        else:
            x=file.read(1)
            break
        x=file.read(1)

    while x != "x" and x != "o":# read in for number of columns
        if x != " ":
            cols += x
        else:
            x=file.read(1)
            break
        x=file.read(1)

    while x != "x" and x != "o" and x!= "\n": #read in for the dividing point
        if x != " ":
            divideAt += x
        else:
            break
        x=file.read(1)

    array = ['.' for j in range(int(rows))]
    i=0
    for line in file: #store each line as a string in an array
        array[i] = line.rstrip()
        i+=1
    file.close()

    #set up variables for use in algorithm
    rows = int(rows)
    divideAt = int(divideAt) #folding point
    cols = int(cols)
    result =['' for j in range(int(rows))] #var to store the result in

    if(len(array[0])//2 >= divideAt): #if the folding point is less/equal to halfway along the punch car run this
        for i in range(rows): #increment through each row
            for j in range(divideAt *2, len(array[0])): #first store the excess part of the array 
                # print(j)
                result[i] += array[i][j]
            result[i] = result[i][::-1]  #reverse the excess
        for i in range(rows):
            for j in range(divideAt): #concatinate the result after the excess has been done
                result[i] += array[i][j] * (array[i][j] == array[i][divideAt*2-j-1])#compare counting up the string while counting down from the other side of the fold point
                result[i]+= 'x' * (array[i][j] != array[i][divideAt*2-j-1])#if not matched default to no hole

    elif(len(array[0])//2 < divideAt): #if the folding point is past the halfway point on the punch card, run this
        start = (divideAt*2-len(array[0])) #the point between when the fold overlaps and the over hang
        for i in range(rows):
            for j in range(0, start): #store the non overlapping part of the card at the start
                result[i] += array[i][j]

        for i in range(rows):
            y=0
            for j in range(start, divideAt):
                result[i]+= array[i][j] * (array[i][j] == array[i][len(array[0])-1-y])#compare counting up the string while counting down from the other side of the fold point
                result[i]+= 'x' * (array[i][j] != array[i][len(array[0])-1-y]) #if not matched default to no hole
                y+=1
    return result

start_time = time.time()

arraytest = punchcard("punchcard.txt") #input punchcard file (.txt) formatted correctly (has to be in same folder as cardFolding.py)

algorithim_time = time.time()-start_time

for i in arraytest:
    print(i)
print("Length of each row:", len(arraytest[0]))

print("Execution time of algorithim:", algorithim_time)
print("Execution time of program:", time.time()-start_time)
