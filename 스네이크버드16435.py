n,h=input().split()

n=int(n)
h=int(h)

a=list(map(int,input().split()))

a=sorted(a)

for i in range(n):
    if h>=a[i]:
        h+=1
print(h)