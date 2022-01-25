def pattern(n):
    temp = []
    result = []

    for i in range(n):
        if i == n-1:
            temp.append(1)
        else:
            temp.append(0)

    for j in range(n):
        if j == 0:
            temp_new = temp[:]
            result += temp_new
        else:
            temp[-j-1] = temp[-j]+1
            temp_new = list(temp)
            result += temp_new
    return result

x2 = pattern(2)
x3 = pattern(3)
x4 = pattern(4)

print(x2)
print(x3)
print(x4)