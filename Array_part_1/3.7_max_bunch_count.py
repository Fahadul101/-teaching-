numbers = []
numbers = input("Enter numbers separated by space: ")

numbers = numbers.split()
size = len(numbers)

for i in range(size):
    numbers[i] = int(numbers[i])

print("List:", numbers)

i = 0
maxCount = 0
while i < size-1:
    currentCount = 1
    j = i+1
    while j < size:
        if numbers[j] == numbers[i]:
            currentCount = currentCount + 1
        else:
            break
        if currentCount > maxCount:
            maxCount = currentCount
        j = j+1
    i = j

print("Number of elements in largest bunch:", maxCount)