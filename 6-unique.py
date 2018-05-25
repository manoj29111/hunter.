f=int(input())
m=[]
for x in range(0,f):
    a=input()
    m.append(a)    
n=[]
for x in m:
    if x not in n:
       n.append(x)
    else:
        print (x)
        break
