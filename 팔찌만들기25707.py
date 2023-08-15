from collections import deque

#입력받기
a=int(input())

b=list(map(int,input().split()))

s_b=sorted(b,reverse=True) #정렬하기

q=deque() #큐생성

#큐 배치
for i in range(0,a,2):
    q.append(s_b[i])

for i in range(1,a,2):
    q.appendleft(s_b[i])

#최솟값구하기

s=0

for i in range(0,a-1):
    s=s+abs(s_b[i]-s_b[i+1])

s=s+abs(s_b[0]-s_b[a-1])

print(s)
