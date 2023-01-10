n = int(input())
a = str(n)
cnt = 0


while True:

    if int(a) < 10:
       a = '0'+str(a)


    a=str(a)
    A = int(a[0])
    B = int(a[1])
    sum = A+B
    print(a[0],a[1],"이고, 1의자리와 10의자리를 더하면 :",sum)

    new_num = B*10 + sum%10
    print("1의자리와 sum을 더한 new num :",new_num)
    cnt += 1
    print("cnt",cnt,"번째")
    if n==new_num:
        break
    
    a= int(a)
    a = new_num
print("사이클의 길이는",cnt,"입니다.")
    
