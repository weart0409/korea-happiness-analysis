"""
WHR (World Happiness Report) 데이터 로더 및 전처리 유틸리티
"""

import os
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "WHR26_Data_Figure_2.1.xlsx"


def load_whr_data(excel_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """WHR 원본 엑셀 데이터를 로드하여 정리된 DataFrame으로 반환합니다."""
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"데이터 파일을 찾을 수 없습니다: {excel_path}")

    xls = pd.ExcelFile(excel_path)
    sheet_name = xls.sheet_names[0]
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    return df


def get_korea_series(df: pd.DataFrame = None) -> pd.DataFrame:
    """대한민국(Republic of Korea / South Korea)의 시계열 데이터를 추출하고 정렬합니다."""
    if df is None:
        df = load_whr_data()

    korea_df = df[df["Country name"].astype(str).str.contains("Korea", case=False, na=False)].copy()
    korea_df = korea_df.sort_values(by="Year").reset_index(drop=True)
    return korea_df


def get_oecd_comparison(year: int = 2025, df: pd.DataFrame = None) -> pd.DataFrame:
    """특정 연도의 OECD 주요국 및 글로벌 상위국 비교 데이터를 추출합니다."""
    if df is None:
        df = load_whr_data()

    year_df = df[df["Year"] == year].copy()
    return year_df


if __name__ == "__main__":
    korea = get_korea_series()
    print("=== 대한민국 시계열 행복 데이터 (2011~2025) ===")
    print(korea[["Year", "Rank", "Life evaluation (3-year average)"]])
