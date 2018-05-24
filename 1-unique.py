m=int(input())
n=[]
for y in range(0,m):
    a=input()
    n.append(a)
q=[]
t=[]
for y in n:
    if y not in q:
        q.append(y)
    else:
        t.append(y)
t.sort()
u=[]
for y in t:
    if y not in u:
        u.append(y)
print (u)
