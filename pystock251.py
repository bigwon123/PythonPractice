#251
'''
클래스 : 붕어빵 틀과 같은 것, 객체나 인스턴스의 설계도
객체, 인스턴스 : 그 틀로부터(클래스) 만들어진 객체
'''

#252
class Human:    #관례적으로 대문자 사용
    pass

#253
class Human:
    pass

areum=Human()

#254
class Human():
    def __init__(self):
        print("응애응애")
 
areum=Human()

#255
class Human():
    def __init__(self, name, age, sex): #Human의 key는 init 
        self.name=name                  #value는 4개
        self.age=age
        self.sex=sex

areum=Human("아름","25","여자")
print(areum.name)

#256
print(areum.age)
print(areum.sex)

#257
class Human:
    def __init__(self, name, age, sex):
        self.name=name
        self.age=age
        self.sex=sex

    def __del__(self): #소멸자
        print("나의 죽음을 알리지 마라")
    
    def who(self):
        print(f"이름:{self.name} 나이:{self.age}\
    성별:{self.sex}")

    def setInfo(self, name, age, sex):
        self.name=name
        self.age=age
        self.sex=sex

areum=Human("아름이",26,"女")
areum.who()     #Human.who(areum)

#258
areum=Human("",0,"모름")
areum.setInfo("대원","26","남자")
areum.who()

#259
areum=Human("아름",25,'여자')
del(areum)

#260
class OMG:
    def print(self):
        print("Oh my god")

mystock=OMG()
mystock.print()

#261
class Stock:
    pass

#262
class Stock:
    def __init__(self,name,code):
        self.name=name
        self.code=code

삼성=Stock("삼성전자","005930")
print(삼성.name)
print(삼성.code) 

#263
class Stock:
    def __init__(self,name,code):
        self.name=name
        self.code=code
    
    def set_name(self,name):
        self.name=name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)

#264
class Stock:
    def __init__(self,name,code):
        self.name=name
        self.code=code
    
    def set_name(self,name):
        self.name=name

    def set_code(self,code):
        self.code=code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code
 

a = Stock(None, None)
a.set_code("005930")
print(a.code)

print(a.get_code())

#266
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.dividend)

#269
삼성.set_per(12.75)
print(삼성.per)

#270
type=[]
samsung=Stock("삼성전자","005930",15.79,1.33,2.83)
hyundai=Stock("현대차","005380",8.70,0.35,4.27)
lg=Stock("LG전자","066570",317.34,0.69,1.37)

type.append(samsung)
type.append(hyundai)
type.append(lg)

for i in type:
    print(i.code,i.per)

#271
import random

num=random.randint(0,99)

str(num).zfill(5)   #5자리로 채운다 99 -> 00099 zerofill
 

class Account:
    account_count=0 #class variable 

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.bank="sc은행"

        num1=random.randint(0,999)
        num2=random.randint(0,99)
        num3=random.randint(0,999999)
 
        num1=str(num1).zfill(3)
        num2=str(num2).zfill(2) 
        num3=str(num3).zfill(6)
        self.account_number=num1+'-'+num2+'-'+num3

        Account.account_count+=1

    def get_account_num(cls):      #class메소드(객체접근필요x)
        print(cls.account_count)

    def deposit(self,amount):
        if amount >=1:
            self.balance+=amount
            self.deposit_count +=1
            if self.deposit_count%5==0:
                self.balance=(self.balance*1.01)

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount

    def display_info(self):
        print(self.bank)
        print(self.name)
        print(self.account_number)
        print(self.balance)

kim=Account("김민수",100)
lee=Account("이민수",100)
park=Account("박민수",100)
kim.get_account_num()

kim.display_info()

p=Account("파이썬",10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)


















