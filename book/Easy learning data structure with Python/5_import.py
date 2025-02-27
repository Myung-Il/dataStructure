# 파이썬에서 모듈을 불러오고 클래스를 호출하는거 까지는 from ... import ... 로 해결할 수 있으나
# 복합적인 형태는 그만 알아보자, 얘는 이게 끝이다, 대단한 무언가는 없다
# 경로에 관한 것도 비슷하다

'''
생각해본 형태

from a.b import c
import a.b.c
    from이 있으면 from 자리에는 무조건 모듈만 올 수 있으며
    import는 함수나 클래스, 변수가 와야 한다

from a import b.c
    위와 같이 from에는 모듈만 왔지만
    import에 모듈이 섞였으므로 안된다

'''