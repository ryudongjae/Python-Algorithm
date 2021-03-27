class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,data):
        self.head = Node(data)

    #추가 메소드
    def add(self,data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    #삭제 메소드
    def remove(self,data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == data:
                    self.removeData(data)
                    return
                cur = cur.next
            print("data does not exist in linked list")

    def removeData(self,data):
        cur = self.head
        while cur.next is not None:
            if cur.next.data == data:
                nextNode = cur.next.next
                cur.next = nextNode
                break

    #출력메소드
    def printlist(self):
        cur = self.head
        print("HEAD:: ",end='')
        while cur is not None:
            print(cur.data, '->',end=' ')
            cur = cur.next
        if cur is None:
            print('empty')


    #linked list size 출력 메소드
    def size(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    #탐색메소드
    def search(self,data):
        check = self.head
        for i in range(self.size()):
            if check.val == data:
                print(data,"The data is at the {} index".format(i+1))
                return None
            check = check.next
        print(data,"Data does not exist in linkd list")
        return None