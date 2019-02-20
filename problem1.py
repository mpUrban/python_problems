# written in VS Code with jupyter extension

#https://simpleprogrammer.com/programming-interview-questions/

# How do you find the missing number in a given integer array of 1 to 100? 

# assume only 1 missing number
# missing number can be zeroed or removed from array

#%%
startArray = 1
stopArray = 100

#%%
n = startArray + stopArray - 1

#%%
sequenceArray = list(range(startArray, (stopArray + 1)))

#%%
testArray = sequenceArray.copy()
testArray[4] = 0 #zeroing fifth element

#%%
sumArray = n * (startArray + stopArray) / 2
sumArray

#%%
sumTest = sum(testArray)
sumTest

#%%
answer = sumArray - sumTest
print('The missing number is: ' + str(answer))