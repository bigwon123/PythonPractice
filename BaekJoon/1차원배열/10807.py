'''n = int(input())
list = []
cnt = 0
list = input().split()

print(list)

v = int(input())

if v == list:
    cnt += 1

print(cnt)

n= int(input())
L = list(map(int,input().split()))
v = int(input())
cnt =0 

for i in L:
    if i == v:
        cnt+=1

print(cnt)'''

n= int(input())
L = list(map(int,input().split()))
v = int(input())

print(L.count(v))