a,b=input().split()

a=int(a)
b=int(b)

s=0

if a>=b :
    s=s+a+b
    s=s+(b//10)
else:
    s=s+a+b
    s=s+(a//10)

print(s)    