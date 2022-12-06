# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:57:35 2022

@author: Jelson
This is my attempt at AdventofCode2022

"""
import heapq

"""
#Advent of Code Program 1
def day1():
    #Reading the file and splitting into a list
    f = open("day1.txt", 'r')
    cal = f.read()
    cals = cal.split("\n")
    
    #calculate the number of calories per elf
    add = 0
    sumList = []
    for item in cals:
        if item != '':
            add += int(item)
        if item == '':
            sumList.append(add)
            add = 0
    
    #Find elf with the most calories - Part 1
    greatest = 0
    elfNum = 0
    for i in range (0,len(sumList)):
        if(sumList[i] > greatest):
            greatest = sumList[i]
            elfNum = i
    
    print("The elf with the most calories is Elf " + str(elfNum) + " and he has " + str(greatest) + " calories on him")
    
    #Part 2 - Find the top 3 largest calories and add them 
    top3 = heapq.nlargest(3,sumList)
    print("The 3 elves with the most calories are carrying " + str(top3[0]) + " calories, " + str(top3[1]) + 
          " calories, and " + str(top3[2]) + " calories which totals to " + str(top3[0] + top3[1] + top3[2]) + " calories") 
"""

"""
#Advent of Code Program 2
def day2():
    #Reading in the text file
    f = open("day2.txt", 'r')
    strat = f.read()
    strat = strat.replace(" ", "")
    strat = strat.split("\n")

    
    #Part 1
    #Creating a dictionary to convert into rock, paper, scissors
    key1 = {'A' : 'rock', 'B' : 'paper', 'C' : 'scissors', 'X' : 'rock', 'Y' : 'paper', 'Z' : 'scissors'}

    #Calculate the score for part 1
    points = 0
    for item in strat:
        opp = key1[item[0]]
        you = key1[item[1]]

        #print("Your opponent played " + opp + ", so you should play " + you + " according to the strategy guide")

        #Points for picks + determining if you win or lose
        if(you == 'rock'):
            points += 1
            if(opp == 'rock'):
                points += 3
            elif(opp == 'scissors'):
                points += 6

        elif(you == 'paper'):
            points += 2
            if(opp == 'paper'):
                points += 3
            elif(opp == 'rock'):
                points += 6

        elif(you == 'scissors'):
            points += 3
            if(opp == 'scissors'):
                points += 3
            elif(opp == 'paper'):
                points += 6

    print("You scored this many points in Rock, Paper, Scissors: " + str(points))
    

    #Updating the strategy guide
    key2 = {'A' : 'rock', 'B' : 'paper', 'C' : 'scissors', 'X' : 'lose', 'Y' : 'tie', 'Z' : 'win'}

    newpoints = 0
    for item in strat:
        opp = key2[item[0]]
        you = key2[item[1]]

    #Calculating scores
        if(you == 'lose'):
            if(opp == 'rock'):
                #You need to pick scissors
                newpoints += 3
            elif(opp == 'paper'):
                #You need to pick rock
                newpoints += 1
            elif(opp == 'scissors'):
                #You need to pick paper
                newpoints += 2

        elif(you == 'tie'):
            newpoints += 3
            if(opp == 'rock'):
                #You need to pick rock
                newpoints += 1
            elif(opp == 'paper'):
                #You need to pick paper
                newpoints += 2
            elif(opp == 'scissors'):
                #You need to pick scissors
                newpoints += 3

        elif(you == 'win'):
            newpoints += 6
            if(opp == 'rock'):
                #You need to pick paper
                newpoints += 2
            elif(opp == 'paper'):
                #You need to pick scissors
                newpoints += 3
            elif(opp == 'scissors'):
                #You need to pick rock
                newpoints += 1

    print("You scored this many points in Rock, Paper, Scissors: " + str(newpoints))
"""

"""
#Advent of Code Program 3
def day3():
    f = open("day3.txt", 'r')
    sacks = f.read()
    sacks = sacks.split("\n")

    
    #Part 1 calculate the sum of each priority item in the rucksack
    sum1 = 0
    for item in sacks:
        num = int(len(item)/2)
        #Split the rucksacks into two to find the common value
        first = item[:num]
        second = item[num:]
        for i in range(num):
            if(second[i] in first):
                lett = second[i]
        
        #Calculate the common letter priority value and sum
        if(lett.isupper()):
            prio = ord(lett)-38
        else:
            prio = ord(lett) - 96
        sum1 += prio
        #print("The compartments are split into " + first + " and " + second)
    
    print("The sum of the priorities is " + str(sum1))
    


    #Part 2 - Calculate the priorities when looking at sets of 3
    ruck = []
    comlet = []
    sum2 = 0
    for i in range(0, len(sacks), 3):
        #Split the rucksacks into two to find the common value
        first = sacks[i]
        second = sacks[i + 1]
        third = sacks[i + 2]

        #find the common letter between the 3 sacks
        for x in first:
            ruck.append(x)
        
        for y in second:
            if(y in ruck):
                comlet.append(y)
        
        for z in third:
            if(z in comlet):
                lett = z

        ruck = []
        comlet= []

        #Calculate the common letter priority value and sum
        if(lett.isupper()):
            prio = ord(lett)-38
        else:
            prio = ord(lett) - 96
        sum2 += prio 

    print("The sum of the priorities is " + str(sum2))
"""

"""
#Advent of Code Program 4
def day4():
    #read in the file
    f = open("day4.txt", 'r')
    jobsList = f.read()
    jobsList = jobsList.split("\n")

    #Splitting the jobs into lists
    countOverlap = 0 #The count for part 1
    countRange = 0 #The count for part 2
    overlap = False
    for job in jobsList:
        tasks = job.split(',')
        
        
        # #Removed because the second iteration of day4Helper does this
        # taskOne = tasks[0]
        # taskOne = taskOne.split('-')
        
        # taskTwo = tasks[1]
        # taskTwo = taskTwo.split('-')
        
        print(tasks)
        #Creates a list from the Start-End pair
        taskOne,taskTwo = day4Helper(tasks)

        #Part 1 if count variable increase
        if(all(element in taskOne for element in taskTwo)):
            countOverlap += 1
        elif(all(element in taskTwo for element in taskOne)):
            countOverlap += 1 
        
        #Part 2 element increase - for some reason if((element in taskOne for element in taskTwo)): did not 
            # count correctly so I broke it down
        for element in taskOne:
            print(element)
            if(element in taskTwo):
                overlap = True

        if(overlap):
            countRange += 1
        overlap = False

    print("The number of pairs that have a assignment fully contained is " + str(countOverlap)) #Part 1
    print("The number of pairs that have range overlap is " + str(countRange)) #Part 2
        


# #Iteration 1 that uses the already split taskOne and taskTwo
# def day4Helper(taskList):
#     newList = []
#     start = int(taskList[0])
#     end = int(taskList[1])
#     while start <= end:
#         newList.append(start)
#         start += 1
#     return newList


#Iteration 2 that uses the initial to task line to break into separate lists (I did this to reduce the number of variables used)
def day4Helper(taskList):
    newListOne = []
    newListTwo = []

    taskOne = taskList[0]
    taskOne = taskOne.split('-')
        
    taskTwo = taskList[1]
    taskTwo = taskTwo.split('-')

    startOne = int(taskOne[0])
    endOne = int(taskOne[1])
    while startOne <= endOne:
        newListOne.append(startOne)
        startOne += 1

    startTwo = int(taskTwo[0])
    endTwo = int(taskTwo[1])
    while startTwo <= endTwo:
        newListTwo.append(startTwo)
        startTwo += 1
    
    return newListOne, newListTwo
"""
def main():
    #day1()
    #day2()
    #day3()
    #day4()
    pass


if __name__ == "__main__":	  	
    main()