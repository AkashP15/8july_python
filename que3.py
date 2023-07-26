# Write a Python program to get the Fibonacci series of given range.

num1,num2=0,1

for i in range (10):
    print(num1,end=" ")
    result=num1+num2

    num1=num2
    num2=result

    