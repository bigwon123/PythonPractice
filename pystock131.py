for 변수 in [10,20,30]:
    print(변수)

for i in {10, 20, 30}:
    print(i)

data=[10,20,30]
for i in data:
    print("------")

#141
리스트 = [100, 200, 300]
for i in 리스트:
    print(i+10)


#142
리스트 = [100, 200, 300]
for i in 리스트:
    print("오늘의 메뉴:",i)


#143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

#144
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0])

#151
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if int(i)<0:
        print(i)

#152
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i%3==0:
        print(i)

#153
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i%3==0:
        if i<20:
            print(i)

#154
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i)>3:
        print(i)

#155
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i==i.upper():    #i.isupper()
        print(i)
    elif i.islower():
        print(i+"1")

#157
리스트 = ['dog', 'cat', 'parrot']

for i in 리스트:
    first=i[0].upper()
    print(first+i[1:])

for i in 리스트:
    print(i.capitalize())

#158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
    data=i.split(".")
    print(data[0])

#159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    data=i.split(".")
    if data[1]=="h":
        print(i)

for i in 리스트:    
    if i.endswith(".h"):    #두 번째 방법
        print(i)