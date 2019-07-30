"""check to lists if the lists containt different items,
output them into the third list """

List_A = ["apple", "banana", "pear", "mango", "Watermelon"]
List_B = ["apple", "banana", "pear", "melon"]
List_C = []

# if the item is not in list_a and list_b then add it to List C 
IfNotInB = [item for item in List_A if item not in List_B]
IfNotInA  = [item for item in List_B if item not in List_A]


List_C.append(IfNotInB)
List_C.append(IfNotInA)
print(List_C)
