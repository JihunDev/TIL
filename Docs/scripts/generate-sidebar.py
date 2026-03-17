#!/usr/bin/env python3
"""
generate-sidebar.py

Docs/ 디렉토리를 스캔하여 두 파일을 자동 생성합니다:
  - Docs/_sidebar.md  → Docsify (GitHub Pages)
  - Docs/SUMMARY.md   → GitBook

사용법:
  python3 Docs/scripts/generate-sidebar.py
"""

import os
import re
from pathlib import Path

# ── 경로 설정 ────────────────────────────────────────────────
SCRIPT_DIR  = Path(__file__).parent
DOCS_DIR    = SCRIPT_DIR.parent
SIDEBAR_OUT = DOCS_DIR / "_sidebar.md"
SUMMARY_OUT = DOCS_DIR / "SUMMARY.md"

# ── 제외 목록 ────────────────────────────────────────────────
EXCLUDED_DIRS  = {"scripts", "31-Templates", ".git"}
EXCLUDED_FILES = {"README.md", "_sidebar.md", "SUMMARY.md"}

# ── 디렉토리 표시 레이블 (이모지 포함) ───────────────────────
DIR_LABELS: dict[str, str] = {
    "1-Projects":             "🚀 1-Projects",
    "11-FODRo":               "📁 11 · FODRo",
    "12-LKAS":                "📁 12 · LKAS",
    "2-Areas":                "🗂️ 2-Areas",
    "21-Embedded":            "📂 21 · Embedded",
    "22-ROS2":                "📂 22 · ROS2",
    "23-DevOps":              "📂 23 · DevOps",
    "24-Network":             "📂 24 · Network",
    "25-Vision":              "📂 25 · Vision",
    "26-SignalProcessing":    "📂 26 · Signal Processing",
    "27-SoftwareEngineering": "📂 27 · Software Engineering",
    "3-Resources":            "📚 3-Resources",
    "4-Archives":             "🗃️ 4-Archives",
}

# ── 헬퍼 함수 ────────────────────────────────────────────────

def _sort_key(path: Path) -> tuple:
    """파일/디렉토리를 숫자 prefix 기준으로 정렬."""
    m = re.match(r"(\d+)(?:\.(\d+))?", path.name)
    if m:
        return (int(m.group(1)), int(m.group(2) or 0))
    return (999, 999)


def get_title(filepath: Path) -> str:
    """
    문서 제목 추출 우선순위:
      1. YAML frontmatter title 필드
      2. 첫 번째 H1 헤딩
      3. 파일명 (숫자 prefix·특수문자 제거)
    """
    try:
        content = filepath.read_text(encoding="utf-8")
        # 1) frontmatter
        m = re.search(
            r'^---\s*\ntitle:\s*["\']?(.+?)["\']?\s*\n',
            content,
            re.MULTILINE,
        )
        if m and m.group(1).strip():
            return m.group(1).strip()
        # 2) H1
        m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if m:
            return m.group(1).strip()
    except Exception:
        pass
    # 3) 파일명 fallback: "21.03-HW-DCDC_Converter" → "HW DCDC Converter"
    stem = re.sub(r"^\d+\.\d+-(?:Bug-|Exp-)?", "", filepath.stem)
    return stem.replace("_", " ").replace("-", " ")


def collect_md_files(directory: Path) -> list[Path]:
    """디렉토리 내 .md 파일 목록을 숫자 prefix 기준으로 정렬하여 반환."""
    files = [
        f for f in directory.iterdir()
        if f.is_file() and f.suffix == ".md" and f.name not in EXCLUDED_FILES
    ]
    return sorted(files, key=_sort_key)


def scan_docs(base: Path) -> dict:
    """
    Docs/ 트리를 스캔하여 중첩 딕셔너리 반환:

    {
      "2-Areas": {
        "21-Embedded": [Path, ...],
        "23-DevOps":   [Path, ...],
      },
      "1-Projects": {
        "_root": [Path, ...]   # 서브디렉토리 없이 바로 .md 파일이 있는 경우
      },
      ...
    }
    """
    structure: dict = {}
    top_dirs = sorted(
        [d for d in base.iterdir()
         if d.is_dir() and d.name not in EXCLUDED_DIRS and not d.name.startswith(".")],
        key=_sort_key,
    )

    for top in top_dirs:
        sub_dirs = sorted(
            [d for d in top.iterdir()
             if d.is_dir() and d.name not in EXCLUDED_DIRS],
            key=_sort_key,
        )
        structure[top.name] = {}

        if sub_dirs:
            for sub in sub_dirs:
                files = collect_md_files(sub)
                if files:  # 빈 폴더는 생략
                    structure[top.name][sub.name] = files
        else:
            # 서브디렉토리 없이 바로 .md 파일이 있는 최상위 폴더
            files = collect_md_files(top)
            if files:
                structure[top.name]["_root"] = files

    # 완전히 비어있는 최상위 폴더 제거
    structure = {k: v for k, v in structure.items() if v}
    return structure


# ── 생성기 ───────────────────────────────────────────────────

def build_sidebar(structure: dict) -> str:
    """Docsify _sidebar.md 내용 생성."""
    lines = [
        "<!-- _sidebar.md -->",
        "<!-- ⚠️  자동 생성 파일입니다. 직접 수정하지 마세요.    -->",
        "<!-- ⚠️  generate-sidebar.py 를 실행하면 덮어씌워집니다. -->",
        "",
        "- 🏠 [**Home**](/)",
        "",
        "---",
        "",
    ]

    for top_name, sub_structure in structure.items():
        top_label = DIR_LABELS.get(top_name, f"📁 {top_name}")
        lines.append(f"- **{top_label}**")
        lines.append("")

        for sub_name, files in sub_structure.items():
            if sub_name == "_root":
                for f in files:
                    rel = "/" + f.relative_to(DOCS_DIR).as_posix()
                    lines.append(f"  - [{get_title(f)}]({rel})")
            else:
                sub_label = DIR_LABELS.get(sub_name, f"📂 {sub_name}")
                lines.append(f"  - **{sub_label}**")
                for f in files:
                    rel = "/" + f.relative_to(DOCS_DIR).as_posix()
                    lines.append(f"    - [{get_title(f)}]({rel})")
                lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def build_summary(structure: dict) -> str:
    """GitBook SUMMARY.md 내용 생성."""
    lines = [
        "# Summary",
        "",
        "<!-- ⚠️  자동 생성 파일입니다. generate-sidebar.py 를 실행하면 덮어씌워집니다. -->",
        "",
        "* [Home](README.md)",
        "",
    ]

    for top_name, sub_structure in structure.items():
        top_label = DIR_LABELS.get(top_name, top_name)
        # GitBook 섹션 헤더 (## 사용 시 좌측 네비게이션 그룹화)
        lines.append(f"## {top_label}")
        lines.append("")

        for sub_name, files in sub_structure.items():
            if sub_name == "_root":
                for f in files:
                    rel = f.relative_to(DOCS_DIR).as_posix()
                    lines.append(f"* [{get_title(f)}]({rel})")
            else:
                sub_label = DIR_LABELS.get(sub_name, sub_name)
                # GitBook 그룹 항목 (링크 없는 그룹)
                lines.append(f"* **{sub_label}**")
                for f in files:
                    rel = f.relative_to(DOCS_DIR).as_posix()
                    lines.append(f"  * [{get_title(f)}]({rel})")
            lines.append("")

        lines.append("")

    return "\n".join(lines)


# ── 진입점 ───────────────────────────────────────────────────

def main() -> None:
    print(f"🔍  Docs 디렉토리 스캔: {DOCS_DIR}")
    structure = scan_docs(DOCS_DIR)

    total_files = sum(
        len(files)
        for subs in structure.values()
        for files in subs.values()
    )
    print(f"    발견된 문서: {total_files}개")

    print("📝  _sidebar.md 생성 중 (Docsify / GitHub Pages)…")
    SIDEBAR_OUT.write_text(build_sidebar(structure), encoding="utf-8")
    print(f"    ✅  {SIDEBAR_OUT.relative_to(DOCS_DIR.parent)}")

    print("📖  SUMMARY.md 생성 중 (GitBook)…")
    SUMMARY_OUT.write_text(build_summary(structure), encoding="utf-8")
    print(f"    ✅  {SUMMARY_OUT.relative_to(DOCS_DIR.parent)}")

    print("🎉  완료!")


if __name__ == "__main__":
    main()
