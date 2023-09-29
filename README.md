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

## Recipe-provided-project
```
json-server --watch ./bin_FoodData.json --host 0.0.0.0 --port 5000
```
```
json-serve
```
```
r --watch ./Trash.json --host 0.0.0.0 --port 5001
```

## server
```
uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

## client
```
nodemon app.js
```




## back-end 아키텍쳐 설계

<img width="592" alt="스크린샷 2023-09-22 오후 9 31 23" src="https://github.com/LeeMyungdeok/bike-rental-project/assets/115915362/4ac3590d-024c-4318-8427-0a00966efda1">

### 테스트는 이런 식으로 동작합니다
|                sign in              |                sign up               |
| :----------------------------------: | :----------------------------------: | 
| <img src='https://github.com/LeeMyungdeok/bike-rental-project/assets/115915362/d9b8fd6f-920d-4086-81b4-28481e60e383' width='400px' height='200px'>                                | <img src='https://github.com/LeeMyungdeok/bike-rental-project/assets/115915362/6f8f1f67-5432-4956-a45a-778daa9e633c' width='400px'  height='200px'>                                 |

|                return              |                rental               |
| :----------------------------------: | :----------------------------------: |
| <img src='https://github.com/LeeMyungdeok/bike-rental-project/assets/115915362/ffe5dd42-a87b-46f1-98b3-d673b25a15a4' width='400px' height='300px'>                                 | <img src='https://github.com/LeeMyungdeok/bike-rental-project/assets/115915362/d191e793-e651-4951-bdf1-7bbe480dac17' width='400px' height='400px'>                                 |







## 배포

예정 입니다.

## 팀명: 이세계식당

* [팀원](링크) - 이명덕, 서민희

## 담당 업무

- backend
  - 
- frontend
  - 로그인 페이지, main 페이지를 구축했습니다.
 
## 보완점

* 해당 프로젝트는 node.js, html, css, javascript의 내용을 배워 첫 프로젝트이기에 부족한 점이 많습니다. 조금 씩 업그레이드를 할 예정입니다.
