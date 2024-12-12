a = [2,6,4,8,7,9]

for i in range(len(a)):
    for j in range(0, len(a)-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
