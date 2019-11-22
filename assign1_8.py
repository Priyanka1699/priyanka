def sort_as_firstElement_list(tuple_list):
    return(sorted(tuple_list,key = lambda x:x[0]))
def sort_as_secondElement_list(tuple_list):
    return(sorted(tuple_list,key = lambda x:x[1]))
def sort_as_lastElement_list(tuple_list):
    return(sorted(tuple_list,key = lambda x:x[-1]))

tuple_list=[(2,'Archana',800,60),(1,'Radha',203,10),(5,'Priyanka',332,40),(4,'Pooja',170,20),(3,'Laxmi',421,30)]
print("Original List=",tuple_list)
print("Sort according to last Element =",sort_as_lastElement_list(tuple_list))
print("Sort according to 2nd Element =",sort_as_secondElement_list(tuple_list))
print("Sort according to 1st Element =",sort_as_firstElement_list(tuple_list))
