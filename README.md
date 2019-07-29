# Music of Today
![status](https://img.shields.io/badge/Status-On%20Development-yellowgreen.svg)
![platform](https://img.shields.io/badge/Platform-AWS-orange.svg)
![project_start_date](https://img.shields.io/badge/Project%20Start%20Date-2019--07--24-informational.svg)
> Community web site to recommend Music of Today.

## 📖 Introduction
 그날 그날 상황과 분위기에 따라 음악을 추천하고 공유하는 사이트입니다.
 
 음악 추천을 위한 게시판 기능을 주로 하여 태그, 날짜, 날씨등을 기반으로 음악을 추천을 할 수 있도록 할 예정이며, 메인 페이지에는 오늘 날씨와 시간에 따라 자동으로 작성된 플레이 리스트를 제공할 예정입니다.
 
 또한, 음악 등록 시, 제목과 아티스트를 입력하면 자동으로 유튜브, 지니, 멜론에서 링크를 찾아서 사용자가 이용하는 플렛폼에서 재생할 수 있는 기능도 구현 예정입니다.
 
## 👩‍💻 System requirements
 기본적으로 개발 완료 후, AWS에 배포까지 해볼 계획이나, 로컬에서 실행해 보고자 하시면 Django를 활용한 빌드 후 실행하면 됩니다.
 다만, settings.py 파일은 .gitignore에 포함해 놨기 때문에 github 용으로 따로 업로드 해둔 settings 파일의 이름을 바꿔 사용해주시면 되겠습니다.
 
### 👩‍💻 Dependency Build Instructions
 > 자세한 사용법은 개발 완료 후 작성할 예정입니다.
 ```
 pip install django==2.1.1
 pip install Pillow
 pip install bs4
 pip install requests
```

## 📝 Todo list 
- [X] 💻 아마존 웹 서비스 배포용 환경 설정
- [X] 💻 현재 날씨 크롤러 구현
- [X] 💻 날씨, 시간 기반 가변 백그라운드 이미지 구현
- [X] 💻 UI 디자인
- [X] 💻 회원가입
- [ ] 🔨 게시판
- [ ] 🔒 태그 기능
- [ ] 🔒 Youtube 검색, 크롤러 구현
- [ ] 🔒 Genie 검색, 크롤러 구현
- [ ] 🔒 Melon 검색, 크롤러 구현
- [ ] 🔒 메인 페이지 음악 추천

## 📁 Development Plan
### Main
> 사이트의 주요 기능을 포함하는 앱
- [X] 💻 Nav, Footer 를 포함한 공통 UI
- [X] 💻 Session 기반 크롤링 횟수 최소화
- [X] 💻 날씨 정보, 시간대 정보 기반 백그라운드 이미지 선택
- [ ] 유튜브 뮤직 플레이어
- [ ] 메인페이지 음악 선택기

### Board
> 커뮤니티 게시판 기능을 포함하는 앱
- [ ] 게시판 글 CRUD
- [ ] 음악 첨부, 플레이어 연동 기능
- [ ] 글 태그 기능

### Account
>로그인, 회원가입, 로그아웃 및 계정관리 전반
- [X] 💻 로그인
- [X] 💻 회원가입

## Update Note
> 2019/07/28
> <p>날씨 크롤러를 bs로 개발하였다. 일단 서울 날씨를 기반으로 하게 하였으나 추후 현위치 기반으로 업데이트하면 좋을 듯 하다.
> <p>현재 크롤러가 매 접속 시점에 크롤링을 수행하는데, 성능 개선을 위해 이를 주기적으로 수행하도록 (periodic task) 개선할 예정이나 방법을 모르겠다..
> <p>위의 크롤러 퍼포먼스 문제로 이미지를 매번 새로 찾는 것이 아닌 스태틱 이미지 중 적절한 것을 골라서 보여주는 것으로 대채하였다. 다만 나중엔 정말로 그때그때 새 이미지를 찾도록 해보고 싶다.

> 2019/07/29
> <p>로그인 및 회원 기능 전반을 구현하였다. Django의 기본 회원 기능이 너무 좋은 것 같다. 나때는 말이야... 스프링에서 읍읍ㅂ..
> <p>크롤러를 메인 페이지 접속시에만 작동하고 이외에는 세션에 저장된 정보를 사용하도록 하였다.
## Contact
```
email : giopaik@naver.com
```