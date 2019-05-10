# 생성

s = {1, 2, 3}
print(s, type(s))

# 기본 연산
print(len(s))
print(2 in s)
print(10 not in s)

# 없는 원소를 제거시에 discard는 오류X / remove는 오류ㅇ
s.discard(20)
print(s)

# s.remove(30)
# print(s)

s.update({2, 3, 4}) # 없는 data만 추가 -> {1, 2, 3, 4}
print(s)

# 수학의 집합과 관련된 객체 함수
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2) # 합집합
print(s3)

s4 = s1.intersection(s2) # 교집합
print(s4)

s5 = s1.difference(s2)
print(s5)

s6 = s1.symmetric_difference(s2)
print(s6)