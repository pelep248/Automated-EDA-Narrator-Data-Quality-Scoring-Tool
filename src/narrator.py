# Narrator
# src/narrator.py
from typing import Dict, List

class Narrator:
    def __init__(self, eda_results: Dict, quality_scores: Dict):
        self.eda = eda_results
        self.scores = quality_scores

    def numeric_summary_sentences(self, top_n=3) -> List[str]:
        outs = []
        summary = self.eda.get('summary', {})
        for col, metrics in (summary.items() if isinstance(summary, dict) else []):
            try:
                mean = metrics.get('mean')
                std = metrics.get('std')
                if mean is None:
                    continue
                sent = f"Column '{col}' has mean {mean:.2f} and std {std:.2f}."
                outs.append(sent)
                if len(outs) >= top_n:
                    break
            except Exception:
                continue
        return outs

    def missing_sentences(self) -> List[str]:
        miss = self.eda.get('missing', {})
        outs = []
        for col, info in miss.items():
            if info['missing'] > 0:
                outs.append(f"Column '{col}' has {info['missing']} missing values ({info['pct']}%).")
        return outs

    def outlier_sentences(self) -> List[str]:
        out = self.eda.get('outliers', {})
        return [f"Column '{c}' has {n} detected outliers." for c, n in out.items() if n > 0]

    def score_sentence(self):
        overall = self.scores.get('overall', None)
        if overall is None:
            return "Overall data quality score not computed."
        verdict = "Excellent" if overall >= 90 else "Good" if overall >= 75 else "Fair" if overall >= 50 else "Poor"
        return f"Overall data quality: {overall}/100 — {verdict}."

    def generate(self) -> List[str]:
        text = []
        text.extend(self.numeric_summary_sentences())
        text.extend(self.missing_sentences())
        text.extend(self.outlier_sentences())
        text.append(self.score_sentence())
        return text
