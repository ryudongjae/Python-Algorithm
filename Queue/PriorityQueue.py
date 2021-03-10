import queue

data_queue = queue.PriorityQueue()

data_queue.put((10,"Korea"))
data_queue.put((5,1))
data_queue.put((15,"yyyy"))

print(data_queue.qsize())

print(data_queue.get())
print(data_queue.get())
print(data_queue.get())