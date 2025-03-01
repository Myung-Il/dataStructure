# 큐는 먼저 들어온 요소를 가장 먼저 꺼내주는 배열이다
# [ ...요소...] 파이썬에서는 이를 리스트로 표현하기 때문에 맨 앞의 요소를 꺼내면
# 바로 뒤 요소를 하나씩 앞으로 당겨줘야하기때문에 남아 있는 요소의 수만큼 연산 수가 증가한다
# 이 시간을 줄이기 위한 방법으로 원형 큐가 있다
# 단점은 큐의 크기가 정해져 있다

# 하지만 나는 그 단점을 없애기 위해서 크기에 제한을 두지 않기 위해서
# 선형이 아닌 비선형으로 만들었다
# 문제는 이렇게 만든 순간부터 원형 큐가 아니라 큐 트리가 된다는 것이다
# 그래도 만들었으니까 그냥 두기로 했다

# 원형은 나중에 만들도록 하겠다

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def MT(self):return self.size==0

    def append(self, item):
        if self.MT():
            self.head = self.tail = Node(item)
        else:
            node = Node(item)
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def popleft(self):
        if self.MT():return "비어 있습니다"
        else:
            node = self.head.item
            self.head = self.head.next
            self.size -= 1
            return node
    
    def __str__(self):
        if self.MT():return "비어 있습니다"
        else:
            node = self.head
            l = f"[{node.item}"
            while node.next:
                node = node.next
                l += f", {node.item}"
            return l + "]"

q = Queue()
print(q)

q.append(5)
q.append(8)
q.append(7)
q.append(2)
q.append(3)
print(q)

q.popleft()
print(q)

q.popleft()
print(q)