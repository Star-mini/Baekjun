# a=list(input())
# s=0

# for i in range(len(a)):
#     if a[i] == 'Y':
#         a[i]='N'
#         s=s+1
#         #뒤에 배수전부 바꿔주기
#         for j in range(1,len(a)//(i+1)): 
#             if a[(j)*(i+1)] == 'N':
#                 a[(j)*(i+1)] = 'Y'
#             elif a[(j)*(i+1)] == 'Y':
#                 a[(j)*(i+1)] = 'N'
# print(s)

a=list(input())
s=0

for i in range (len(a)):
    if a[i] == 'Y':
        a[i]='N'
        s=s+1
        #뒤에를 배수만큼 바꿔주기
        for j in range(i+1,len(a)-i,i+1):
            if a[i+j] == 'Y':
                a[i+j]='N'
            else:
                a[i+j]='Y'

print(s)


# a=list(input())
# 이거랑
# 배수만큼 더하는거는 그냥 for i in range (i,len(a),i+1):
# 이렇게 해결하였다.

