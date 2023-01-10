# 221
import datetime
import math


def print_reverse(a):
    print(a[::-1])


print_reverse("MoonSungDae")

# 222


def print_score(a):
    print(sum(a)/len(a))


print_score([1, 2, 3])

# 223


def print_even(a):
    for i in a:
        if i % 2 == 0:
            print(i)


print_even([1, 3, 2, 10, 12, 11, 15])

# 224


def print_keys(a):
    val = a.values()
    for i in val:
        print(i)


print_keys({"이름": "김말똥", "나이": 30, "성별": 0})

# 225


def print_value_by_key(a, key):
    print(a[key])  # 인덱싱은 문자열로도 가능하다


my_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]}

print_value_by_key(my_dict, "10/26")

# 226


def print_5xn(string):
    # print(string[0:5])
    # print(string[5:10])
    length = len(string)/5
    length = int(length)
    for i in range(length):
        print(string[5*i:5*(i+1)])


print_5xn("hello my name is daewon")

# #227


def print_mxn(string, i):
    length = len(string)/i
    length = math.ceil(length)

    for j in range(length):
        print(string[j*i:(j+1)*i])


print_mxn("아이엠어보이유알어걸", 4)

# 228


def calc_monthly_salary(annual_salary):
    money = (annual_salary/12)
    print(int(money))


calc_monthly_salary(120)

# 229
# 232


def make_url(a):
    return "www."+a+".com"


b = make_url("naver")
print(b)

# 233


def make_list(num):
    var = []
    for i in num:
        var.append(i)
    print(var)


make_list("abcd")

# 234


def pickup_even(a):
    b = []  # 리스트 할당
    for i in a:  # a에대한 인덱싱
        if int(i % 2) == 0:
            b.append(i)  # 리스트b에 append
    print(b)


pickup_even([3, 4, 5, 6, 7, 8])

# 235


def convert_int(src):
    src = src.replace(",", "")
    src = int(src)
    # src1,src2,src3=src.split(",")
    # print(src1,src2,src3)
    # res=int(src1+src2+src3)
    return src


result = convert_int("1,234,567")
print(result)

# 241

x = datetime.datetime.now()
print(x)

# 242
now = datetime.datetime.now()
print(now, type(now))  # 모르는 타입이다 라고 이해하기

# 243
delta = datetime.timedelta(days=1)  #days=1 : 다음 날
print(now+delta)

#244
import datetime

now=datetime.datetime.now()
print(now,type(now))
a= now.strftime("%Y:%D:%H:%M:%S") # 현재 년, 일, 시, 분, 초
print(a,type(a))

#245
import datetime

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

#246
import time
import datetime

print("hello")
time.sleep(3) #3초를 쉬어라
print("again") 

i=0
while i<5:
    now=datetime.datetime.now()
    print(now)
    time.sleep(0.5)
    i=i+1
    
#247
#모듈을 임포트하는 네가지 방식

import os               #os.rename() os안에있는 rename함수출력
from os import rename   #rename() os를 붙이긴싫다  
from os import *        #os 안에있는 함수, 클래스, 변수를 다!
import os as myos       #이름을 바꿔서 사용하고싶을때

#248
import os
ret=os.getcwd()     #현재 작업경로의 위치
print(ret,type(ret))

#249
os.rename("C:\\Users\\User\\Desktop\\연수휴직계획.txt",
"C:\\Users\\User\\Desktop\\연수휴직계획.txt")

#250
import numpy
for i in numpy.arange(0,5,0.1):
    print(i)