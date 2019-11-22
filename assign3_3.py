def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


choice=1
while choice!=0:
    print()
    print("Select Operation ::")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.division")
    print("0.Exit")
    choice=input("Enter Choice 1/2/3/4/0 ::")
    num1=input("Enter First Number ::")
    num2=input("Enter Second Number ::")
    
    
    if choice=='1':
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice=='2':
        print(num1,"-",num2,"=",sub(num1,num2))
    elif choice=='3':
        print(num1,"*",num2,"=",mul(num1,num2))
    elif choice=='4':
        print(num1,"/",num2,"=",div(num1,num2))
    elif choice=='5':
        print("Exit!!!!")
    else:
        print("Invalid Choice!")

    




    




    




    

