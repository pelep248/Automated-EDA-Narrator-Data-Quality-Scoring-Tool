# Dataset class (facade/orchestrator)
# src/orchestrator.py
from loader import DataLoader
from preprocessor import Preprocessor
from eda_analyzer import EDAAnalyzer
from quality_scorer import QualityScorer
from narrator import Narrator
from report_builder import ReportBuilder

class DatasetPipeline:
    def __init__(self, path):
        self.loader = DataLoader(path)
        self.df = None
        self.pre = None
        self.eda = None
        self.scores = None
        self.narrative = None
        self.report = None

    def run(self):
        self.df = self.loader.load()
        # basic preprocessing
        self.pre = Preprocessor(self.df).trim_strings(self.df.select_dtypes(include=['object']).columns.tolist())
        clean_df = self.pre.get()
        # analysis
        analyzer = EDAAnalyzer(clean_df)
        eda_results = analyzer.run_all()
        # scoring
        scorer = QualityScorer(eda_results, df_len=len(clean_df))
        scorer.overall_score()
        scores = scorer.scores
        # narration
        narrator = Narrator(eda_results, scores)
        narrative = narrator.generate()
        # report
        builder = ReportBuilder(narrative, eda_results, scores)
        md = builder.to_markdown()
        self.eda = eda_results
        self.scores = scores
        self.narrative = narrative
        self.report = md
        return md
