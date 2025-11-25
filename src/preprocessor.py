# Preprocessor
# src/preprocessor.py
import pandas as pd
from dateutil import parser
from typing import List

class Preprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def trim_strings(self, cols: List[str]):
        for c in cols:
            if c in self.df:
                self.df[c] = self.df[c].astype(str).str.strip()
        return self

    def try_parse_dates(self, cols: List[str]):
        for c in cols:
            if c in self.df:
                def _p(x):
                    try:
                        return parser.parse(x) if pd.notna(x) else x
                    except Exception:
                        return x
                self.df[c] = self.df[c].apply(_p)
        return self

    def drop_constant_columns(self):
        nunique = self.df.nunique(dropna=False)
        const_cols = nunique[nunique <= 1].index.tolist()
        self.df.drop(columns=const_cols, inplace=True)
        return self

    def get(self):
        return self.df
