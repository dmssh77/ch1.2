# packing 은 tuple 로만 가능
t = 10, 20, 30, "python"
print(t, type(t))

# unpacking
a, b, c, d = t
print(a, b, c, d)

# error : 패킹되어 있는 객체가 더 많은 경우
# a, b, c, = t

# error : 패킹되어 있는 객체가 더 적은 경우
# a, b, c, d, e = t

# unpacking 확장
t = (1, 2, 3, 4, 5)
a, *b = t
print(a, b)

*a, b = t
print(a, b)

# tuple 변경 불가
# t = ("a", "b", "c")
# t[2] = 90

# tuple 을 이용해서 여러개의 값을 대입할 수 있다
x, y, z = (10, 20, 30)

# tuple 을 이용해서 여러개의 값을 치환할 수 있다
x, y = (10, 20)
print(x, y)
x, y = y, x
print(x, y)

#
# 객체 함수 : immutable 때문에 객체 함수가 많지 않음
#

t = (20, 30, 40, 50, 20)
print(t.index(30))
print(t.count(20))

# 변환 ( tuple -> set )
s = set(t)
print(s)

# 변환 ( tuple -> list )
l = list(t)
print(l)

# 변환 ( list -> tuple )
t2 = tuple(l)
print(t2)
