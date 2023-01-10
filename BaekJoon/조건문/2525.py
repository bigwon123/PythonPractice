#2525
num1, num2 = map(int, input().split())
num3 = int(input())

hour = num1 + num3//60
min = num2 + num3%60

if min >=60:
    hour=hour+1
    min=min-60
    
if hour >= 24:
    hour = hour-24

print(hour, min)