# 식비 절약!! 자취생들위한 음식 레시피 검색 서비스

<br>

<p align="center">
<img width="400px" src="https://smashinglogo.com/v3/envision/image.jpg?id=91fc3d13-3b21-4163-842f-ec930369348b&format=desktop">
<br><br>
<img src= "https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white" />
<img src= "https://img.shields.io/badge/nodedotjs-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
<img src= "https://img.shields.io/badge/mysql-4479A1?style=flat-square&logo=mysql&logoColor=white" />
<img src= "https://img.shields.io/badge/mongodb-47A248?style=flat-square&logo=mongodb&logoColor=white" />
<img src= "https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white" />
<img src= "https://img.shields.io/badge/inux-FCC624?style=flat-square&logo=linux&logoColor=white" />

<br>
</p>

## 주제 선정 이유

서울의 공공 자전거 서비스인 '따릉이'의 이용률이 최근 증가하고 감소함에 따라 사람들의 건강에 대한 관심이 높아지고 있습니다. 이에 우리 팀은 이러한 요즘 핫한 주제인 건강에 관한 프로젝트를 진행하고자 합니다. 이 프로젝트의 목표는 '따릉이' 서비스를 대상으로 한 자전거 대여 서비스를 제공하는 것입니다.

### Installing

#### npm 모듈 설치 

```
apt install -y npm
```
```
npm install -g nodemon
```
```
npm init -y
```
```
npm install express morgan path body-parser cookie-parser mongoose
```
#### mongodb 설치

```
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
```
```
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
```
```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
```
```
dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb
```
```
rm -rf libssl1.1_1.1.1f-1ubuntu2_amd64.deb
```
```
apt -y update; apt -y upgrade
```
```
apt -y install mongodb-org
```
```
systemctl start mongod
```
```
systemctl status mongod
```
```
mongod --version
```
```
mongo
```
#### nodejs install

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
```
```
cat ~/.bashrc
```
```
source ~/.bashrc
```
```
nvm --version
```
```
nvm ls-remote
```
```
nvm install v18.15
```
```
nvm install v16.20
```
```
npm install sync-mysql dotevv async axios
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
