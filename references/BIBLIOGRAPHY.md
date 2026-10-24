# 프로젝트 레퍼런스 및 문헌 데이터베이스 (Bibliography & References)

본 문서는 **대한민국 행복 데이터 분석 프로젝트**에서 활용되는 1차 공식 보고서, 통계 지표, 그리고 심리학 및 경제학 학술 문헌의 출처와 메타데이터를 체계적으로 정리한 레퍼런스 아카이브입니다.

---

## 1. 핵심 공식 데이터 및 학술 문헌 (Core References)

### [REF-01] UN World Happiness Report 2026 (WHR 2026)
* **저자/발행기관**: Helliwell, J. F., Layard, R., Sachs, J. D., De Neve, J.-E., Aknin, L. B., & Wang, S. (Eds.) / UN Sustainable Development Solutions Network (SDSN)
* **발행연도**: 2026
* **보관 위치**:
  * 본 보고서: [`references/WHR26.pdf`](file:///C:/Users/samsung/Desktop/dataprogect/references/WHR26.pdf)
  * 통계 부록: [`references/WHR26_Statistical_Appendix.pdf`](file:///C:/Users/samsung/Desktop/dataprogect/references/WHR26_Statistical_Appendix.pdf)
  * 데이터셋: [`data/raw/WHR26_Data_Figure_2.1.xlsx`](file:///C:/Users/samsung/Desktop/dataprogect/data/raw/WHR26_Data_Figure_2.1.xlsx)
* **핵심 지표**:
  * **Life Evaluation (Cantril Ladder)**: 삶의 사다리 평가 (0~10점 척도, 3개년 이동평균)
  * **6대 설명 변수(Decomposition Factors)**: Log GDP per capita, Social support, Healthy life expectancy, Freedom to make life choices, Generosity, Perceptions of corruption.
* **대한민국 핵심 수치 (2025 기준)**:
  * 점수: **6.040점** / 전세계 **67위**
  * GDP(1.906) 및 기대수명(1.028)은 세계 최상위권이나, 관대함(0.089)과 사회적 지지(1.230)는 극단적 취약.

---

### [REF-02] 통계청 「국민 삶의 질 2024~2025」 보고서
* **발행기관**: 대한민국 정부 통계청 통계개발원 (KOSTAT)
* **주요 내용**: 고용, 건강, 교육, 소득·소비, 주거, 여가, 환경, 안전, 공동체, 시민참여, 가족 등 11개 영역 71개 지표 종합 측정.
* **한국적 시사점**: 객관적 물질 지표(소득, 기대수명)는 꾸준히 개선되었으나, 대인신뢰도(20%대)와 공동체 소속감, 여가 만족도는 정체되어 심리적 웰빙 취약성을 뒷받침.

---

### [REF-03] Does Economic Growth Improve the Human Lot? Some Empirical Evidence
* **저자**: Richard A. Easterlin (1974)
* **출처**: Nations and Households in Economic Growth (Academic Press)
* **핵심 이론 (이스털린의 역설)**: 소득이 일정 수준을 넘어서면 추가적인 소득 증가가 국가 전체의 행복 증진으로 이어지지 않음. 한국 1인당 GDP 3만 5천 달러 시대의 행복 정체를 설명하는 대표 이론.

---

### [REF-04] Flourish: A Visionary New Understanding of Happiness and Well-being (PERMA Model)
* **저자**: Martin E. P. Seligman (2011)
* **출처**: Free Press / Simon & Schuster
* **핵심 개념**: 웰빙을 5가지 독립적 차원(Positive Emotion, Engagement, Relationships, Meaning, Accomplishment)으로 정의. 한국인의 경우 성취(A)는 세계 최고 수준이나 관계(R)와 긍정정서(P)의 결핍이 두드러짐.

---

## 2. 2차 연계 데이터셋: Kaggle WHR 한국 장기 패널 (2005~2023)
* **식별자**: `jainaru/world-happiness-report-2024-yearly-updated` (Arpit Jain / Gallup World Poll)
* **규모**: 전 세계 160여 개국 2,363개 관측치 중 **한국 2006~2023년 18개년 연속 패널**
* **특화 지표**: 
  * `Life Ladder`, `Log GDP per capita`, `Social support`, `Healthy life expectancy`, `Freedom`, `Generosity`, `Perceptions of corruption` 실측치
  * **`Positive affect` (긍정적 정서: 웃음, 즐거움, 흥미)** 및 **`Negative affect` (부정적 정서: 불안, 슬픔, 걱정, 분노)** 완비
