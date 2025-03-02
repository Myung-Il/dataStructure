# 개방 주소법 : 오버플로우시 다른 곳에 저장
# 체이닝 : 한 곳에 여러개 저장

# 개방 주소법의 대표적인 방법이 있다
# 그것은 선형 조사법이라는 것으로 오버플로우가 발생하면
# 다음 슬롯이 비어 있으면 다음 슬롯에 저장하는 방법이다
# 단점
# 오버플로우가 계속 발생하는 구간이 만들어 질 수 있는데
# 그럴 경우에는 느려질 수 있다

# 각 기능을 만들어보자면
def hAdd(k):
    LEN = len(str(k))-1
    if LEN:return k//10**LEN+k%10
    else: return k

def probing(e):
    key = hAdd(e)
    chaining_hashTable[key].append(e)
    while openAdressing_hashTable[key]:
        key += 1
    openAdressing_hashTable[key] = e

openAdressing_hashTable = [None] * 10
chaining_hashTable = [[]for _ in range(10)]
for item in [213, 1, 6591, 174, 500, 190, 41]:
    probing(item)

print(openAdressing_hashTable)
print(chaining_hashTable)