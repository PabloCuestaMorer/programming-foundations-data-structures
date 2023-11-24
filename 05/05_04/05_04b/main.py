from collections import deque

# 1     --> 1
# 10    --> 2
# 11    --> 3
# 100
# 101
# 110
# 111
# 1000

def print_binary_number(number):
  if 0 >= number:
    return 
  
  queue = deque()
  queue.append(1) #number is at least 1
  for i in range(number):
    binary = queue.popleft()
    print(binary)
    queue.append(binary * 10) #add 0
    queue.append(binary * 10 + 1) #add 1
    
print_binary_number(4)

