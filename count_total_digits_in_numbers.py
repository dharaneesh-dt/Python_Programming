#Count the total number of digits in a number
#Write a program to count the total number of digits in a number using a while loop.
#For example, the number is 75869, so the output should be 5.

num=int(input("enter the numbers:"))
num1=num
count=0
while(num!=0):
    num=num//10
    count=count+1
print(f"the total no of digits in {num1} is {count}")
