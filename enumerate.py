# enumerate() 함수 사용

i = 0
for color in ["red", "yellow", "pink"]:
    print(i, color)
    i += 1;


for color in enumerate(["red", "yellow", "pink"]):
    print(color)