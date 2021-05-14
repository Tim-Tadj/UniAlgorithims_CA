import sys
import os
import time

def find_solution(people):

    #stores the second shortest distance of of every person
    secondBestDistances = []
    for i in range(len(people)): #iterates through current person

        #stores all the distances from the current person to another person
        distances = [] 

        for j in range(len(people)): #iterates through all other people
            if j !=i: #if not itself, save the distance
                distances.append( (people[i][0] - people[j][0])**2 + (people[i][1] - people[j][1])**2 )

        distances.sort() #sort distance
        if len(distances) > 1:
            secondBestDistances.append(distances[1]) #save the second smallest distance of current person

    secondBestDistances.sort()#sort all the second smallest distances

    solution = secondBestDistances[0] #finds the best out of all the second smallest distances
    return solution
    
            

filename = input("Enter name of .txt file to read in (must be in dir of .py file): ")

with open(os.path.join(sys.path[0], filename), "r") as inputf:

    #get number of specified people
    nPeople = int(inputf.readline())

    #tests to see if over the limit of number of people
    if not 3 <= nPeople <= 100:
        print("wrong number of people!")
        quit()

    #stores coordinates for every person
    people = [] 
    for i in range(1, nPeople+1):

        #get coordinate
        person = [int(b) for b in inputf.readline().rstrip().split()]

        #tests to see of coordinates are valid
        if (-10000 <= person[0] <=10000) and (-10000 <= person[1] <=10000):
            people.append(person) #store coordinate
        else:
            print("wrong coordiate!", person[0], person[1])
            quit()

    #tests to see if we scanned in the right number of people
    if len(people)!=nPeople:
        print("wrong number of people!")
        quit()

    start = time.perf_counter()
    Ans = find_solution(people) #run the find solution algorithim
    finish = time.perf_counter()

    print("Answer:", Ans)
    print("Done in", finish-start, "s")

    