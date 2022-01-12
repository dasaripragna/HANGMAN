# def firstMissingPositive(nums):
#     n = 1
#     s = set(nums)
#     while n in s:
#         n += 1
#     return n
# a=[1,5,3]
# print()

def a(num):

    for i in range(len(num)):
        while 0 <= num[i] - 1 < len(num) and num[num[i]-1] != num[i]:
            tmp = num[i] - 1
            num[i], num[tmp] = num[tmp], num[i]
    for i in range(len(num)):
        if num[i] != i + 1:
            return i + 1
    return len(num) + 1

num = [6,7,8,2,3]
print(a(num))
