# 식비 절약!! 자취생들위한 음식 레시피 검색 서비스

## 🍳 식비절약! 자취생들을 위한 레시피 검색 서비스 🔍 

<br/>

###  ✔ 시작가이드
#### 🍴 For building and running the application you need :
- Node.js 18.16.0
- npm 9.5.1
- Python 3.10.12
- javac 1.8.0_202
- mongodb 4.4.24


#### 🍴 Installation
```
# git clone https://github.com/westmini427/Provide-recipe-project.git
# cd type_01
```
#### 🍴 Server
```
# cd server
# pip install --upgrade pip
# pip install pandas pymongo requests konlpy bs4
# uvicorn main:app --host 0.0.0.0 --port 3000 --reload
# json-server --watch ./bin_FoodData.json --host 0.0.0.0 --port 5000
# json-server --watch ./Trash.json --host 0.0.0.0 --port 5001
```

#### 🍴 Client
```
# cd client
# npm install express morgan path body-parser cookie-parser dotenv axios
# nodemon app.js
```
<br/>

### ✔ 기술스택

|Category|Language|
|:--:|:--|
|Server|![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)|
|Frontend|![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) |
|Backend|![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) |
|Database|![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)|

<br/>

### ✔ 프로젝트 개요

- 팀명 : 이세계식당
- 인원 : 3인 [ 서민희, 이명덕, 한민지 ]
- 기간 : 10일 [ 2023.05.22.(월) ~ 2023.06.01.(목) ]
- 문서 : Wireframe, API Sequence, API report, Architecture

<br/>

### ✔ 프로젝트 목적

- 공공데이터 API를 활용한 웹서비스 시스템 구축

<br/>

### ✔ 활용한 DATA API

- [ 식품의약품안전처 ] 식품영양성분 DB
- [ 식품의약품안전처 ] 조리식품의 레시피 DB

<br/>

### ✔ 프로젝트의 필요성

> 현재 인플레이션으로 인한 물가 상승률이 상당히 높아진 상황에서<br/>  대학생 및 사회 초년생 중 자취생들은 여러 가지 경제적 어려움에 직면하고 있습니다.<br/> 이 중에서도 가장 큰 어려움은 식비로, 이를 해결하는 것이 매우 어렵습니다. <br/> 따라서 우리는 자취생들이 이러한 부담을 덜게 하고, <br/>요리의 방향을 잡는 데 도움을 주기 위한 도구를 개발하고자 합니다.

<br/>


### ✔ 기획 의도와 방향성

![KakaoTalk_Photo_2023-09-30-19-46-32](https://github.com/LeeMyungdeok/Recipe-provided-project/assets/115915362/91408678-2d33-4135-9963-88693afb5807)

- 집에서 요리하기 위한 자취생들의 냉장고를 부탁해!
- 사용하면 할수록 데이터가 쌓이는 성장형 시스템 구축

<br/>

###  ✔ 개발 과정

> 기획의도에 맞게 시스템이 동작하려면 사용자의 입력값에 대한 <br/> 일련의 정보를 처리하고 가공하는 과정이 정리가 되어야 했습니다. <br/> 저희는 우선 영양정보 API를 가공하여 mongodb에 저장 했고, <br/> 이를 기반으로 db와 매칭을 통해 식재료를 판별하는 과정을 거쳤습니다.

![KakaoTalk_Photo_2023-09-30-19-46-53](https://github.com/LeeMyungdeok/Recipe-provided-project/assets/115915362/c04ee5a3-325e-4a53-8081-da1e575b74d8)


> 위의 화면은 [Show list]를 하기까지의 과정을 보여줍니다. <br/> [Show list]는 사용자가 음식을 검색하면 그에 대한 레시피와 식재료에 대한 정보를 제공하는 부분입니다. 

![Alt text](image-1.png)

> 필요한 데이터만을 추출하기 위한 가공이 완벽하지 않아,<br/> 식재료가 아닌 값이 화면에 나오는 경우가 있습니다. <br/> 이러한 데이터의 경우 사용자가 '신고'를 눌러줌으로써 필터에 들어가고, <br/> 그 후 다시 그 음식에 대한 레시피를 조회하면 필터링이 될 수 있도록 설계했습니다.<br/> 사용자들이 시스템을 사용하고 '신고'를 눌러 데이터가 쌓임으로써<br/>  더욱 정교한 프로세스가 될 수 있는 성장형 시스템을 구축하고자 했습니다.

<br/>

###  ✔ 실행 화면
![결과물](___%EC%9D%B4%EC%84%B8%EA%B3%84%EC%8B%9D%EB%8B%B9___-Chrome-2023-09-30-14-17-36.gif)

<br/>

###  ✔ 개선 방향
- AWS 환경에서 dynamodb 등을 활용해 시스템을 재구축할 예정입니다.
- docker를 활용하여 개발환경을 배포할 예정입니다.

## 담당 업무

- backend
  - 공공 데이터 포털에서 요리 재료에 대한 데이터를 가공했습니다.
    - 재료에 대한 전처리는 주로 코넬파이를 이용하여 형태소 분리 또는 정규 표현식을 사용하여 작업을 진행했습니다. 
  - 요리 레시피에 대한 데이터 및 재료 데이터를 가지고 Fast api를 사용하여 Rest full 방식으로 프로세스를 구축했습니다.
    - json 파일을 임의의 server로 사용하여 전처리를 잘못된부분을 필터링을 걸치도록 하기위해 구축했습니다.
    - 검색, 연관검색, 신고, 레시피 조회 등 전반적인 api 설계 부터 구현까지 위주로 담당업무를 진행했습니다. 
- frontend
  - xhr를 사용하여 client와 server을 연결했습니다.
    - 기존에 axios를 사용했지만 xhr을 알게 되어 어떤 흐름으로 가는지 경험했습니다. 
 
## 보완점

* 데이터 전처리에 대한 경우 완벽하지 못하여 재료가 아닌 값이 나오는 경우가 있습니다. 그것을 사용자가 신고를 해줌으로써 필터안에 들어가게 되고 그 후 다시 그 음식에 대한 레시피를 조회하면 필터링이 될 수 있도록 설계를 했습니다. 비롯 초반에는 애러가 종종 발생하지만 사용자들이 사용하고 신고를 눌러 줌으로써 데이터가 쌓여 더욱 정교한 프로세스서가 될수 있는 성장형 프로그램을 만들었습니다.
* 현재 AWS에서 다시 Develop 예정입니다.
