import requests

# 학교 코드
school_code = "8140089"

# 교육청 코드
office_code = "N10"

# 날짜
date = "20210305"

# 인증키
key = "개인_"

# 주소
url = "https://open.neis.go.kr/hub/mealServiceDietInfo"

# 파라미터
params = {
    "KEY" : key,
    "Type" : "json",
    "ATPT_OFCDC_SC_CODE" : office_code,
    "SD_SCHUL_CODE" : school_code,
    "MLSV_YMD" : date
}

# api 요청
res = requests.get(url, params=params)

# json 파싱
data = res.json()

# 파일을 생성하고 날짜 정보 기록
with open(date + ".txt", "w", encoding="utf-8") as f: # 해당 날짜의 이름을 가진 파일을 쓰기모드(w)로 열기 - 한글이 깨지는 것을 방지하기 위해 인코딩을 utf-8로 설정
    f.write("서령고등학교 " + date + " 급식정보\n\n") # 파일 맨 위에 제목 기록 및 줄바꿈 2번

# 내용을 분별하여 파일에 저장
for i in data["mealServiceDietInfo"][1]["row"]: # 파싱한 데이터에서 각 식시별로 아래 코드를 실행 - 반복문
    menu = i["DDISH_NM"]  # 파싱한 데이터에서 메뉴 부분 가져오기
    menu = menu.replace("<br/>", "\n") # 데이터에서 "<br/>를 줄바꿈으로 치환"
    with open(date + ".txt", "a", encoding="utf-8") as f:  # 해당 날짜의 이름을 가진 파일을 추가모드(a)로 열기 - 한글이 깨지는 것을 방지하기 위해 인코딩을 utf-8로 설정
        f.write(i['MMEAL_SC_NM'] + "\n" + menu + "\n\n") # 파일에 쓰기


    

