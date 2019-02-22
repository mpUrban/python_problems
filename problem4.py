# written in VS Code with jupyter extension

#https://simpleprogrammer.com/programming-interview-questions/

# How do you find all pairs of an integer array whose sum is equal to a given number? 

#%%
testArray = [2,1,5,8,4,5,4,7,3,9]
target = 5
print('Given array: ' + str(testArray))
print('Given target: ' + str(target))
print('Pairs with sum equal to target: ')

#%%
for i, element in enumerate(testArray,start=0):
    #print(str(i)+ ','+ str(element))
    for j, element2 in enumerate(testArray, start = i):
        if ((element + element2) == target):
            print(str(element)+ ','+ str(element2))
