# written in VS Code with jupyter extension

#https://simpleprogrammer.com/programming-interview-questions/

# How do you find the duplicate number on a given integer array? 

# solving without using packages

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

print('The array with duplicates removed is: ')
print(newArray)
print('The duplicates found are: ')
print(dupeArray)

#%%
