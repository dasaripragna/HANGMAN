# l=[3,6,9,1]
# def maxDiff(a):
# a = len(l)
# arr = []
# for i in range(a-1):
#     for j in range(i+1, a):
#         if a[j] > a[i]:
#             diff = a[j] - a[i]
#             arr.append(diff)
# return (max(arr))
n=[1,2]
n1=[3,4]
s=n+n1
sum=0
i=0
c=0
while i<len(s):
	sum=sum+s[i]
	c=c+1
	a=sum/c
	i=i+1
print(a)