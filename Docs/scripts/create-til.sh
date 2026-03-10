#!/bin/bash
# create-til.sh - TIL 파일 자동 생성 스크립트
# Usage: ./create-til.sh <type> [title]
# Types: quick | tech | bug | cheatsheet | code | exp | meeting | review

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE_DIR="$DOCS_DIR/3-Resources/31-Templates"
TODAY=$(date +%Y-%m-%d)

# ── 카테고리 매핑 ──────────────────────────────────────────
declare -A CATEGORY_NAMES=(
  ["11"]="1-Projects/11-FODRo"
  ["12"]="1-Projects/12-LKAS"
  ["21"]="2-Areas/21-Embedded"
  ["22"]="2-Areas/22-ROS2"
  ["23"]="2-Areas/23-DevOps"
  ["24"]="2-Areas/24-Network"
  ["25"]="2-Areas/25-Vision"
  ["26"]="2-Areas/26-SignalProcessing"
  ["27"]="2-Areas/27-SoftwareEngineering"
)

# 다음 순번 계산
next_number() {
  local prefix=$1
  local dir="$DOCS_DIR/${CATEGORY_NAMES[$prefix]}"
  local max=0
  if ls "$dir"/*.md 2>/dev/null | grep -q .; then
    max=$(ls "$dir"/*.md 2>/dev/null | grep -oE "${prefix}\.[0-9]+" | grep -oE "[0-9]+$" | sort -n | tail -1)
    max=${max:-0}
  fi
  printf "%02d" $((10#$max + 1))
}

# 프로젝트 선택
select_project() {
  echo "📁 카테고리 선택:"
  echo "  1) 11 - FODRo"
  echo "  2) 12 - LKAS"
  echo "  3) 21 - Embedded"
  echo "  4) 22 - ROS2"
  echo "  5) 23 - DevOps"
  echo "  6) 24 - Network"
  echo "  7) 25 - Vision"
  echo "  8) 26 - SignalProcessing"
  echo "  9) 27 - SoftwareEngineering"
  read -p "선택 (1-9): " choice
  case $choice in
    1) echo "11" ;;
    2) echo "12" ;;
    3) echo "21" ;;
    4) echo "22" ;;
    5) echo "23" ;;
    6) echo "24" ;;
    7) echo "25" ;;
    8) echo "26" ;;
    9) echo "27" ;;
    *) echo "23" ;;  # 기본값: DevOps
  esac
}

# 파일명 슬러그 변환 (공백 → _, 특수문자 제거)
slugify() {
  echo "$1" | tr ' ' '_' | sed 's/[^A-Za-z0-9_\-]//g'
}

# ── 메인 로직 ──────────────────────────────────────────────
TYPE=${1:-quick}
TITLE=${2:-""}

# 주간 리뷰는 별도 처리
if [ "$TYPE" = "review" ]; then
  WEEK=$(date +%Y-W%V)
  FILENAME="$DOCS_DIR/2-Areas/$WEEK-Weekly_Review.md"
  TEMPLATE="$TEMPLATE_DIR/template-weekly-review.md"
  sed "s/YYYY-WXX/$WEEK/g; s/YYYY-MM-DD/$TODAY/g" "$TEMPLATE" > "$FILENAME"
  echo "✅ 주간 리뷰 생성: $FILENAME"
  ${EDITOR:-vi} "$FILENAME"
  exit 0
fi

# 제목 입력
if [ -z "$TITLE" ]; then
  read -p "📝 주제 입력: " TITLE
fi

# 카테고리 선택
PREFIX=$(select_project)
DIR="$DOCS_DIR/${CATEGORY_NAMES[$PREFIX]}"
NUM=$(next_number "$PREFIX")
SLUG=$(slugify "$TITLE")

# 타입별 파일명 접두사
case $TYPE in
  bug|troubleshooting) PREFIX_TAG="Bug-" ;;
  exp|experiment)      PREFIX_TAG="Exp-" ;;
  *)                   PREFIX_TAG="" ;;
esac

# 타입별 템플릿 매핑
case $TYPE in
  quick)                TEMPLATE="$TEMPLATE_DIR/template-quick-note.md" ;;
  tech|technical)       TEMPLATE="$TEMPLATE_DIR/template-technical-analysis.md" ;;
  bug|troubleshooting)  TEMPLATE="$TEMPLATE_DIR/template-troubleshooting.md" ;;
  cheatsheet)           TEMPLATE="$TEMPLATE_DIR/template-cheatsheet.md" ;;
  code)                 TEMPLATE="$TEMPLATE_DIR/template-code-analysis.md" ;;
  exp|experiment)       TEMPLATE="$TEMPLATE_DIR/template-experiment.md" ;;
  meeting)              TEMPLATE="$TEMPLATE_DIR/template-meeting-notes.md" ;;
  *)                    TEMPLATE="$TEMPLATE_DIR/template-quick-note.md" ;;
esac

FILENAME="$DIR/${PREFIX}.${NUM}-${PREFIX_TAG}${SLUG}.md"

# 날짜 치환하여 파일 생성
sed "s/YYYY-MM-DD/$TODAY/g" "$TEMPLATE" > "$FILENAME"

echo "✅ TIL 생성: $(basename $FILENAME)"
echo "   경로: $FILENAME"

# 에디터 열기 (EDITOR 환경변수 우선, 없으면 vi)
${EDITOR:-vi} "$FILENAME"
