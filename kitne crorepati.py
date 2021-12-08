num=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
def function(num):
    i=0
    c1=0
    c2=0
    c3=0
    while i<len(num):
        if num[i]>10000000:
            c1=c1+1
        if num[i]>100000:
            c2=c2+1
        if num[i]<100000:
            c3=c3+1
        i=i+1
    print("crorepati hai",c1)
    print("lakhpati hai",c2)
    print("dilwale hai",c3)
function(num)
    

    

