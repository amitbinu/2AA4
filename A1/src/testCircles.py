## @file testCircles.py


## @title Test Cases for CircleADT.py
# @author Amit Binu
# @date 28/1/2017




## @brief Case 1 for xcoord method in CircleADT:
# @details input: CircleADT.CircleT(5,4,3).xcoord
# @details expected output: 5
# @details output: 5
# @details Test case Passed

## @brief Case 2 for ycoord method in CircleADT:
# @details input: print CircleADT.CircleT(5,4.0,3).ycoord()
# @details expected Output: 4.0
# @details Actual Output: 4
# @details Test Case Passed



## @brief Case 3 for radius method in CircleADT:
# @details input: print CircleADT.CircleT(5,4.0,3).radius()
# @details expected output: 3
# @details actual output: 3
# @details Test Case passed



## @brief Case 4 for area method in CircleADT
# @details input: print CircleADT.CircleT(5,4.0,3).area()
# @details expected Output: 28.2743338823
# @details Actual Ouput: 28.2743338823
# @details Test Case passed



## @brief Case 5 for circumference method in CircleADT
# @details input: print CircleADT.CircleT(5,4.0,3.0).area()
# @details expected Output: 18.8495559215
# @details actual output: 18.8495559215
# @details Test Case passed



## @brief Case 6 for insidebox method in CircleADT
# @details 1)
# @details input: CircleADT.CircleT(55, 44, 33).insidebox(20,78, 70, 70)
# @details Expected Output: True
# @details Actual Output: True
# @details Test Case Passed



## @brief 2nd Case for inside box
# @details 2)
# @details input: CircleADT.CircleT(80,20,0).insidebox(10,20,10,10)
# @details Expected Output: False
# @details Actual Output: False
# @details Test Case Passed

   
    
## @brief 3rd case for insidebox
# @details 3)
# @details input: CircleADT.CircleT(5, -5, 1).insidebox(0,0,20,20)
# @details Expected Output: True
# @details Actual Output: True
# @details Test Case passed


## @brief Case 7 for intersect method in CircleADT
# @details 1)
# @details input: CircleADT.CircleT(0,0,5).intersect(3,0,5)
# @details Expected Output: True
# @details Actual Output: True
# @details Test Case Passed

## @brief
# @details 2)
# @details input: CircleADT.CircleT(0,0,5).intersect(0,0,100)
# @details Expected Output: True
# @details Actual Output: True
# @details Test Case Passed

## @brief
# @details 3)
# @details input: CircleADT.CircleT(0,0,5).intersect(0,100,5)
# @details Expected Output: False
# @details Actual Output: False
# @details Test Case Passed


## @brief Case 8 for scale method in CircleADT
# @details input: h = CircleADT.CircleT(0,0,5); h.scale(8); h.radius()
# @details Expected Output: 40
# @details Actual Output: 40
# @details Test Case Passed


## @brief Case 9 for translate method in CircleADT
# @details input: h = CircleADT.CircleT(0,0,40); print h.xcoord(), h.ycoord()
# @details Expected Output: 5 , 6
# @details Actual Output: 5 , 6
# @details Test case Passed

## @brief Case 10 for average method in Statistics method
# @details input: Statistics.average([CircleADT.CircleT(11, 12, 6),CircleADT.CircleT(10,10,5),CircleADT.CircleT(5,5,11),CircleADT.CircleT(2,3,9)])
# @details Expected Output: 7.75
# @details Actual Output: 7.75
# @details Test case passed



## @brief Case 11 for rank method in Statistics method
# @details input: Statistics.stdDev([CircleADT.CircleT(11, 12, 6),CircleADT.CircleT(10,10,5),CircleADT.CircleT(5,5,11),CircleADT.CircleT(2,3,9)])
# @details Expected Output: 2.38484800354
# @details Actual Output: 2.38484800354
# @details Test case Passed



## @brief Case 12 for rank method in Statistics method
# @details input: Statistics.rank([CircleADT.CircleT(11, 12, 6),CircleADT.CircleT(10,10,5),CircleADT.CircleT(5,5,11),CircleADT.CircleT(2,3,9)])
# @details Expected Output: [3, 4, 1, 2]
# @details Actual Output: [3, 4, 1, 2]
# @details Test Case Passed


