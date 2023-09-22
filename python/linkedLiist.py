class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value): 
        new_node = Node(value)
        # 처음에만 head,tail가 new_node를 가리키게 한다.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    def insert(self, idx, value):
        new_node = Node(value)

        # 인덱스가 0이면 새로운 노드를 헤드로 설정
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx - 1):
                if current is None:
                    raise IndexError("인덱스가 범위를 벗어납니다.")
                current = current.next
            if current is None:
                raise IndexError("인덱스가 범위를 벗어납니다.")
            
            new_node.next = current.next
            current.next = new_node
    def remove(self, idx):
        # 인덱스가 0이면 헤드 노드를 제거해야 함
        if idx == 0:
            if self.head is not None:
                self.head = self.head.next
            else:
                raise IndexError("인덱스의 범위를 벗어납니다.")
        else:
            current = self.head
            prev = None
            for _ in range(idx):
                if current is None:
                    raise IndexError("인덱스가 범위를 벗어납니다.")
                prev = current
                current = current.next
            if current is None:
                raise IndexError("인덱스가 범위를 벗어납니다.")
            
            # 이전 노드의 next를 현재 노드의 next로 설정하여 노드를 제거
            prev.next = current.next





ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.get(0)
ll.get(1)
ll.insert(1,5)
print(ll.get(1))