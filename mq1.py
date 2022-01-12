a=[2,4,3]
b=[5,6,4]
c=" "
d=" "
sum=0
i=1
while i<=len(a):
    c=c+str(a[-i])
    d=d+str(b[-i])
    i=i+1
sum=int(c)+int(d)
print(sum)
k=str(sum)
sum_k=" "
z=[]
l=-1
while l>=-(len(k)):
    c=k[l]
    d=int(c)
    x=z.append(d)
    l=l-1
print(z)
