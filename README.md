# Music of Today
![status](https://img.shields.io/badge/Status-On%20Development-yellowgreen.svg)
![platform](https://img.shields.io/badge/Platform-AWS-orange.svg)
![version](https://img.shields.io/badge/Project%20Start%20Date-2019--07--24-informational.svg)
> Community web site to recommend Music of Today.

## 📖 Introduction
 그날 그날 상황과 분위기에 따라 음악을 추천하고 공유하는 사이트입니다.
 
 음악 추천을 위한 게시판 기능을 주로 하여 태그, 날짜, 날씨등을 기반으로 음악을 추천을 할 수 있도록 할 예정이며, 메인 페이지에는 오늘 날씨와 시간에 따라 자동으로 작성된 플레이 리스트를 제공할 예정입니다.
 
 또한, 음악 등록 시, 제목과 아티스트를 입력하면 자동으로 유튜브, 지니, 멜론에서 링크를 찾아서 사용자가 이용하는 플렛폼에서 재생할 수 있는 기능도 구현 예정입니다.
 
## 👩‍💻 ㅁSystem requirements
 기본적으로 개발 완료 후, AWS에 배포까지 해볼 계획이나, 로컬에서 실행해 보고자 하시면 Django를 활용한 빌드 후 실행하면 됩니다.
 다만, settings.py 파일은 .gitignore에 포함해 놨기 때문에 직접 작성 후 사용하셔야 합니다.
 
### 👩‍💻 Dependency Build Instructions
 > 자세한 사용법은 개발 완료 후 작성할 예정입니다.
 ```
 pip install django==2.1.1
 pip install Pillow
```

## 📝 Todo list 
- [X] 💻 아마존 웹 서비스 배포용 환경 설정
- [ ] 🔨 UI 디자인
- [ ] 🔨 회원가입
- [ ] 🔨 게시판
- [ ] 🔒 태그 기능
- [ ] 🔒 Youtube 검색, 크롤러 구현
- [ ] 🔒 Genie 검색, 크롤러 구현
- [ ] 🔒 Melon 검색, 크롤러 구현
- [ ] 🔒 메인 페이지 음악 추천

## Contact
```
email : giopaik@naver.com
```