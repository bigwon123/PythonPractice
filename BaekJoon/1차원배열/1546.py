n = int(input())
L = list(map(int,input().split()))
m = max(L)

for i in range(n):
    L[i] = L[i]/m*100

print(sum(L)/len(L))