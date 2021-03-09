# 반복문 기본
i = 0  # 반복문 조건에 사용될 변수
while i < 4: # 만약 i가 4 미만이라면 실행
    i = i + 1 # i를 1 증가
    print(f"눈치게임 {i}") # "눈치게임 i" 출력
    if i == 4: # 만약 i가 4라면
        print("탈락") # 탈락 출력

### 반복문 탈출하기 ##
i = 0  # 반복문 조건에 사용될 변수를 0으로 설정
while True: # 무한히 반복
    i = i + 1 # i를 1 증가
    print(f"눈치게임 {i}") # "눈치게임 i" 출력
    if i == 4: # 만약 i가 4라면
        print("탈락") # 탈락 출력
        break # 반복문 탈출

### 반복문 탈출하기 ##
i = 0 
while True:
    i = i + 1 
    print(f"눈치게임 {i}")
    if i == 4:
        print("탈락")
        break

# 반복문 맨 처음으로 돌아가기 (= 넘어가기)
i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)

