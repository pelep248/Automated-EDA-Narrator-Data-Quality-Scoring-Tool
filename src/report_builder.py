# Composition
from tabulate import tabulate

class ReportBuilder:
    def __init__(self, narrative, scores, eda_results):
        self._narrative = narrative
        self._scores = scores
        self._eda = eda_results

    def to_markdown(self):
        md = ["# Automated EDA Report\n", "## Narrative Insights"]
        for s in self._narrative:
            md.append(f"- {s}")
        md.append("\n## Quality Scores")
        rows = [(k, v) for k,v in self._scores.items()]
        md.append(tabulate(rows, headers=["Metric","Score"], tablefmt="github"))
        return "\n\n".join(md)
