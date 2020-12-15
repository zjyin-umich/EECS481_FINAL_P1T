# test suite for the Binomial Coefficient Algorithm

# Note: this implementation is the Dynamic Programming solution to the binomial coefficient
# from geeksforgeeks.com. The link is:
# https://www.geeksforgeeks.org/binomial-coefficient-dp-9/

import random
# Please not that we use math.comb which is only available on Python 3.8 or above.
import math

array = [0]*100
array1 = [0]*100
i = 0
j = 0
temp = 0 
max = 0 
count = 0
maxdigits = 0 
c = 0

def postmansort(numericalData,size):

    t1, t2, k, t, n = 1

    for x in range(count):
        array1[x] = array[x]
    

    
    for x in range(count):
        t = array[x]
        while t > 0:
            c = c + 1
            t = t / 10
        if maxdigits < c: 
            maxdigits = c 
        c = 0

    while (maxdigits > -1):
        n = n * 10
        maxdigits -= 1
    
    i = 0
    for i in range (0, count):
        max = array[i] / n
        j = i + 1 
        for j in range (0, count):
            j += 1
            if max >  (array[j] / n):
                max = array[j] / n 
                t = j 
        
        temp = array1[t]
        array1[t] = array1[i]
        array1[i] = temp 
        temp = array[t]
        array[t] = array[i]
        array[i] = temp 
        
    
    
    while n >= 1:
        for i in range (0, count):
            t1 = array[i] / n
            j = i + 1
            for j in range (0, count):
                if t1 == (array[j] /n):
                    swapTMPS(i , j)
                    i = j
                    j += 1
        n = n / 10 

    print("sorted array POSTMN SRT")
    for i in range (0, count):
        print(array1[i])

def swapTMPS( k , n):
    i = k 
    for i in range (k, n-1):
        j = i + 1 
        for j in range (0, n):
            temp = array1[i]
            array1[i] = array1[j]
            array1[j] = temp 
            temp = array[i] % 10
            array[i] = array[j] % 10
            array[j] = temp
            j += 1


# This function tests the binomial coefficient function by generating a random int for the value of n and k, calculating the binomial coefficient of those values, and asserting that the function calculated the same value.
def test_1():
    array = [1]
    size = 1
    sorted = [1]
    
    result_array = postmansort(array,size) 
    for x in range(size):
        assert(result_array[x] == sorted[x])


def test_2():
    array = [1,2]
    size = 2
    sorted = [1,2]
    result_array = postmansort(array,size) 
    for x in range(size):
        assert(result_array[x] == sorted[x])

def test_3():
    array = [3,2,1]
    size = 3
    sorted = [1,2,3]
    result_array = postmansort(array,size) 
    for x in range(size):
        assert(result_array[x] == sorted[x])

def test_4():
    array = [9,8,7,6,5,4,3,2,1,0]
    size = 10
    sorted = [1,2,3,4,5,6,7,8,9,10]
    result_array = postmansort(array,size) 
    for x in range(size):
        assert(result_array[x] == sorted[x])


def test_4():
    array = [10, 30, 20, 50, 40, 60, 50, 80, 70, 100, 90]
    size = 10
    sorted = [10,20,30,40,50,60,70,80,90,100]
    result_array = postmansort(array,size) 
    for x in range(size):
        assert(result_array[x] == sorted[x])