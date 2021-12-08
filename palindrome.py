name=["m","o","m"]
d=[]
i=0
j=len(name)-1
while i<len(name):
    if name[i]==name[j]:
        d.append(name[j])
        i=i+1
        j=j-1
if name==d:
    print("it is palindrom")
else:
    print("it is not palindrom")
    
