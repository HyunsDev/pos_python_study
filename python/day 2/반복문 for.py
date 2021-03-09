# 반복문 for 기본
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print(f"{number}학생은 합격입니다.")
    else: 
        print(f"{number}학생은 불합격입니다.")
