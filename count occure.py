list1=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a","t","g","a"] 
list2=[]
i=0
while i<len(list1):
    count=1
    j=0
    while j<len(list1):
        if list1[j]==list1[i]:
            count+=1
        j+=1
    if list1[i] in list2:
        i+=1
        continue
    list2.append(list1[i])
    print (list1[i],"",count)
i+=1
print (list2)

