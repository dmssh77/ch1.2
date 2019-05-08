# 사칙연산
print(2 * 3)
print(2 + 3)
print(2 - 3)
print(2 / 3)

# // 몫 연산
# ** 지수승
# % 나머지연산

print(2 ** 3)
print(2 // 3)
print(2 % 3)

# divmod 함수 ( tuple 로 출력 )
print(divmod(2, 3)) # -> 0, 2 출력

t = divmod(50, 100)
print(t, type(t))

# 연산자 우선순위
print(2 + 3 * 4)
print(-2 + 3 * 4)
print(-(2 + 3) * 4)

# 결합순서
print(2 ** 3 ** 4)
print((2 ** 3) ** 4)
print(2 ** (3 ** 4))