class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == Node(data):     #셀프에 헤드가 있는지다 여부 None이면 새로 만든다.
            self.head = Node(data)      #None이면 만든다.
            self.tail = self.head       #None이면 만든다.
        else:                           #None이 아닌 경우
            node = self.head            #self.head를 특정 변수에 넣는다
            while node.next:
                node = node.next        #마지막을 찾는다
            new = Node(data)            #찾으면 새로만든다.
            node.next = new             #이전의 next에 있는 주소를 새로만든 node를 가리키게 만든다.
            new.prev = node             #새로 만든 노드가 이전의 node를 기리키게 만든다
            self.tail = new             #tail이 새로만든 node로 바꾼다.

    def desc(self):                     #데이터를 출력하는 출력함수
        node = self.head
        while node:                      #처음부터 끝까지 출력하게 한다.
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False



double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
print(double_linked_list.desc())


node1 = double_linked_list.search_from_head(3)
print(node1.data)


node1 = double_linked_list.search_from_tail(5)
print(node1.data)