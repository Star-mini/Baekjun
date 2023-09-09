a=input()
a=int(a)

b=input().split()
b=list(map(int,b))

a_s=b[0]
b_s=b[1]

i=2

#가재 놓기
while i < a:
    if a_s <= b_s:
        a_s=a_s + b[i]
        i=i+1
    else:
        b_s=b_s + b[i]
        i=i+1

#두저울의 차이
a_b=abs(a_s-b_s)

split=[100,50,20,10,5,2,1]

s=0     #횟수

for i in range(7):
    s=s+(a_b//split[i])
    a_b=a_b-(a_b//split[i])*split[i]

print(s)