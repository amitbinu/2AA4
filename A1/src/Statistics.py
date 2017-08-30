## @file Statistics.py

## @title CircleADT
# @author Amit Binu
# @date 28/1/2017
# @brief This program has functions that doesaverage, stadarad deviation on the radii of the circle objects in a list.
# @details This class has 3 functions in total. -average, stdDEV, rank

import CircleADT
import numpy as np

#instance_1 = CircleADT.CircleT(11, 12, 2)
#instance_2 = CircleADT.CircleT(10,10,9)
#instance_3 = CircleADT.CircleT(5,5,10)
#instance_4 = CircleADT.CircleT(2,3,9)
#instance_5 = CircleADT.CircleT(8,54,9)
#instance_6 = CircleADT.CircleT(89,20,9)

#list = [instance_1, instance_2, instance_3, instance_4, instance_5, instance_6]

##This is an empty list which will contain only radii when the appropriate function is called.
list1 = []
    
## @brief This functon takes a list of CircleADT objects and uses their radii to calculate an average of those radii.
# @param list is a list that contains CircleADT objects
# @return a floating number that represents the average of all radii which is calculated using numpy.
def average(list):
    

    for i in range (len(list)):
        list1.append(list[i].r)
    if (list1 == []):
        return "ERROR: The list should contain at least one item"
    
    return np.average(list1)

## @brief This function takes a list of CircleADT objects and uses their radii to calculate an average of those radii.
# @param list is a list that contains CircleADT objects
# @return a floating number that represents all radii's standard deviation, which is calculated using numpy.
def stdDev(list):
 
    for i in range(len(list)):
        list1.append(list[i].r)
    if (list1 == []):
        return "ERROR: The list should contain at least one item"
    return np.std(list1)


## @brief This function takes a list of CircleADT objects and uses their radii to produce another list with their ranks in descending order.
# @param list is a list that contains CircleADT objects
# @return a list with the ranking of each radii in descending order. 
def rank(list):
    ## This list will contain radii after the rank function is implemented
    list1 =[]
    ## This list will contain radii in descending order after the rank list is implemented
    list2 = []
    ## This list will contain the ranking of radii in descending order after the rank function is implemented
    list3 = []
    for i in range(len(list)):
        list1.append(list[i].r)
        list2.append(list[i].r)

    for i in range(len(list1)):
        for j in range (i+1, len(list1)):
            if ( i != len(list1) - 1):
                if (list1[i] < list1[j]):
                    x = list1[i]
                    list1[i] = list1[j]
                    list1[j] = x
    # list1 now contains radii in descending order
    print list1
    print list2
    for i in range (len(list2)):
        list3.append(i)

    counter = 0
        
    for i in range(len(list1)):
        if (i < len(list1)-1):
            if (list1[i] == list1[i+1]):
                counter = counter + 1
                continue
                
        for j in range (len(list2)):
            if (list1[i] == list2[j]):
                if (counter == 0):
                    print i, j
                    list3[j] = i+1
                if (counter == 1):
                    print i, j
                    list3[j] = i
                if (counter > 1):
                    print i,j
                    print counter
                    list3[j] = i - counter + 1

       
                

    if (list1 == []):
        return "ERROR: The list should contain at least one item"
    
    return list3

#Testing

#print average(list)
#print stdDev(list)
#print rank(list)
