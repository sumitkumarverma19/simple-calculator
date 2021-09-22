# To create a Simple calculator

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))

print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("Press 5 to find power")
print("Press 6 to find modulus")
n=int(input())

if(n==1):
    c=a+b
    print(c)
elif(n==2):
    c=a-b
    print(c)
elif(n==3):
    c=a*b
    print(c)
elif(n==4):
    c=a/b
    print(c)
elif(n==5):
    c=a**b
    print(c)
elif(n==6):
    c=a%b   
    print(c)
else:
 print("number not matched")


    
    