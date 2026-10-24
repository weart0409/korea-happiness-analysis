# 🇰🇷 대한민국 행복(Happiness) 데이터 분석 프로젝트

<div align="center">

[![Live Presentation](https://img.shields.io/badge/🌐_웹_슬라이드덱-바로_실행하기-38bdf8?style=for-the-badge&logo=googlechrome&logoColor=white)](https://weart0409.github.io/korea-happiness-analysis/)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Active-34d399?style=for-the-badge&logo=github)](https://weart0409.github.io/korea-happiness-analysis/)

### 👉 **[https://weart0409.github.io/korea-happiness-analysis/](https://weart0409.github.io/korea-happiness-analysis/)**
*(별도 설치 없이 위 링크를 클릭하면 브라우저에서 7장 풀 슬라이드덱이 즉시 실행됩니다)*

</div>

---

> **프로젝트 목표**: World Happiness Report 2026(WHR 2026) 데이터 및 국내외 웰빙 지표를 기반으로, 대한민국 국민의 행복도 현황과 결정 요인, 그리고 '경제적 성취 대비 낮은 행복'이라는 역설적 현상을 실증적으로 분석하고 정책적·사회적 시사점을 도출합니다.

---

## 📁 프로젝트 폴더 구조 (Project Architecture)

효율적인 데이터 과학 워크플로우와 AI-인간 페어 프로그래밍 협업을 위해 다음과 같이 모듈화되어 있습니다.

```
dataprogect/
├── data/
│   ├── raw/                 # 원본 데이터 보관 (WHR26_Data_Figure_2.1.xlsx 등)
│   └── processed/           # 정제 및 가공 완료된 데이터셋 (CSV, Parquet)
├── references/              # 논문, 원본 보고서 PDF 및 서지 정보
│   ├── WHR26.pdf            # UN 세계 행복 보고서 2026 본문
│   ├── WHR26_Statistical_Appendix.pdf # 통계 방법론 및 회귀 모형 부록
│   └── BIBLIOGRAPHY.md      # 인용 출처, 메타데이터, 연구 레퍼런스 정리
├── notebooks/               # Jupyter Notebook 탐색적 데이터 분석(EDA)
│   └── 01_eda_korea_whr.ipynb # (예정) WHR 시계열 및 OECD 비교 분석
├── src/                     # 공통 파이썬 모듈 (데이터 로더, 시각화 유틸)
│   └── __init__.py
├── slides/                  # HTML 슬라이드덱 (발표 및 계획 공유용)
│   └── index.html           # 인터랙티브 모던 HTML 프리젠테이션
├── outputs/                 # 생성된 차트, 통계 요약표, 리포트 저장소
│   ├── figures/             # 시각화 이미지 (PNG, SVG)
│   └── tables/              # 요약 결과 테이블
├── ROADMAP.md               # 데이터 분석 진행 단계 및 To-Do 협업 체크리스트
└── README.md                # 본 프로젝트 안내서
```

---

## 🤝 AI와 사용자 간의 협업 가이드 (How We Collaborate)

1. **상태 공유 및 우선순위 조정 (`ROADMAP.md`)**:
   - 분석 단계(Phase 1~4)의 진행 상황을 `ROADMAP.md`에서 지속적으로 업데이트합니다.
   - 언제든 새로운 가설이나 분석하고 싶은 세부 토픽이 생기면 말씀해 주시면 로드맵에 반영합니다.

2. **레퍼런스 관리 (`references/BIBLIOGRAPHY.md`)**:
   - 논문, 기사, 정부 보고서 등 추가하고 싶은 자료는 `references/`에 넣거나 링크를 공유해 주시면 `BIBLIOGRAPHY.md`에 등재하고 분석 모델에 반영합니다.

3. **슬라이드덱 즉시 확인 (`slides/index.html`)**:
   - 브라우저(Chrome, Edge 등)로 `slides/index.html`을 열어 최신 분석 계획과 구조화된 인사이트를 슬라이드 형태로 열람하실 수 있습니다.

4. **파이썬 실행 환경**:
   - 기본 파이썬 인터프리터: `C:\Users\samsung\anaconda3\python.exe` (Python 3.13)
   - 데이터 분석 및 시각화는 Anaconda 환경의 `pandas`, `matplotlib`, `seaborn`, `statsmodels` 등을 활용합니다.

---

## 📊 빠른 시작 (Quick Start)

1. **슬라이드덱 열기**:
   - 탐색기에서 `slides/index.html` 파일을 더블 클릭하거나 브라우저에서 실행합니다.
   - 키보드 `좌/우 방향키(←, →)` 또는 하단 네비게이션으로 슬라이드를 넘길 수 있습니다.

2. **EDA 노트북 실행**:
   - `notebooks/` 폴더 내의 분석 노트북을 통해 데이터 탐색을 시작합니다.
