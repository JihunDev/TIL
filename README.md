# Today I Learned

[![Netlify Status](https://api.netlify.com/api/v1/badges/fe943f01-7efe-49b0-bd02-614dbc32ba67/deploy-status)](https://app.netlify.com/sites/brave-einstein-d2f693/deploys)

> 하루하루 학습한 내용을 기록하는 개인 지식 베이스입니다.
> **"나를 위한 구글"** — 검색 가능한 기술 노트 아카이브

## 목적

- **지식 축적**: 학습한 내용을 체계적으로 기록
- **실무 연계**: 프로젝트에서 재사용 가능한 지식 관리
- **블로그 소스**: 월 1회 TIL을 통합하여 [기술 블로그](https://jihundev.github.io) 포스트 발행

## 폴더 구조 (PARA + Johnny Decimal)

```
Docs/
├── 1-Projects/          # 진행 중인 프로젝트 관련 학습
├── 2-Areas/             # 지속 관리 영역
│   ├── 21-Embedded/     # C, 하드웨어, 임베디드
│   ├── 22-ROS2/         # ROS2, Nav2
│   ├── 23-DevOps/       # Git, Linux, CI/CD
│   ├── 24-Network/      # 네트워크
│   ├── 25-Vision/       # 이미지 처리, 컴퓨터 비전
│   ├── 26-SignalProcessing/  # 신호 처리
│   └── 27-SoftwareEngineering/  # 소프트웨어 공학
├── 3-Resources/         # 참조 자료
│   └── 31-Cheatsheets/  # 명령어 / 도구 레퍼런스
├── 4-Archives/          # 완료 / 보관
└── scripts/
    └── create-til.sh    # TIL 자동 생성 스크립트
```

## 파일명 규칙

```
[카테고리].[순번]-[주제].md
[카테고리].[순번]-Bug-[주제].md     ← 트러블슈팅
[카테고리].[순번]-Exp-[주제].md     ← 실험/벤치마크
```

**예시**

```
12.15-MPC_Cost_Function_Tuning.md
23.04-Linux-sudo_Option.md
21.02-Bug-CAN_Timeout_Error.md
```

## 템플릿 사용법

`Docs/3-Resources/31-Templates/` 에 8종 템플릿 제공:

| 템플릿 | 용도 | 예상 소요 시간 |
|--------|------|----------------|
| `template-quick-note.md` | 일상적인 메모 (80% 상황) | 5~10분 |
| `template-technical-analysis.md` | 기술/알고리즘 분석 | 30~60분 |
| `template-troubleshooting.md` | 버그 해결 기록 | 20~40분 |
| `template-cheatsheet.md` | 명령어/도구 레퍼런스 | 15~30분 |
| `template-code-analysis.md` | 코드베이스 분석 | 60분+ |
| `template-experiment.md` | 성능 실험/벤치마크 | 30~60분 |

### 자동화 스크립트

```bash
# 설치 (최초 1회)
chmod +x Docs/scripts/create-til.sh
echo 'alias til="/path/to/TIL/Docs/scripts/create-til.sh"' >> ~/.bashrc

# 사용법
til quick "ROS2 파라미터 오버라이드"   # 빠른 메모
til tech  "Nav2 DWB 컨트롤러 분석"    # 기술 분석
til bug   "CAN 통신 타임아웃"          # 버그 기록
```

## 작성 원칙

1. **완벽주의 배제** — 불완전하게라도 작성하는 것이 안 하는 것보다 낫다
2. **실무 연계** — "오늘 배운 것이 FODRo/LKAS에 어떻게 쓰일까?" 를 항상 고민
3. **검색성 최우선** — 3개월 후 내가 빠르게 찾아볼 수 있는 형태로

## 운영 사이클

```
매일 오후      → TIL 작성 (10~15분)
매주 금요일    → 주간 회고 (20분)
매월 마지막 주 → TIL 통합하여 블로그 포스트 1편 작성
```

## TIL vs 기술 블로그

| | TIL (jihun2til.netlify.app) | 블로그 (jihundev.github.io) |
|---|---|---|
| 목적 | 개인 지식 베이스 | 대외 기술 브랜딩 |
| 독자 | 미래의 나 | 동료 개발자, 채용 담당자 |
| 완성도 | 60~70% (초안 수준) | 90%+ (편집 완료) |
| 작성 주기 | 매일 | 월 1~2회 |

> TIL은 **재료**, 블로그는 **요리** — 같은 재료로 더 좋은 요리를 만든다.

## Using Tool

- [Docsify](https://docsify.js.org/)
- [Netlify](https://www.netlify.com/)

## Docsify

```bash
npm i docsify-cli -g
docsify serve ./Docs
```

## Netlify 설정 방법

> 📄 [NETLIFY_SETUP.md](./NETLIFY_SETUP.md) 참고
