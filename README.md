# Today I Learned 

[![Netlify Status](https://api.netlify.com/api/v1/badges/fe943f01-7efe-49b0-bd02-614dbc32ba67/deploy-status)](https://app.netlify.com/sites/brave-einstein-d2f693/deploys)

> Jihun이 오늘 새로 배운 것을 다음의 규칙으로 commit 합니다.

## 작성 규칙
- 문서 생성은 [GFM (Github Flavored Markdown)](https://help.github.com/articles/github-flavored-markdown/) 을 사용한다.
- 언어나 기술명으로 폴더를 만든다. 
- root에 문서를 만들지 않는다.
- 파일명은 영어로 만든다.
- 파일명은 아래의 규칙으로 작성한다.
    - 파일명-파일_제목.md
    - 파일명 규칙표
        | 파일명 | 설명 |
        | ---- | ---- |
        | Reference | 설명 |
        | Difference | 차이점 분석 |
        | Command | 커맨드 설명 |
        | Error | 에러 해결 |
        | Setting | 설정법 |

## Using Tool
- [Docsify](https://docsify.js.org/)
- [Netlify](https://www.netlify.com/)

## Docsify
### Install
```shell
$ npm i docsify-cli -g
```
### 초기 설정
```shell
$ docsify init ./docs
```
### 실행 방법
```shell
$ docsify serve ./docs
```

## Netlify 설정 방법

![NetlifySetting1](https://imgur.com/9pUgVnc.png)
- 로그인

![NetlifySetting2](https://imgur.com/XoC3lOb.png)
- New site from Git을 눌러 진행

![NetlifySetting3](https://imgur.com/cVVQbxb.png)
- Github, Gitlab, Bitbucket중 Docsify을 만든 곳을 선택

![NetlifySetting4](https://i.imgur.com/1cMbV7n.png)
- Only Select Repositories에서 선택

![NetlifySetting5](https://imgur.com/5jFb0Vo.png)
- Deploy Site 버튼 클릭

![NetlifySetting6](https://imgur.com/zPQCEkP.png)
- Publish Directory에 docs/ 추가