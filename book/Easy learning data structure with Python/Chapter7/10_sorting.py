# 정렬의 다양한 방법
array = [3, 7, 6, 2, 8, 4, 9, 1, 5]
LEN = len(array)


# 선택 정렬
l = array[:]
for idx1 in range(LEN-1):
    MIN = idx1                        # 현위치가 가장 작음
    for idx2 in range(idx1+1, LEN):
        if l[MIN]>l[idx2]:            # 가장 작은 것 찾는 중
            MIN = idx2                # 가장 작은 것 갱신
    l[idx1], l[MIN] = l[MIN], l[idx1] # 선택한 요소와 자리 교체
print("선택 정렬", l)

# 삽입 정렬
l = array[:]
for idx1 in range(1, LEN):         # 0번은 자신과 교체되어 줄 수가 없음
    elm = l.pop(idx1)              # 1번부터 자리를 교체 해줌
    idx2 = idx1-1                  # 자신의 앞자리와 위치를 맞춰주고
    while idx2>=0 and l[idx2]>elm: # 자신보다 작거나 같으면 넘어가고
        idx2 -= 1                  # 자신보다 크면 앞으로 한칸 더 간다
                                   # 결국 자신보다 작은 것을 만날떄까지 반복되다가
    l.insert(idx2+1, elm)          # 만나면 그 뒷자리에 배치된다
print("삽입 정렬", l)

# 버블 정렬
l = array[:]
for _ in range(LEN-1):
    for idx1 in range(LEN-1):
        if l[idx1]>l[idx1+1]: # 다로 다음 것과 비교해주며 교체해준다
            l[idx1], l[idx1+1] = l[idx1+1], l[idx1]
print("버블 정렬", l)


# 이 외에도 다양한 정렬법이 있는데 따로 찾아보도록 하겠다