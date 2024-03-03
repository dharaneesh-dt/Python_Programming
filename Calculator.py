num1=int(input("Enter the value of num 1:"))
num2=int(input("Enter the value of num 2:"))
option=input("""Choose the correct option:
        1.Addition(ADD)
        2.Subration(SUB)
        3.Multipilcation(MUL)
        4.Division(DIV):""")

option=option.lower()
if(option=="add"):
    print("The addition of num1 and num2 is:",num1+num2)
elif(option=="sub"):
    print("The Subraction of num1 and num2 is:",num1-num2)
elif(option=="mul"):
    print("The Multiplication of num1 and num2 is:",num1*num2)
elif(option=="div"      ):
    print("The division of num1 and num2 is:",num1%num2)
else:
    print("The value is invalid.Enter a valid entry")
