# 해싱은 연산을 이용해서 데이터를 내가 원하는 장소에 저장하는 기술인데
# 연산을 해시 함수라고 하며 장소를 해시 테이블이라고 한다

# 해시함수
# 어떠한 데이터를 주소로 보내는데 최대한 충돌(오버플로우)을 일으키지 않고
# 분포시켜야 좋은 함수라고 할 수 있음

# 제산 함수
# 산술 %를 이용해서 만든다, h(k) = k mod N, N=소수
# N이 소수일 때, 충돌이 적다
def hMod(k):return k % 997

hashTable = [None] * 1000
data = 1234
key = hMod(data)

hashTable[key] = data
print(f"해시값 : {key}, 저장된 데이터 : {hashTable[key]}")


# 폴딩 함수
# 데이터를 같은 크기(비트)로 나누어 연산을 한다
# 더하거나 XOR연산처리 또는 곱하는 것도 있다
def hAdd(k):
    point = len(str(k))//2
    a, b = k//10**point, k%10**point
    return a+b

hashTable = [None] * 1000
data = 1234
key = hAdd(data)

hashTable[key] = data
print(f"해시값 : {key}, 저장된 데이터 : {hashTable[key]}")


# 중간 제곱 함수
# 제곱한 다음 일부 중간 숫자를 해시값으로 쓴다
def hPow(k):return int(str(k**2)[2:-2])

hashTable = [None] * 1000
data = 1234
key = hPow(data)

hashTable[key] = data
print(f"해시값 : {key}, 저장된 데이터 : {hashTable[key]}")


# 비트 추출 함수
# 위 중간 제곱 함수와 같으나 제곱이 아닌 비트로 한다는 점이 다르다
def hBit(k):return int(bin(k)[4:-2], 2)

hashTable = [None] * 1000
data = 1234
key = hBit(data)

hashTable[key] = data
print(f"해시값 : {key}, 저장된 데이터 : {hashTable[key]}")


# 숫자 분석 함수
# 특정 자리의 숫자를 이용해서 해시값으로 쓴다
def hNum(k):
    kString = str(k)
    return int(kString[0]+kString[-1])

hashTable = [None] * 1000
data = 1234
key = hNum(data)

hashTable[key] = data
print(f"해시값 : {key}, 저장된 데이터 : {hashTable[key]}")