# n = int(input())
# p = list(map(int, input().split()))
# count = 0
# for i in range(1,n):
#     if max(p[:i]) < p[i] or min(p[:i]) > p[i]:
#         count+=1
# print(count)




n,k = map(int,input().split())
marks = list(map(int,input().split()))
z = []
for i in marks:
    if i >= marks[k-1] and i>0:
        z.append(i)
print(len(z))






