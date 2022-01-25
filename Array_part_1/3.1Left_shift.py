#Shift Left k Cells
"""
Consider an array named source. Write a method/function named shiftLeft( source, k)
that shifts all the elements of the source array to the left by 'k' positions. You must
execute the method by passing an array and number of cells to be shifted. After calling
the method, print the array to show whether the elements have been shifted properly.
Example:
source=[10,20,30,40,50,60]
shiftLeft(source,3)
After calling shiftLeft(source,3), printing the array should give the output as:
[ 40, 50, 60, 0, 0, 0 ]

"""


def shiftLeft(source, k):
    #!shifting the values in the array to left by k positions
    for i in range (0, len(source)):
        if((i-k)>=0):
            source[i-k] = source[i]

    #!placing 0's in the places where values are already shifted to left
    for i in range (len(source)-k, len(source)):
        source[i] = 0
    return source 

source = [int(x) for x in input().split()] 
k = int(input()) 
print(shiftLeft(source, k))            