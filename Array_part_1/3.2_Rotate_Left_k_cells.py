#2. Rotate Left k cells
"""
Consider an array named source. Write a method/function named rotateLeft( source, k)
that rotates all the elements of the source array to the left by 'k' positions. You must
execute the method by passing an array and number of cells to be shifted. After calling
the method, print the array to show whether the elements have been shifted properly.
Example:
source=[10,20,30,40,50,60]
rotateLeft(source,3)
After calling rotateLeft(source,3), printing the array should give the output as:
[ 40, 50, 60, 10, 20, 30]
"""
def rotateLeft(source,K):
  n=len(source)  #!length of the given array source 
  i = 0  #starting index 
  temp_arr=[] #temporary array 
  while (i < K):
    temp_arr.append(source[i]) #!append everything in temp array 
    i = i + 1
  i = 0
  while (K < n):
    source[i] = source[K] #!rotateLeft by k position 
    i = i + 1
    K = K + 1
  source[:] = source[: i] + temp_arr
  return source 

source = [10, 20, 30, 40, 50, 60]
print("After calling rotateLeft(source,3) : ", end=' ')
print(rotateLeft(source, 3))