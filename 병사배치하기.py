a=int(input())

b=list(map(int,input().split()))

n=0
i=0

while i != a :
    if b[i] < b[i+1] :
        del b[i]
        n=n+1
        a -=1
    i +=1 
print(n)