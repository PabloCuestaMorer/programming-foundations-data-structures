from collections import deque

printer_queue = deque()

printer_queue.append("Doc1")
printer_queue.append("Doc2")
printer_queue.append("Doc3")
printer_queue.append("Doc4")
printer_queue.append("Doc5")

print(printer_queue)

printer_queue.popleft()

print(printer_queue)

printer_queue.pop()

print(printer_queue)


print("Print element in FIFO order:")
for doc in printer_queue:
  #Like this u can pop it also in FIFO order
  print('-', doc)