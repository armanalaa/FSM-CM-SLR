**Functional Size Measurement with Conceptual Models: A Systematic Literature Review**

This repository contains scripts, data, and results supporting the paper:

Functional Size Measurement with Conceptual Models: A Systematic Literature Review by Ala Arman et al.

**Project Background**

This repository supports research on functional size measurement (FSM) methods using conceptual models. The systematic literature review (SLR) investigates FSM approaches, analyzing key methodologies, challenges, and limitations across two decades (2004–2024). The study identifies influential studies, classifies FSM techniques, and provides actionable insights for future research.

**Use Cases**

- Researchers analyzing functional size measurement methods.
- Data analysts investigating citation trends and publication impact.
- Developers automating systematic literature review processes.


SLR-Functional-Size-Measurement/
├── data/
│   ├── raw/                  # Raw datasets
│   ├── processed/            # Processed datasets
├── results/                  # Analysis outputs
├── scripts/                  # Python scripts for processing
├── README.md                 # Documentation
└── requirements.txt          # Dependencies


**Repository Contents**

1. **Data**

data/raw/

R_Tot_1137.xlsx: The initial dataset containing 1137 papers retrieved through systematic search.
1137_CachedPapers.pkl: A consolidated cache of all retrieved papers stored in a Python dictionary. It includes metadata such as title, authors, venue, and citations for each paper.
allPapers.tsv: A tab-separated file summarizing all processed papers, including metadata and the queries that retrieved them. This file serves as the primary output for analysis or reporting.
queryCachedPapers/: Stores cached query results from Google Scholar, with each .pkl file corresponding to a specific query. These files speed up processing by avoiding repeated queries.
queryResults_tsv_xlsx/: Contains processed results of the queries in .tsv or .xlsx formats. These files are used for analysis or sharing in tabular formats.

data/processed/

R1_687.xlsx: The refined dataset after applying inclusion/exclusion criteria.
R_Tot_1137_with_publisher: R_Tot_1137.xlsx with an added column 'publisher' that includes the publisher information for all studies.

2. Scripts

scripts/fetch_all_studies.py: Fetches metadata of studies from online sources.

scripts/fetch_and_update_publishers.py: Queries to fetch and add publisher information to the dataset.

scripts/citation_analysis.py: Normalizes citation counts by publication year, identifies top 20% influential studies, and generates visualizations.

Scripts/log.txt: Logs the fetch_all_studies.py script

3. Results

results/top_20_percent_papers.xlsx: A list of papers in the top 20% by normalized citation counts.

results/Normalized_citation_distribution_with_the_80th_percentile_cutoff.png: A histogram visualizing the distribution of normalized citations with percentile markers.

**How to Use This Repository**

**Step 1: Clone the Repository**

Clone the repository to your local machine using:

git clone https://github.com/armanalaa/SLR-Functional-Size-Measurement.git

**Step 2: Install Dependencies**

Install the required Python packages listed in requirements.txt:

pip install -r requirements.txt

**Step 3: Process Data**

Run the provided scripts for various stages of data processing and analysis:

Fetch Metadata:

python scripts/fetch_all_studies.py

Update Publisher Information:

python scripts/fetch_and_update_publishers.py

Analyze Citations:

python scripts/citation_analysis.py


Step 4: Review Outputs

Check the results in the results/ directory for the processed datasets, visualizations, and analysis outputs.

**Key Features**

- Automated data fetching and updating using APIs.

- Normalization of citation counts to ensure fair comparison across publication years.

- Identification of influential studies using percentile thresholds.

- Comprehensive visualizations of citation trends.

**Dependencies**

The scripts in this repository depend on the following Python libraries:

pandas

openpyxl

matplotlib

requests

**To install dependencies:**

pip install pandas openpyxl matplotlib requests

**Reproducibility**

To ensure reproducibility of the results, use the following Python version:

- Python 3.x (tested with Python 3.9.x)

## Replacing `scholar_id` in `scripts/fetch_all_studies.py`

To ensure the script fetches data for the correct Google Scholar profile, follow these steps to replace the `scholar_id`:

### Steps:

1. **Locate the Scholar ID:**
   - Open the [Google Scholar profile](https://scholar.google.com/) of the target author or organization.
   - The `scholar_id` is the string in the URL after `user=`.
     - Example URL: `https://scholar.google.com/citations?user=_dS6nXMAAAAJ`
     - The `scholar_id` here is `_dS6nXMAAAAJ`.

2. **Edit the Script:**
   - Open the file `scripts/fetch_all_studies.py` in a text editor or IDE.
   - Locate the line:
     ```python
     scholar_id = 'scholar_id'
     ```
   - Replace `'scholar_id'` with the actual ID:
     ```python
     scholar_id = '_dS6nXMAAAAJ'
     ```

3. **Save the Changes:**
   - Save the file and ensure it is properly updated in the repository.

### Example:
If your target scholar's profile URL is:
`https://scholar.google.com/citations?user=abcd1234&hl=en`

Update the line in the script to:
```python
scholar_id = 'abcd1234'

**Known Issues**
- API limitations: CrossRef API may occasionally restrict access due to rate limits. Consider adding an API key for extended usage.
- Large datasets may lead to increased processing times.

## Troubleshooting: Resolving `MaxTriesExceededException: Cannot Fetch from Google Scholar`

The error `MaxTriesExceededException: Cannot Fetch from Google Scholar` occurs because Google Scholar blocks repeated access from the same IP address to prevent scraping. This is due to strict rate limits and anti-bot measures. Follow the steps below to resolve this issue.

---

### Steps to Fix the Issue

#### 1. Use a Proxy

Google Scholar blocks repeated access from the same IP address. Using a proxy service can bypass these restrictions.

##### Using ScraperAPI (Recommended)
1. Sign up for [ScraperAPI](https://www.scraperapi.com/) and obtain an API key.
2. Update your script to use the proxy:
   ```python
   from scholarly import ProxyGenerator

   pg = ProxyGenerator()
   API_KEY = '<Your ScraperAPI Key>'  # Replace with your ScraperAPI key
   success = pg.ScraperAPI(API_KEY)
   scholarly.use_proxy(pg)


**Citations**

If you use this repository in your research, please cite the following paper:

Ala Arman et al., *Functional Size Measurement with Conceptual Models: A Systematic Literature Review.*

Use the `requirements.txt` file to install exact versions of dependencies.

**Acknowledgments**

This study was carried out within the MICS (Made in Italy – Circular and Sustainable) Extended Partnership and received funding from Next- Generation EU (Italian PNRR – M4 C2, Invest 1.3 – D.D. 1551.11-10-2022, PE00000004).

**Contact**

For questions or feedback, please contact:

**Ala Arman**

Email: arman@diag.uniroma1.it

Department of Computer, Control and Management Engineering "Antonio Ruberti," Sapienza University of Rome