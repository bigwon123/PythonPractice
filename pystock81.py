#91~ 100
a={"메로나" : 1000,
    "폴로포": 1200,
    "빵빠레": 1800}

print(a)

a["죠스바"]=1200    #key value 적어주기
a["월드콘"]=1500

print(a)
print(a["메로나"])  #딕셔너리의 인덱싱은 키를 통해서만 가능

a["메로나"]=1300
print(a)
del a["메로나"]
print(a)

#91
inventory={
    "메로나": [300,20],
    "비비빅": [400,3],
    "죠스바": [250,100]
}
print(inventory)
print(inventory["메로나"])
print(inventory["메로나"][1])

inventory["월드콘"]=[500,7]

print(inventory) 

#95
icecream = {'탱크보이': 1200, '폴라포': 1200, 
'빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

print(icecream.keys())
print(list(icecream.keys()))

print(icecream.values())
print(list(icecream.values()))

print(sum(icecream.values()))

new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream) 

#99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result=list(zip(keys,vals)) #zip : 쌍을묶어줌
#but 우리가 원하는건 딕셔너리 타입이므로
result=dict(zip(keys,vals))

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table=dict(zip(date,close_price))
print(close_table)

#101
a=True
print(type(a))  #불리안 타입 boolean

print(3==5)
print(3<5)

x=4
print(1<x<5)

print ((3 == 3) and (4 != 3))

if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")

