# 식비 절약!! 자취생들위한 음식 레시피 검색 서비스

<br>
<p align="center">
<img width="500px" src="https://github.com/LeeMyungdeok/Recipe-provided-project/assets/115915362/c623c6fb-4475-4ea4-b7af-431b0073c758)">
<br>
<img src= "https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white" />
<img src= "https://img.shields.io/badge/nodedotjs-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
<img src= "https://img.shields.io/badge/mysql-4479A1?style=flat-square&logo=mysql&logoColor=white" />
<img src= "https://img.shields.io/badge/mongodb-47A248?style=flat-square&logo=mongodb&logoColor=white" />
<img src= "https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white" />
<img src= "https://img.shields.io/badge/inux-FCC624?style=flat-square&logo=linux&logoColor=white" />
<img src= "https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white" />

<br>
</p>

## 주제 선정 이유
현재 인플레이션으로 인한 물가 상승률이 상당히 높아진 상황에서 대학생 및 사회 초년생 중 자취생들은 여러 가지 경제적 어려움에 직면하고 있습니다. 이 중에서도 가장 큰 어려움은 식비로, 이를 해결하는 것이 매우 어렵습니다. 따라서 우리는 자취생들이 이러한 부담을 덜게 하고, 요리의 방향을 잡는 데 도움을 주기 위한 도구를 개발하고자 합니다.

### development environment

#### Recipe-provided-project
```
json-server --watch ./bin_FoodData.json --host 0.0.0.0 --port 5000
```
```
json-serve
```
```
r --watch ./Trash.json --host 0.0.0.0 --port 5001
```

#### server
```
uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

#### client
```
nodemon app.js
```

## back-end 아키텍쳐 설계

<p align="center">
<img width="700" alt="image" src="https://github.com/LeeMyungdeok/Recipe-provided-project/assets/115915362/fa80152a-5bb5-4977-9e4f-a94d953fa51e">
</p>
### 기능 동작
|                sign in              |                sign up               |
| :----------------------------------: | :----------------------------------: | 
| <img src='https://github.com/LeeMyungdeok/Recipe-provided-project/assets/115915362/0a8dd09a-962c-4eb5-9ee7-aea4d4bcc16f' width='400px' height='300px'> | <img src='https://github.com/LeeMyungdeok/Recipe-provided-project/assets/115915362/96fccd2d-74b5-4c75-9f83-2857754edf8d' width='400px' height='300px'>                                 |

|                return              |                rental               |
| :----------------------------------: | :----------------------------------: |
| <img src='https://github.com/LeeMyungdeok/Recipe-provided-project/assets/115915362/b6b795d0-f00b-4429-8351-fe532fa74a7c' width='400px' height='300px'> | <img src='https://github.com/LeeMyungdeok/Recipe-provided-project/assets/115915362/36730ab2-37b2-4ecf-8324-3318801bfbc4' width='400px' height='300px'> |

## 배포

예정 입니다.

## 팀명: 이세계식당

* [팀원](링크) - 이명덕, 서민희

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
