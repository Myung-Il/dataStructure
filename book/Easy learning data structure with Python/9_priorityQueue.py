# 우선 순위 큐는 뭘 넣든지 순서대로 정리해서 숫자를 뽑아낸다
# 크고 작은 순서는 만드는 과정에 따라 바뀐다

# 나는 이 우선 순위 큐를 효율적으로 만들기위해서 힙을 사용할 것이다

import heapq

heap = []
for elm in [3, 7, 5, 8, 9, 2, 1, 6, 4]:
    heapq.heappush(heap, -elm)
print([-val for val in heap])

print(-heapq.heappop(heap))
print("최대값 :", [-val for val in heap])

print(-heapq.heappop(heap))
print("최대값 :", [-val for val in heap])



# 아래 코드는 아래 조건을 구성으로 GPT에게 물어본 결과다

# 힙 트리를 짜는데 조건이 있어
# 1. heapq를 사용하지 않는다
# 2. list를 사용하지 않고 class node 구현해서 만든다
# 3. 코드는 단순 효율적으로 만든다
# 위 3가지를 지켜줘
# 
# 그리고 기능은
# append와 maxpop 이렇게
# 2가지만 만들어줘

class Node:
    """힙 트리의 노드 정의"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # 부모 노드 추가

class MaxHeap:
    """클래스 기반 최대 힙 구현"""
    def __init__(self):
        self.root = None
        self.size = 0

    def _find_insert_position(self):
        """완전 이진 트리를 유지하며 삽입할 위치 찾기 (BFS)"""
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                return node, "left"
            elif not node.right:
                return node, "right"
            queue.append(node.left)
            queue.append(node.right)

    def _bubble_up(self, node):
        """삽입 후, 최대 힙 조건을 만족하도록 조정"""
        while node.parent and node.value > node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value  # Swap
            node = node.parent

    def append(self, value):
        """값을 힙에 추가"""
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            parent, side = self._find_insert_position()
            if side == "left":
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self._bubble_up(new_node)
        self.size += 1

    def _find_last_node(self):
        """완전 이진 트리에서 마지막 노드 찾기"""
        queue = [self.root]
        last = None
        while queue:
            last = queue.pop(0)
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)
        return last

    def _bubble_down(self, node):
        """삭제 후, 최대 힙 조건을 만족하도록 조정"""
        while node.left:
            larger_child = node.left
            if node.right and node.right.value > node.left.value:
                larger_child = node.right
            if node.value < larger_child.value:
                node.value, larger_child.value = larger_child.value, node.value
                node = larger_child
            else:
                break

    def maxpop(self):
        """최대값 제거 후 반환"""
        if not self.root:
            return None
        max_value = self.root.value
        if self.size == 1:
            self.root = None
        else:
            last_node = self._find_last_node()
            self.root.value = last_node.value  # 루트 값 교체
            if last_node.parent.left == last_node:
                last_node.parent.left = None
            else:
                last_node.parent.right = None
            self._bubble_down(self.root)
        self.size -= 1
        return max_value

    def print_heap(self):
        """힙의 구조를 출력"""
        if not self.root:
            print("Heap is empty")
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(f"({node.value})", end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

# ✅ 사용 예시
heap = MaxHeap()
heap.append(10)
heap.append(5)
heap.append(15)
heap.append(3)
heap.append(7)
heap.append(12)

heap.print_heap()  # 힙 구조 출력
print(heap.maxpop())  # ✅ 15 (최대값 삭제)
heap.print_heap()
print(heap.maxpop())  # ✅ 12
heap.print_heap()

# 원래는 내 손으로 heapq를 사용하지 않고 만들고 싶었으나
# 너무 어려워져서 포기했다