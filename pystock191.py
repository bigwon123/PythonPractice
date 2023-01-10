#191~194
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result=[ ]
for i in data:
    sub=[]
    for j in i:     #j=0 이 아니라 j= 초기값이 처음[0]이다.
        sub.append(j*1.00014)
    result.append(sub)

print(result) 

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    print(i[3])
print("\n")
#196
for i in ohlc[1:]:
    if i[3]>150:
        print(i[3])

for i in ohlc[1:]:
    close_price=i[3]
    if close_price>150:
        print(close_price)        

#198
volatility=[]
for i in ohlc[1:]:
    volatility.append(i[1]-i[2])

print(volatility)    

for i in ohlc[1:]:
    if i[0]<i[3]:
        print(i[3]-i[0])
        
num=[]
for i in ohlc[1:]:
    num.append(i[3]-i[0])
    print(num)
sum=num[0]+num[1]+num[2]
print(sum)