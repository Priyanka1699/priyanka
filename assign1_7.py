
stu_list=[(1,100,'12/12/2018'), (2,101,'11/10/2019'), (3,102,'2/2/2019'), (4,103,'5/5/2018'), (5,104,'8/6/2019')]


choice=1
while choice!=0:
    print()
    
    print("1. Search by book number")
    print("2. Search by student id")
    print("3. Search by date")
    print("0. Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        a=int(input("Enter Bookno  :"))
        l=len(stu_list)
        for i in range(l):
            if a==stu_list[i][1]:
                print("",stu_list[i][1:])
    elif choice==2:
        a=int(input("Enter Id :"))
        l=len(stu_list)
        for i in range(l):
            if a==stu_list[i][0]:
                print(stu_list[i][:2])
    elif choice==3:
        print(stu_list) 
        a=str(input("Enter Date :"))
        l=len(stu_list)
       
        for i in range(l):
            
            if a==stu_list[i][2]:
                print(stu_list[i][:2])
    elif choice==0:
        print("Exit!")
    else:
        print("Invalid choice!!")
print()
