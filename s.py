a=[1,2,3,4,5,6]
b=[2,3,1,0,6,7]
i=0
x=(len(a))
while i<=x:
    if a[i]in b:
        continue
    i=i+1
print(a[i])
    