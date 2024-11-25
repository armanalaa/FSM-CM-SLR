# Functional Size Measurement with Conceptual Models: A Systematic Literature Review

This repository contains scripts, data, and results supporting the paper:

*Functional Size Measurement with Conceptual Models: A Systematic Literature Review* by Ala Arman et al.

## Project Background

This repository supports research on functional size measurement (FSM) methods using conceptual models. The systematic literature review (SLR) investigates FSM approaches, analyzing key methodologies, challenges, and limitations across two decades (2004–2024). The study identifies influential studies, classifies FSM techniques, and provides actionable insights for future research.

## Use Cases

- Researchers analyzing functional size measurement methods
- Data analysts investigating citation trends and publication impact
- Developers automating systematic literature review processes

## Directory Structure

```
SLR-Functional-Size-Measurement/
├── data/
│   ├── raw/                  # Raw datasets
│   ├── processed/            # Processed datasets
├── results/                  # Analysis outputs
├── scripts/                  # Python scripts for processing
├── README.md                 # Documentation
└── requirements.txt          # Dependencies
```

## Repository Contents

### 1. Data

#### data/raw/
- **R_Tot_1137.xlsx**: Initial dataset containing 1137 papers from systematic search
- **1137_CachedPapers.pkl**: Consolidated cache of retrieved papers in Python dictionary format
- **allPapers.tsv**: Tab-separated summary file of all processed papers
- **queryCachedPapers/**: Cached Google Scholar query results
- **queryResults_tsv_xlsx/**: Processed query results in tabular formats

#### data/processed/
- **R1_687.xlsx**: Refined dataset after applying inclusion/exclusion criteria
- **R_Tot_1137_with_publisher**: Dataset with added publisher information

### 2. Scripts
- **scripts/fetch_all_studies.py**: Fetches study metadata from online sources
- **scripts/fetch_and_update_publishers.py**: Updates dataset with publisher information
- **scripts/citation_analysis.py**: Performs citation analysis and generates visualizations
- **Scripts/log.txt**: Script execution logs

### 3. Results
- **results/top_20_percent_papers.xlsx**: Papers in top 20% by normalized citation counts
- **results/Normalized_citation_distribution.png**: Citation distribution visualization

## Usage Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/armanalaa/SLR-Functional-Size-Measurement.git
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Process Data

Execute the scripts in sequence:

```bash
python scripts/fetch_all_studies.py
python scripts/fetch_and_update_publishers.py
python scripts/citation_analysis.py
```

### Step 4: Review Outputs

Check the `results/` directory for processed datasets and visualizations.

### Step 5: Configure Google Scholar ID

1. **Locate the Scholar ID**:
   - Visit the author's [Google Scholar profile](https://scholar.google.com/)
   - Extract the ID from the URL after `user=`
   - Example: In `https://scholar.google.com/citations?user=_dS6nXMAAAAJ`, the ID is `_dS6nXMAAAAJ`

2. **Update the Script**:
   ```python
   # In scripts/fetch_all_studies.py
   scholar_id = 'YOUR_SCHOLAR_ID'  # Replace with actual ID
   ```

## Key Features

- Automated data fetching and updating via APIs
- Citation count normalization for fair comparison
- Influential study identification using percentile thresholds
- Comprehensive citation trend visualizations

## Dependencies

Required Python libraries:
- pandas
- openpyxl
- matplotlib
- requests

Install via pip:
```bash
pip install pandas openpyxl matplotlib requests
```

## Reproducibility

Tested with Python 3.9.x

## Known Issues

- CrossRef API may impose rate limits
- Large datasets may increase processing time

## Troubleshooting

### Resolving `MaxTriesExceededException`

If encountering Google Scholar access restrictions:

1. **Use ScraperAPI (Recommended)**:
   ```python
   from scholarly import ProxyGenerator

   pg = ProxyGenerator()
   API_KEY = '<Your ScraperAPI Key>'
   success = pg.ScraperAPI(API_KEY)
   scholarly.use_proxy(pg)
   ```

## Citation

If using this repository, please cite:

```
Ala Arman et al., "Functional Size Measurement with Conceptual Models: A Systematic Literature Review"
```

## Acknowledgments

This study was supported by the MICS (Made in Italy – Circular and Sustainable) Extended Partnership and funded by Next-Generation EU (Italian PNRR – M4 C2, Invest 1.3 – D.D. 1551.11-10-2022, PE00000004).

## Contact

**Ala Arman**  
Department of Computer, Control and Management Engineering "Antonio Ruberti"  
Sapienza University of Rome  
Email: arman@diag.uniroma1.it
