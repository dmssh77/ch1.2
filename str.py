# 한 줄 문자열

s = ""
str1 = "hello"
str2 = "HELLO"
print(type(s))

# 여러줄 문자열
str3 = """ABC
DEF
가나다라마바사
아자차카타파하"""

# 여러줄 주석 -> 여러줄 문자열 사용
"""
주석1
주석2
주석3
"""

# escape
print("예히\n뭐다냐")
print("i say \"helloworld\"")
print('i say "helloworld"')
print("she\'s good")
print("둘리\t010-1234-1234") # tap

# 문자열 연산
str1 = "first"
str2 = "second"
str3 = str1 + " " + str2

print(str3)

str4 = str1 * 3
print(str4)

# 인덱싱
print(str1[0], str1[2], str1[4])

# 슬라이싱
str5 = str2[2:5]
print(str5)
print(str5[2:])

# 연결(+) 생략 가능쓰
# str3 = str1 + " " + str2
str3 = "이게" " " "뭐랴"
print(str3)

# 문자열 객체와 정수형 객체는 + 연산을 할 수 없다
name = "초이"
age = 29

print(name + str(age))

# len() 함수
print(len(str5))

# in / not in 연산자
print("s" in str2)
print("s" not in str1)

# 문자열 객체는 변경할 수 없다
# str1[0] = "f"
# print(str1)

# formating ( 서식 ) - tuple
f = "name:%s, age:%d"
print(f)
print(f % ('초이', 29))

# formating ( 서식 ) - format() 함수
name = "초이"
age = 29
print("name -> " + name + ", age -> " + str(age))
print("name -> " + format(name, "s") + ", age -> " + format(age, "d"))

# 객체함수 ( 대소문자 )
s = "i like SANGTAEYA"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 객체함수 ( 검색 )
s = "i like SANGTAEYA. SANGTAEYA~~"
print(s.count("SANGTAEYA"))
print(s.find("SANGTAEYA"))
print(s.find("SANGTAEYA", 10))
print(s.rfind("SANGTAEYA"))
