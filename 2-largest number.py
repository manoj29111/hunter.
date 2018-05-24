s=int(input())
o=[]
for x in range(0,s):
    p=input()
    o.append(p)
m=[]
for x in o:
    if x not in m:
        m.append(x)
m.sort(reverse=True)
print ("".join(m))
