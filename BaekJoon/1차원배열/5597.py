student = [i for i in range(1,31)] #list comprehension
for _ in range(28):
    num = int(input())
    student.remove(num)

print(min(student))
print(max(student))

# 예외인 소수의 값을 얻으려면 전체에서 다수를 빼는 (remove)
# 방법도 유용함!