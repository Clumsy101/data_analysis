def check_duplicate(name:str):
    n1=[ ]
    for i in name:
        if i in n1:
            return True
        else:
            n1.append(i)
            print(n1)
    return False
 
            
name=str(input("enter the word: "))
if check_duplicate(name):
    print("there is duplicate number")
else:
    print("there is no duplicate number")