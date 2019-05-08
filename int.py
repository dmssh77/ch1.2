# int 정수형

a = 7
print(a, type(a))
#print(isinstance(a, int))
print(isinstance(a, bool))

# 2진수
b = 0b1101
c = 0o23
d = 0x23

print(b, c, d)

# 3.x 에서는 long 합쳐짐. 표현범위 무한대
e = 2 ** 1024
print(e, type(e))
print(e.bit_length())

# 변환함수
print(oct(38))