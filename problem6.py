# written in VS Code with jupyter extension

#https://simpleprogrammer.com/programming-interview-questions/

# How are duplicates removed from a given array in Java?


#%%
import numpy as np

#%%
testArray = np.random.randint(10, size=(1,10))



#%%
testArray = list(range(10))
testArray[2] = 5 # inserting 5 as a duplicate
print(testArray)

#%%
tempArray = sorted(testArray)
print(tempArray)

#%%
newArray = []
dupeArray = []
for element in tempArray:
    if element not in newArray:
        newArray.append(element)
    else:
        dupeArray.append(element)