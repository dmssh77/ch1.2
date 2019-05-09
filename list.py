# 생성
list1 = []
list1 = [1, True, "python"]

# indexing
print(list1[0], list1[1], list1[2])

print(list1[-3], list1[-2], list1[-1])

# slicing
print(list1[1:3:1])
print(list1[:])
print(list1[2:])
print(list1[len(list1)-1::-1])

# 반복
list2 = list1 * 2
print(list2)

# 길이
print(len(list1))

# in / not in 확인
print(5 not in list2)
print("python" in list2)

# 삭제
del list2[2]
print(list2)

# 변경가능한 객체 ( mutable )
a = ["apple", "banana", 10, 20]
a[2] = a[2] + 90
print(a[2])

# 슬라이싱을 사용한 치환
a = [1, 12, 123, 1234]
# a[0:2] = [10, 20]
a[0:2] = [10]
print(a)

a[2:3] = [300, 400]
print(a)

# 슬라이싱을 사용한 삭제
a = [1, 12, 123, 1234]
a[1:2] = []
print(a)

a[0:] = []
print(a)

# 슬라이싱을 사용한 삽입
a = [1, 12, 123, 1234]

# 중간삽입
a[1:2] = ['a']
print(a)

# 마지막 삽입
a[5:] = [4567]
print(a)

# 처음에 삽입
a[:0] = [7777]
print(a)

# 여러개 삽입
a[2:2] = [-12, -1, 0]
print(a)

# 뒤에 삽입
a.append(5)
print(a)

# 앞에 삽입
a.insert(0, 0)
print(a)

# reverse
a.reverse()
print(a)

# 제거 ( 값으로 삭제 )
# 값이 없는 경우 예외 발생
# a.remove(3)
# print(a)

# 확장
a.extend([-1, -2, -3])
print(a)
print("----------------------")
# stack 사용
s = []

s.append(10) # push
s.append(20) # push
s.append(30) # push
print(s)

print(s.pop())
print(s)

print("----------------------")

# queue 사용
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)

print(q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print(q.pop())
print(q)

# sort() 내장된 정렬 알고리즘에 따라 정렬
list1 = [1, 5, 2, 7, 4, 3]
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)
print("*************************")

list2 = [10, 2, 33, 9, 8, 33, 4, 11]
list2.sort(key=str) # [10, 11, 2, 33, 33, 4, 8, 9] -> ASCII 값 비교
print(list2)

list2.sort(key=int) # [2, 4, 8, 9, 10, 11, 33, 33]
print(list2)

# 전역함수 sorted
list1 = [27, 37, 7, 57, 17, 47]
list2 = sorted(list1)
print(list2)

list2 = sorted(list1, reverse=True)
print(list2)

list1 = [19, 35, 22, 17, 55]
def f(i):
    return i % 10

list2 = sorted(list1, reverse=True)

print(list2)