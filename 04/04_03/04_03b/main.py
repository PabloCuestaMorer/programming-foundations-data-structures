set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}
print("Set_A", set_A)
print("Set_B", set_B)
print("------------------------")

#Union both without duplicates
union_set = set_A.union(set_B)
print("Union", union_set)

#Entries in both sets
intersection_set = set_A.intersection(set_B)
print("Intersection:", intersection_set)

#Difference remove one set from another (here substract B from A)
difference_set = set_A.difference(set_B)
print("Difference:", difference_set)

#Symmetric difference: elements uniques in both sets. All the items they do not share
symmetric_difference_set = set_A.symmetric_difference(set_B)
print("Symmetric_difference:", symmetric_difference_set)