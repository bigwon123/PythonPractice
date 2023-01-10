L =[]
for i in range(10):
    num = int(input())
    a = num % 42
    L.append(a)

m = set(L)
print(len(m))
