class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    # 추가 메소드
    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    # 삭제 메소드
    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == item:
                    self.removeItem(item)
                    return
                cur = cur.next
            print("item does not exist in linked list")

    def removeItem(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                nextnode = cur.next.next
                cur.next = nextnode
                break
    # 출력 메소드
    def printlist(self):
        cur = self.head
        print("HEAD:: ", end='')
        while cur is not None:
            print(cur.val, '->', end=' ')
            cur = cur.next
        if cur is None:
            print('empty')

    # linked list size 출력 메소드
    def size(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    # 탐색 메소드
    def search(self, data):
        check = self.head
        for i in range(self.size()):
            if check.val == data:
                print(data, "The data is at the {} index.".format(i+1))
                return None
            check = check.next
        print(data, "Data does not exist in linked list")
        return None
linked = LinkedList(2)

linked.add(3)
linked.add(4)
linked.add(5)
linked.printlist()

linked.remove(3)
linked.printlist()

linked.search(5)
print(linked.size())