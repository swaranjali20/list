num=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
count=0
while i<len(num):
    if num[i]%2==0:
        print(num[i],"even")
    elif num[i]%2!=0:
        print(num[i],"odd")
        count=count+num[i]
        sum=sum+num[i]
    i=i+1
print(count)
print(sum)
print(sum//i)


 



