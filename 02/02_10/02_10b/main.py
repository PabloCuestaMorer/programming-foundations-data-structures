#Complexity O(N log(N))
def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None 
    sorted_list = sorted(my_list)
    return sorted_list[1]

#Complexity O(event)
def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None 
    
    smallest = float('inf')
    smallest2 = float('inf')
    for num in my_list:
        if num < smallest:
            smallest2 = smallest
            smallest = num
        elif(num < smallest2):
            smallest2 = num
            
    return smallest2

print(find_second_smallest_v2([5, 8, 3, 2, 6]))

