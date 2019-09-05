# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:11:01 2019

@author: benny
"""
import sys

#button up
def getWaysToTheTop(n,X):
    if n==0:
        return 1
    n+=1
    nums = []
    nums.append(1)
    for i in range(1,n):
        total=0
        for j in X:
            if i - j >=0:
                total += nums[i-j]
        nums.append(total)
    return nums[n-1]
    
#recursive
def getWayToTheTopRecursive(n,X):
    if n==0:
        return 1
    total=0
    for i in X:
        if n-i>=0:
            #print(total)
            total+=getWayToTheTopRecursive(n-i,X)
    return total

print(getWaysToTheTop(5,[1,2]))
print(getWayToTheTopRecursive(20,[1,2]))



    


