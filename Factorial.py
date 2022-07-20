factorial = 1
num = 8

if num<0:
    print("Factorial does not exist for negative value")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial*=i
    print(f"Factorial of {num} is: {factorial}")
