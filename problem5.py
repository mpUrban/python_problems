# written in VS Code with jupyter extension

#https://simpleprogrammer.com/programming-interview-questions/

# How do you find duplicate numbers in an array if it contains multiple duplicates?

#%%
testArray = [2,1,5,8,4,5,4,7,3,9,4,6,1]
print('Given array: ' + str(testArray))
#print('Pairs with sum equal to target: ')

#%%
newArray = []
dupeArray = []
for element in testArray:
    if element not in newArray:
        newArray.append(element)
    else:
        dupeArray.append(element)

#%%
print('The array with duplicates removed is: ')
print(newArray)
print('The duplicates found are: ')
print(dupeArray)

#%%
tempArray = {}
for i in testArray:
    # get(key, default) falls back to default if key is not present
    tempArray[i] = tempArray.get(i, 0) + 1
tempArray