#Lifo_Queue(last in first out)

import queue
data_queue = queue.LifoQueue()

data_queue.put("funcoding")
data_queue.put("yyyyy")

print(data_queue.qsize())

print(data_queue.get())
print(data_queue.get())