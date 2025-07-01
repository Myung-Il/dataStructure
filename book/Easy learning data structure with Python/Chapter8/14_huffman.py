# 빈도 수에 따라 용량을 할당 해주는 방식
# 가장 적게 쓰는 방식을 합쳐서 트리형태를 만든다

'''
원본
A   B   C   D   E
8   3   5   7   1

정렬
A   D   C   B   E
8   7   5   3   1

압축 1
A   D   C   BE
8   7   5   4

압축 2
A   D   CBE
8   7   9

압축 3
AD   CBE
15   9

압축 4
ADCBE
24

가변길이코드   고정 길이 코드 
A : 00       | A : 0000
B : 1110     | B : 0001
C : 110      | C : 0010
D : 01       | D : 0011
E : 1111     | E : 0100

'''


import heapq
def huffman(seq):
    heap = []
    for n in seq:heapq.heappush(heap, n)
    for _ in range(1, len(seq)):
        e1 = heapq.heappop(heap)
        e2 = heapq.heappop(heap)
        heapq.heappush(heap, e1+e2)
        print(f"({e1}+{e2})")

label = ["A", "B", "C", "D", "E"]
freq  = [ 8,   3,   5,   7,   1 ]
huffman(freq)