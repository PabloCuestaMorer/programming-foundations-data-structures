from collections import deque

history_stack = deque()
history_stack.append("https://google.com")
history_stack.append("https://linkedin.com")
history_stack.append("https://stackoverflow.com")

# View the top without remove it
top = history_stack[-1]
print(top)
# Pop the top
top = history_stack.pop()
print(top)

