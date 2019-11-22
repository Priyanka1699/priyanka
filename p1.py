FoodList=["rice","pavbhaji","paneer","puribhaji","vadapav"]
print(FoodList)
Items=["brush","soap","shampoo","toothpest","mug"]
print(Items)
FoodList[3]="misalpav"
print(FoodList)
print(FoodList[0:3])
FoodList.append("misal")
print(FoodList)
FoodList.append("hanger")
print(FoodList)
print(Items)
FoodList.insert(2,"noodles")
print(FoodList)
FoodList.pop(-2)
print(FoodList)
FoodList+=Items
print(FoodList)
print(len(FoodList))
if "shampoo"  in  FoodList:
    FoodList.remove("shampoo")
    print(FoodList)
if "trimeer" not in FoodList:
    FoodList.append("trimmer")
    print(FoodList)
del(FoodList)





