marks = [
    [7, 7, 9, 8, 8],
    [1, 1, 8, 5, 6],
    [5, 4, 8, 2, 4]
] 
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        j=j+1
    i=i+1
print(sum)

        
    

