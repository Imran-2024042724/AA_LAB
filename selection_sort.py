a = [2,6,7,8,4,9]


for i in range(len(a)-1):
    index = i
    for j in range(i+1, len(a)):
        if a[j]<a[i]:
            index = j
    a[i], a[index] = a[index], a[i]

print(a)
