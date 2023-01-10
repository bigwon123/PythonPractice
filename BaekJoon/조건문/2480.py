n1,n2,n3 = map(int,input().split())
max=0
if n1==n2==n3:
    print(10000+n1*1000)

elif n1==n2!=n3:
    print(1000+n1*100)
elif n2==n3!=n1:
    print(1000+n2*100)
elif n1==n3!=n2:
    print(1000+n1*100)

else :
    if n1>=n2:
        max=n1
        if n1<n3:
            max=n3
            print(max*100)
        else:
            print(max*100)
    elif n1<n2:
        max=n2
        if n2<n3:
            max=n3
            print(max*100)
        else:
            print(max*100)

'''
a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c))
'''

    