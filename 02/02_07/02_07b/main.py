# Linear Search
my_list = [8, 5, 0, 3, 9, 7]
LOOKING_FOR = 7

def search(item, list):

  for element in list:
    if element == item:
      return True
  
  return False

print(search(LOOKING_FOR, my_list))

ITEM_INDEX = my_list.index(LOOKING_FOR)
print('Item is at index:', ITEM_INDEX)
