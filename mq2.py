n = [0,1,2,2,3,0,4,2]
i=0
s1=[]
s2=[]
count=0
while i<len(n):
	if n[i]==2:
		s1.append(' _')
	else:
		s2.append(n[i])
		count=count+1
	i=i+1
s=s1+s2
print(s)

# output=[' _', ' _', ' _', 0, 1, 3, 0, 4]