l = []
even_count=0
odd_count=0
a = int(input("Enter elements:"))
print("Enter ",a,"values :")
for i in range(a):
    b = int(input())
    l.append(b)
for i in l:
    if i % 2 == 0:
        even_count+=1

    else:
        odd_count+=1
print("list no.of even is:",even_count)
print("list no.of odd is:",odd_count)
