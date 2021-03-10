import queue

data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put("wewewewe")

data_queue.qsize()
print(data_queue.qsize())

print(data_queue.get())

print(data_queue.qsize())

print(data_queue.get())

print(data_queue.qsize())