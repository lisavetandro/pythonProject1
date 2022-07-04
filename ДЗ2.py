#дз 1 урок 2
a = input().split()
l = []
for i in range(len(a)):
    l.append(int(a[i]))
l.sort()
print(l[-1])


a = input().split()
l = []
for i in range(len(a)):
    l.append(int(a[i]))
l.sort()
print(l[0])


a = input().split()
l = []
for i in range(len(a)):
    if (i % 3 == 0 and i % 5 != 0 ):
       print([i])