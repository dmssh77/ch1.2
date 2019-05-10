# zip 함수 example

seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}

z = zip(seq1, seq2)

print(z)
print(type(z))

# 순회
for t in z:
    print(t, type(t))

# 한번 슝 돌면 못써 다시 만들어줘야혀
z = zip(seq1, seq2)
for index, t in enumerate(z):
    print(index, t)

d1 = [("foo", "one"), ("bar", "two"), ("baz", "three")]
seq1, seq2 = zip(*d1)
print(seq1)
print(seq2)