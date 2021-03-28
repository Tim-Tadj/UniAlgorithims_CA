def CEO_stock(n):
    total =0
    i = 1 

    #checks the difference between the current number and the next number if the number is greater then 1, it is repeated
    while(((n//i)-(n//(i+1))) > 1):
        #add the amount of of i's by (n//i)-n//(i+1)) times (the amount of times it occurs)
        total += ((n//i)-n//(i+1))*i
        i+=1

    #for all numbers not repeated, add them
    for j in range(1,(n//i+1)):
        total+=n//j
    return total
#n/1 + n/2 + n/3 .... n/n
import time
print("Please input number of days: ")
n = int(input())

start = time.perf_counter()
print("\nNumber of total stocks to be recieved:")
print(CEO_stock(n), "\nTime taken:", time.perf_counter()-start, "(s)")