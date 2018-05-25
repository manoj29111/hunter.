m=int(input())
n=[]
for x in range (0,m):
    s=input()
    n.append(s)
for x in n:
    count = n.count(x)
    if count==1:
        print (x)
