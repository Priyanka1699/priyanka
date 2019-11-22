m1=int(input("Enter marks for 1st subject :: "))
m2=int(input("Enter marks for 2nd subject :: "))
m3=int(input("Enter marks for 3rd subject :: "))


if m1>=40 and m2>=40 and m3>=40:
    per=(m1+m2+m3)/3
    print("Pass ::",per)
elif m1>=32 and m2>=40 and m3>=40:
    grace=40-m1
    per=round(m1+m2+m3+grace)/3
    print("Percentage ::",per)
elif m1>=40 and m2>=32 and m3>=40:
    grace=40-m2
    per=round(m1+m2+m3+grace)/3
    print("Percentage ::",per)
elif m1>=40 and m2>=40 and m3>=32:
    grace=40-m3
    per=round(m1+m2+m3+grace)/3
    print("Percentage ::",per)
else:
    print("Fail!!!!")
