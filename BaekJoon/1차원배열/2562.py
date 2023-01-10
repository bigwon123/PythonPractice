max = 0
L = []
for i in range(9):
    num = int(input())
    L.append(num)
    if num > max:
        max = num
    
print(max)
print(L.index(max)+1)