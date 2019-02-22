# written in VS Code with jupyter extension

#https://simpleprogrammer.com/programming-interview-questions/

# How do you find the largest and smallest number in an unsorted integer array?

#%%
import numpy as np

#%%
# testArray = np.random.randint(10, size=(1,10)) 
testArray = np.random.randint(10, size=(10))
print(testArray)
#testArray.shape

#%%
largest = testArray[0]
smallest = testArray[0]
for element in testArray:
    if (element > largest):
        largest = element
    elif (element < smallest):
        smallest = element

#%%
print(testArray)
print('The smallest number is: ' + str(smallest))
print('The largest number is: ' + str(largest))