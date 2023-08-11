a=1
b=1
c=1
test_case=1

while a!=0 or b!=0 or c!=0 :
    a,b,c=map(int,input().split())

    if a==0 and b==0 and c==0:
        break 

    d=c//b
    e=c%b

    if e > a:
        e=a

    print('Case %d: %d'%(test_case,(d*a)+e))
    test_case=test_case+1