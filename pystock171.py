#161
for i in range(100):
    print(i)

#162
for i in range(2002,2051,4):
    print(i)

#163
for i in range(3,31,3):
    print(i)

#164
for i in range(99,-1,-1):
    print(i)

#165
for i in range(10):
    print(i/10)

#166
for i in range(10):
    cal=3*i
    print("3x",i,"=",cal,sep="")

#167
for i in range(1,10,2):
    cal=3*i
    print("3x",i,"=",cal)

#168
sum=0
for i in range(1,11):
    sum= sum+i
print(sum)

#169
sum=0
for i in range(1,11,2):

    sum+=i
print(sum)

#170
sum=1
for i in range(1,11):
    print(i)
    sum=sum*i
    print(sum,"\n")
print(sum)

#171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):   #더 좋은 코드
    print(price_list[i])

#172
for i in range(len(price_list)):
    print(i,price_list[i])

#173
for i in range(0,4):
    print(3-i,price_list[i])

#174
for i in range(1,len(price_list)):
    print(100+10*i,price_list[i])

#175
my_list = ["가", "나", "다", "라"]
for i in range (len(my_list)-1):
    print(my_list[i] ,my_list[i+1])

#176
my_list = ["가", "나", "다", "라", "마"]
for i in range (len(my_list)-2):
    print(my_list[i] ,my_list[i+1],my_list[i+2])

#177
my_list = ["가", "나", "다", "라"]
for i in range (len(my_list)-1):
    print(my_list[3-i],my_list[2-i])

for i in range (3,0,-1):
    print(my_list[i],my_list[i-1])    

#178
my_list = [100, 200, 400, 800]
for i in range(0,3):
    print(my_list[i+1]-my_list[i])

#179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range (len(my_list)-2):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

#180
volatility=[]
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
for i in range(len(low_prices)):
    volatility.append(high_prices[i]-low_prices[i])

print(volatility)

#181
apart=[[101,102],[201,202],[301,302]]
print(apart)

stock=[["시가",100,200,300],["종가",80,210,330]]

stock={
    "10/10":[80,110,70,90],
    "10/11":[210,230,190,200]
    } 
print(stock)

apart = [ [101, 102],
        [201, 202], 
        [301, 302] ]
for i in apart:
    for j in i:
        print(j)
        print("-----")

#186
apart = [ [101, 102], [201, 202], [301, 302] ]
for 층 in apart[::-1]:
    for 호 in 층:
        print(호,"호")

#187
for 층 in apart[::-1]:
    for 호 in 층[::-1]:
        print(호,"호")

#188 #189
for 층 in apart:
    for 호 in 층:
        print(호,"호")

    print("------")

