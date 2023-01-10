x = int(input())
sum = 0

for _ in range(int(input())):
    a,b = map(int,input().split())
    sum = sum + a*b

if sum == x:
    print("Yes")
else:
    print("No")


# 쉽게 생각하자 ! 프로그래밍은 논리성이 더 중요