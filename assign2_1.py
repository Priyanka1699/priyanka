x=input("Enter String :: ")
for i in x:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        a=i.upper()
        alpha=i.replace(i,a)
        print(alpha)
    else:
        j=ord(i)
        alpha1=chr(j+1)
        print(alpha1)
        
