# 파이썬에 존재하는 특별한 메소드에 대한 기능 정리

class Item:
    def __init__(self, N, L):
        self.name = N
        self.box = L

    def __str__(self): return "__str__를 이용"
    def __len__(self): return len(self.box)
    def __contains__(self, elm): return elm in self.box
    def __getitem__(self, idx): return self.box[idx]
    def __setitem__(self, idx, elm): self.box[idx] = elm

l = Item("리스트", [3, 4, 1, 5, 2])

print(l)
print("__len__를 이용,", len(l))
print("__contains__를 이용,", 4 in l, 0 in l)

print("__getitem__를 이용,", l[0])

l[0] = 0
print("__setitem__를 이용 후,", l[0])



# 위와 같은 것들을 제외하고도
# 비교 연산 : __eq__(==), __lt__(<), __le__(<=), __ne__(!=), __gt__(>), __ge__(>=) 
# 산술 연산 : __add__(+), __sub__(-), __mul__(*), __truediv__(/), __floordiv__(//), __mod__(%), __pow__(**)
# 복합 연산 : __iadd__(+=), __isub__(-=), __imul__(*=), __itruediv__(/=), __ifloordiv__(//=), __imod__(%=), __!pow__(**=)