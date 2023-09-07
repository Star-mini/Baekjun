a=input().split()
b=input().split()       #버거값
c=input().split()       #사이드값
d=input().split()       #음료값

a=list(map(int,a))
b=list(map(int,b))
c=list(map(int,c))
d=list(map(int,d))

#총합값
s=0
s=sum(b)+sum(c)+sum(d)

print(s)

min=min(a) #최솟값

#큰값순서대로 나오게 나열하기
b.sort(reverse=True)
c.sort(reverse=True)
d.sort(reverse=True)


for i in range(min):
    b[i]=b[i]*0.9
for i in range(min):
    c[i]=c[i]*0.9
for i in range(min):
    d[i]=d[i]*0.9

s=sum(b)+sum(c)+sum(d)
s=int(s)
print(s)





