# num=[23,14,56,12,19,9,15,25,31,42,43]
# def function(num):
#     i=0
#     even=0
#     odd=0
#     sum=0
#     j=0
#     while i<len(num):
#         m=num[i]
#         if m%2==0:
#             even=even+1
#             sum=sum+m
#         else:
#             odd=odd+1
#             j=j+m
#         i=i+1
#     a=even
#     b=odd
#     print(sum//a)
#     print(j//b)
# function(num)


# num= 2
# sum=0
# while num>0:
#     sum=sum+num%10
#     num=num//10
# print("sum of digit=",sum)



# write a python program to get the frequence of the element in a list .
# input
# my_list=[10,10,10,10,20,20,20,20,40,40,50,50,30]

# import collections
# my_list=[10,10,10,10,20,20,20,20,40,40,50,50,30]
# print("original List:",my_list)
# ctr=collections.Counter(my_list)
# print("Frequency of the elements in the List:",ctr)

# num=[2,4,6,8,10]
# def average(num):
#     i=0
#     sum=0
#     count=0
#     while i<len(num):
#         sum=sum+num[i]
#         i=i//1
#     print(sum)
#     print(i)
# average(num)

num=[45, 34, 10, 36, 12, 6, 80]
def function(num):
    i=0
    sum=0
    while i<len(num):
        sum=sum+1
        avg=sum/len(num)
        i=i+1
    print(sum)
    print(avg)
    print(i)
function(num)