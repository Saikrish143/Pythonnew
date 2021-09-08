#print(list(set(input().split())))
n=input().split()
n=list(n)
res=[]
for i in n:
    if( i not in res):
        res.append(i)
print(res)

