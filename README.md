# Automated-EDA-Narrator-Data-Quality-Scoring-Tool
# DatasetSense: Automated EDA Narrator + Data Quality Scoring Tool

## 1. Project Overview
DatasetSense is a Python tool that performs **automated exploratory data analysis (EDA)** and computes a **dataset quality score (0–100)**. It generates **human-readable insights** and produces a **markdown report** summarizing dataset characteristics and quality.  

The project demonstrates **object-oriented programming (OOP)** concepts including **encapsulation, inheritance, polymorphism, composition, and dunder methods**.

---

## 2. Team Members
| Member | Role |
|--------|------|
| Member 1 | DataLoader + Preprocessor |
| Member 2 | NumericAnalyzer + CategoricalAnalyzer (EDA) |
| Member 3 | QualityScorer |
| Member 4 | Narrator |
| Member 5 | DatasetPipeline + ReportBuilder + Integration |

---

## 3. Features

### Automated EDA
- Numeric analysis: mean, std, quartiles, outliers
- Categorical analysis: value counts, top categories
- Missing value and duplicate detection
- Correlation matrix for numeric columns

### Data Quality Scoring
- Missing values, duplicates, outliers, balance score
- Weighted overall score (0–100)
- Simple verdict: Excellent / Good / Fair / Poor

### Report Generation
- Narrative insights in human-readable sentences
- Markdown-formatted quality report
- Optional JSON output

---

## 4. Object-Oriented Design

| Concept | Implementation |
|---------|----------------|
| **Classes** | 6 core classes: `DataLoader`, `Preprocessor`, `EDAAnalyzer`, `QualityScorer`, `Narrator`, `ReportBuilder` |
| **Encapsulation** | Protected attributes (e.g., `_df`, `_eda`, `_scores`) with getter methods |
| **Inheritance** | `NumericAnalyzer` & `CategoricalAnalyzer` inherit from `EDAAnalyzer` |
| **Polymorphism** | `run_all()` overridden in child classes for numeric vs categorical data |
| **Dunder Methods** | `__repr__`, `__eq__`, `__len__` in `DataLoader`; `__repr__` in `DatasetPipeline` |
| **Composition** | `DatasetPipeline` contains Loader, Preprocessor, Analyzer, Scorer, Narrator, and ReportBuilder |

---

## 5. Project Structure



# Dataset Facade UML

![Dataset UML](dataset_uml.png)
