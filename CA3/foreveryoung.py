#30/04/21
import time

def intListToString(input):
    output = ""
    for i in input:
        output += str(i) # for each element add a string version of that element ot ouput
    if output == "": # if empty make output a 0
        output = "0"
    return output

def convertToBase(num, base):
    result = []
    remainder = 0
    isValid = True # default the vailidity of the number to true until falsified
    if num == base:
        result = [1, 0]
        return result, isValid # if the base and num is the same we know the outcome
    while num >= 1: #if num is below 1 stop the loop
        remainder = int(num) % base 
        if remainder > 9:# if remainder is large than 9 it wont fit our requirement
            isValid = False
        result.append(remainder) #add the remainder to the number in base "base"
        num /= base #go to next digit
    return result[::-1], isValid

def doSearch(age, minAge):
    minAge = str(minAge) #change minAge to string for comparisons
    upper_limit = age #initialise upper limit
    lower_limit = 10 #initialise lower limit
    isValid =  False #assume invalide

    while lower_limit <= upper_limit: #while we can still binary search, do it
        
        mid = (upper_limit + lower_limit) // 2
        numAsBase, isValid = convertToBase(age, mid)

        if len(numAsBase) > len(minAge): #influence it by looking at number of digits
            lower_limit = mid + 1
        elif len(numAsBase) < len(minAge): #same as prev if
            upper_limit = mid -1

        elif str(numAsBase[0])>= minAge[0]: #once we have same number of digits, look at the most significant digit
            lower_limit = mid + 1
        elif str(numAsBase[0]) < minAge[0]:#same as prev elif
            upper_limit = mid - 1
    
    #once we are in region of answer, go towards the limit until the answer is reached
    while not isValid or (isValid and int(intListToString(numAsBase)) < int(minAge)):
        mid -= 1
        numAsBase, isValid = convertToBase(age, mid)


    return numAsBase, mid


Input = input("Enter current age and minimum age seprated by a space: ").rstrip().split(" ")
if len(Input) == 2:
    age = int(float(Input[0]))
    minAge = int(Input[1])
else:
    print("INVALID INPUT!")
    quit()

start = time.perf_counter()
ageResult, base = doSearch(age, minAge)
finish = time.perf_counter()
ageResult = intListToString(ageResult)
print('The age', age, 'is', ageResult, 'in base', base, '\nRun Time =', finish - start, "s")
