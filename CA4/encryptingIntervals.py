def gcd(a,b): #our gcd func
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
#makes a list containing elements incremented from first to last
def make_array(start, finish):
    result = []
    for i in range(start, finish+1):
        result.append(i)
    return result

#returns all relativly prime combinations
def make_combinations(array1, array2):
    result = []
    for i in array1:
        for j in array2:
            if gcd(i, j) == 1:
                result.append((i, j))
    return result

first_start, first_end = input("Line 1: ").rstrip().split(" ")
second_start, second_end = input("Line 2: ").rstrip().split(" ")


first_array = make_array(int(first_start), int(first_end))
second_array = make_array(int(second_start), int(second_end))
combinations = make_combinations(first_array, second_array)
output = len(combinations)
print("Strength of encryption:",output)