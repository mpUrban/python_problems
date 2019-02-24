# written in VS Code with jupyter extension

#https://simpleprogrammer.com/programming-interview-questions/

# How are duplicates removed from a given array in Java?


#%%
import numpy as np

#%%
testArray = [2,1,5,8,4,5,4,7,3,9]

#%%
testArraySorted = testArray.copy()
testArraySorted.sort()
print(testArraySorted)

#%%
previous = testArraySorted[0]
resultArray = []
resultArray.append(previous)
#%%
for i, element in enumerate(testArraySorted,start=0):
    if(previous != element):
        resultArray.append(element)
    previous = element

#%%
print(resultArray)