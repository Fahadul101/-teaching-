# Linear Search
"""
    1.Traverse the given list using a loop
    2. In every iteration, compare the targetvalue 
		a. match print.
        b. without match -1
pseudo-code:
for each element in the array:
          if element == targetValue
			print(indexOf(targetValue)
	otherwise Not found.

"""

# TODO:Naive way
li = [int(x) for x in input().split()] #! Taking space sepatated input from user.
targetValue = int(input()) #user input for target Value
found = False
for i in li:
    if(i==targetValue): #if we found the target value
        print(li.index(i)) #print the target value
        found = True #! set found as true as we found the target value
        break #Since we found the target value we break out of the loop
if found is False: #if we did not found the target value
    print(-1)




