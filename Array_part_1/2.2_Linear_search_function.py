"""
   At First we create a function liner_search.
   1.Take list and targetValue as a parameters
   2. Run a loop to check the presence of targetValue in List
   3. If it is present then it returns the index of the targetValue
   4. If it is not present, then it returns -1
"""

# TODO: Linear Search Through Functions
def linear_search(list, target):
    for i in list:
        if(i==target):
            return list.index(i)
    return -1

list = [int(x) for x in input().split()]
target = int(input())

print(linear_search(list, target))