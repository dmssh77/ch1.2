# 생성
t = () # 공튜플
t = (1, 2, 3)

print(t, type(t))

#
# 시퀀스 연산
#

# 인덱싱
print(t[-3], t[-2], t[-1], t[0], t[1], t[2])

# 슬라이싱
print(t[1:3])
print(t[:])

# 반복
t2 = t * 2
print(t2)

# 연결
t3 = t + (4, 5, 6)
print(t3)

# in, not in
print(5 in t3)

# tuple 변경 불가 ( immutable ) sequence 형



#
# 객체 함수