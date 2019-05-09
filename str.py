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

# print(s.index("Like"))
# print(s.rindex("Like"))
# 발견X -> exception 발생

print(s.startswith("SANTAEYA"))
print(s.startswith("i like", 2))
print(s.endswith("Also"))
print(s.endswith("Java", 0, 26))

# 편집과 치환
s = '     what the hell      '
print("---" + s.strip() + "---")
print("---" + s.rstrip() + "---")
print("---" + s.lstrip() + "---")

s = "<><abc><><defg><>"
print("---" + s.strip("<>") + "---")

s = "What the"
print(s.replace("What", "WHAT"))

# 정렬
s = "stop no no"
print(s.center(60))
print("---" + s.center(30) + "---")
print("---" + s.ljust(30) + "---")
print("---" + s.rjust(30) + "---")

# 분리
s = "one,two,three,four,five,six,seven"
# r = s.split(",")
r = s.split(",", 2)
print(r)

s = ",".join(r)
print(s)

lines = """first line
2nd line
3rd line
4th line
"""
# print("---" + lines + "---")

# r = lines.split("\n")
# print(r)

r = lines.splitlines()
print(r)

# 판별
print("1234".isalpha())
print("abcd".isalpha())

print("1234".isdigit())
print("abcd".isdigit())

print("abcdef".islower())
print("ABCDEF".isupper())

print("".isspace())
print(" ".isspace())

# 0 채우기
print(str(1).zfill(5))

# formating ( 서식 )
# f = "name:{}, age:{}"
# s = f.format("choi", 29)
# print(s)

f = "name:{1}, age:{0}"
s = f.format(29, "choi")
print(s)

print("name:{}, age:{}".format("choi", 29))