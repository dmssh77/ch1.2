# 생성
d = {"mid": 3, "high": 5}

print(d, type(d))

d2 = dict()
print(d2, type(d2))

# index 대신 key 로 접근 ( 간접 접근 )
print(d["high"])

# 연결을 지원하지 않음 ( 예외 발생 )
# d2 = d + {"ele": 4}

# 반복( * ) 지원하지 않음
# d2 = d * 2

# 크기
print(len(d))

# in, not in : only key
print("uni" in d)
print("high" in d)

d3 = dict(one=1, two=2, three=3)
print(d3, type(d))

d4 = dict([("one", 1), ("two", 2), ("three", 3)])
print(d4, type(d4))

# 다양한 타입의 key 사용 가능
d = {}
print(d)

d["ten"] = 10
d[True] = "true"
print(d)

# key 는 불가능한 type을 사용해야 한다
# d[[1, 2, 3]] = 6

#
# 객체 함수
#
k = d.keys()
print(k, type(k))

for key in k:
    print(key, d[key])

print("------------------------")

items = d.items()
print(items)
for item in items:
    print(item)

print("*********************")
phones = dict(둘리="1234-1234", 도우너="2345-2345", 또치="3456-3456")
print(phones)

p = phones
print(p)

p = phones.copy()
phones["또치"] = "4567-4567"

print(phones)

# get() 을 사용하는 이유 : 없는 경우에는 None
# [] 가져오는 경우에는 없을 시 예외
print(phones.get("또치"))
print(phones.get("길동"))

# setDefault : get()과의 차이점은 실제로 저장
print(p.setdefault("길동", "4567-4567"))
print(p)

# pop() : 삭제와 동시에 값을 가져옴
phone = p.pop("둘리")
print(phone)
print(p)

t = p.popitem()
print(t)
print(p)

# 모두 삭제
p.clear()
print(p)

# 조회
d = dict(c=3, a=1, b=2)

for key in d:
    print(key, end="")
else:
    print("")

print("sleepy..-------------------------")

for key in d.keys():
    print(key, end="")
else:
    print("")

for value in d.values():
    print(value)

