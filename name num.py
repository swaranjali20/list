a=["amisha","shetal","pihu","shrdha","aayushi"]
i=0
b=[]
while i<len(a):
    count=0
    j=0
    while j<len(a[i]):
        count+=1
        j+=1
    if count%2==0:
        b.append(count)
    i+=1
print(b)
