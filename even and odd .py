num=[23,14,56,12,9,15,25,31,42,43]
i=0
sum=0
while i<len(num):
    if num[i]%2==0:
        print(num[i],"even number")
    if num[i]%2!=0:
        print(num[i],"odd number")
    if num[i]>i:
        print(num[i],"positive")
    if num[i]<i:
        print(num[i],"negative")
    else:
        print("zero")
    i=i+1



        





    

