
user_input=input("do you using lifeline")
if user_input=="yes":
    print("5050")
    if count==0:
        print(option_list[i][i])
        print(ans[i])
        a=int(input("only now time using lifeline"))
        if a==2:
            print("your answer is correct")
            count=count+1
        else:
            print("you ans is wrong")
    else:
        print("you can't use more lifeline")
        b=int(input("choose the answer"))
        if b==solution_list[i]:
            print("your ans is correct")
        else:
            print("your ans is wrong")
else:
    c=int(input("choose the answer"))
    if c==solution_list[i]:
        print("your answer is correct")
    else:
        print("your answer is wrong")
    i=i+1