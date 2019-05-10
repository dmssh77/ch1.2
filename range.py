# range() 함수 사용
seq = range(10)
print(seq, type(seq))
print(len(seq))

for i in seq:
    print(i + 1, end=" ")
else:
    print("")


for i in range(5, 10):
    print(i, end=" ")
else:
    print("")


for i in range(0, 10, 2):
    print(i, end=" ")
else:
    print("")

for i in range(0, 10, -1):
    print(i, end=" ")