a,b=input().split()

a=int(a)
b=int(b)

if a==0:
    if b>=45:
        print(0,b-45)
    else:
        print(23,b-45+60)
else:
    if b>=45:
        print(a,b-45)
    else:
        print(a-1,b-45+60)