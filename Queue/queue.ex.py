queue_list =list()

def enqueue(data):
    queue_list.append(data)
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)
print(len(queue_list))

print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())