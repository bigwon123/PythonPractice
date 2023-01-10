#201
def print_coin():
    print("빗코코")

# print_coin()

# #203
# for i in range(100):
#     print_coin()

#204
def print_coins():
    for i in range(10):
        print_coin()
print_coins()

#210
def print_with_smile(a):
    print(a+":D")

b="hello"
print_with_smile(b)

#216
print_with_smile("안녕하세요")

#217
def print_upper_price(price):
    print(price*1.3)
print_upper_price(1000)

#218
m=int(input("입력:"))
n=int(input("입력:"))

def print_sum(a,b):
    print(a+b)

print_sum(m,n)



def print_multiply(a,b):
    print(a*b)

print_multiply(5,10)

#219
def print_arithmetic_operation(m,n):
    print(f"{m}+{n}={m+n}")
    print(f"{m}-{n}={m-n}")
    print(f"{m}*{n}={m*n}")
    print(f"{m}/{n}={m-n}")

print_arithmetic_operation(5,10)

#220
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

print_max(3,5,2)

