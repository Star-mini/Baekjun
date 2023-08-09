t=input()

t=int(t)

for i in range(t):
    a=list(map(int,input().split()))
    avg=sum(a[1:])/a[0]
    count=0
    for j in range(a[0]):
        if avg<a[j+1]:
            count=count+1
        d=count/a[0]*100 
    print('%.3f' %d+'%')
    