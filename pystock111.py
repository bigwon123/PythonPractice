# #111
# data=input("")
# print(data*2)

# #112
# a=int(input())
# print(int(a)+10)

# #113
# b=input()
# if int(b)%2==0:
#     print("짝수")
# else:
#     print("홀수") 

#114
# c=input()
# c=int(c)
# d=c+20
# if d>255:
#     print(255)
# else:
#     print(d)

# #116
# a=input("현재 시간:")
# if a[-2:] =="00":
#     print("정각입니다")
# else:
#     print("정각이 아닙니다")

# #117
# fruit=["사과","포도","홍시"]
# a=input("좋아하는 과일은? ")
# if a in fruit:       # a가 fruit 안에(in) 있냐?
#     print("정답입니다")
# else:
#     print("오답")

#118
# warn_investment_list = ["Microsoft", "Google", 
# "Naver", "Kakao", "SAMSUNG", "LG"]
# item=input("종목 입력: ")
# if item in warn_investment_list:
#     print("투자 경고 종목입니다")
# else:
#     print("ㄱㅊ")

# #119
# fruit = {"봄" : "딸기", "여름" : "토마토", 
# "가을" : "사과"}

# a= fruit.keys()
# print(a)
# b=fruit.values()
# print(b)

#121
# a=input()
# if a.islower()==True:
#     print(a)
# else:
#     print(a.upper())

#122
# score=input()
# score=int(score)
# if (80<score | score<=100):
#     print("A")
# elif (60<score|score<=80):
#     print("B")
# elif (40<score|score<=60):
#     print("C")
# else:
#     print("F")

#123
# data=input("입력: ")
# tokens=data.split()
# amount,currency=tokens

# 환율 = {"달러": 1167, 
#         "엔": 1.096, 
#         "유로": 1268, 
#         "위안": 171}

# print(float(amount)*환율[currency],"원")

#124
# data=input()
# num1,num2,num3=data.split()

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)

#125
# number=input()
# num=number.split("-")
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")

#126
# data=input("우편번호: ")
# data2=data[:3]
# if data2 in ["010","011","012"]:
#     print("강북구")
# elif data2 in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")

#127
# data=input("주민등록번호: ")
# tokens=data.split("-")
# data2=tokens[1]
# if data2[0]=="1" or data2[0]=="3":
#     print("남자")
# else:
#     print("여자")

#128
# jumin=input("주민등록번호: ")
# data=jumin.split("-")
# data2=data[1]
# if 0 <= int(data2[1:3]) <= 8:
#     print("서울입니다")
# else:
#     print("서울이 아닙니다")

#129
a=input("주민등록번호:")
data1,data2=a.split("-") # data=data.replace("-","")
print(data1,data2)
print(type(data1))
print(type(data2))
cal1=int(data1[0])*2+int(data1[1])*3+int(data1[2])\
    *4+int(data1[3])*5+int(data1[4])*6+int(data1[5])\
    *7+int(data2[0])*8+int(data2[1])*9+int(data2[2])\
    *2+int(data2[3])*3+int(data2[4])*4+int(data2[5])*5
cal1=cal1%11
print(cal1)
cal2=11-cal1
print(cal2)
print(f"계산식은{cal2}, 뒷자리는 {data2[6]}입니다.")
if cal2 == int(data2[6]):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

#130
import requests
btc = requests.get\
    ("https://api.bithumb.com/public/ticker/")\
        .json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")