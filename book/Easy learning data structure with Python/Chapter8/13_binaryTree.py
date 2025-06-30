# 트리는 선형 구조와는 다르게 계층적인 구조를 가진다
# 모든 부모 노드가 0~2개까지의 자식 노드를 가지는 형태를 이진 트리라고 한다
'''
[ 종류 ]
포화 이진 트리 : 모든 계층이 꽉 찼을 때
완전 이진 트리 : 모든 노드가 순서대로 채워져 있을 때, (queue)
기타 이진 트리 : 꽉 채우지도 순서대로도 아닐 때

[ 성질 ]
노드의 갯수 : sigma(i=1 to h)2^(i-1) = 2^h-1
계층의 높이 : ceil(log2(i+1)) <= h

[ 표현 ]
배열 표현법
    = [_, A, B, C, D, E, F, _] : 완전 이진 트리
    = [_, A, B, _, D, _, _, _] : 경사 이진 트리

링크 표현법
    =             [*[A]*]
          [*[B]*]         [*[C]*]
      [*[D]*] [*[E]*] [*[F]*]

    =         [*[A]*]
          [*[B]*]
      [*[D]*]
'''

class Node:
    def __init__(self, D, L=None, R=None):
        self.date = D
        self.left = L
        self.right= R

'''
[ 순회 ]
각 노드에서 도착해서 하는 순에 대한 것
전위 순회 (pre): 읽기 -> 왼쪽으로 이동 -> 오른쪽으로 이동
중위 순회 (ino): 왼쪽으로 이동 -> 읽기 -> 오른쪽으로 이동
후위 순회(post): 왼쪽으로 이동 -> 오른쪽으로 이동 -> 읽기
'''

F = Node("F")
E = Node("E")
D = Node("D")
C = Node("C", F)
B = Node("B", D, E)
A = Node("A", B, C)

def preorder(root):
    if root is None:print("(None)", end=" ")
    else:
        print(root.date, end=" ")
        preorder(root.left)
        preorder(root.right)
preorder(A)
print("= [ 전위 순회 ]")

def inordor(root):
    if root is None:print("(None)", end=" ")
    else:
        inordor(root.left)
        print(root.date, end=" ")
        inordor(root.right)
inordor(A)
print("= [ 중위 순회 ]")

def postordor(root):
    if root is None:print("(None)", end=" ")
    else:
        postordor(root.left)
        postordor(root.right)
        print(root.date, end=" ")
postordor(A)
print("= [ 후위 순회 ]")

from collections import deque
def levelorder(root):
    queue = deque()
    queue.append(root)
    while queue:
        x = queue.popleft()
        if x is None:print("(None)", end=" ")
        else:
            print(x.date, end=" ")
            queue.append(x.left)
            queue.append(x.right)
levelorder(A)
print("= [ 레벨 순회 ]")