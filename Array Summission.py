#Question -Add elements of an array ,the user should provide the array.
numArray = map(int, input().split())# this statement is used for getting the array from the user


sum_integer = 0

for number in numArray :#loop
    sum_integer=number + sum_integer#increments the value of sum_integer



print(sum_integer) 
