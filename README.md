# Real Estate Buyer Intelligence Dashboard

An interactive **Streamlit dashboard** for exploring real-estate buyer segments, segment summaries, and illustrative business recommendations.

> **Demo and data notice:** This public repository uses synthetic demonstration data. Segment labels are illustrative categories, not predictions from a trained or validated machine-learning model. This dashboard does not reproduce or validate the original analysis and must not be used to make real customer, lending, property-valuation, or investment decisions.

## Project overview

The app reads three prepared CSV files and presents buyer-segment information in an interactive browser dashboard. It is designed to demonstrate data exploration and presentation—not to train a model.

## Dashboard features

- Filter buyer records by `segment_role`.
- View the number of buyers, selected segments, and clusters for the current selection.
- Compare buyer counts and percentages for the filtered records.
- View segment-profile summaries.
- View illustrative business recommendations by segment.
- Explore selected buyer-level fields.
- Download the currently filtered buyer records as a CSV.
- Check required buyer columns, missing or duplicate client IDs, missing cluster/segment labels, and whether a cluster maps to more than one segment role.

## Demo segment labels

| Segment | Meaning in this public demo |
|---|---|
| Developing Buyers | Illustrative label for dashboard demonstration |
| High-Value Buyers | Illustrative label for dashboard demonstration |
| Growth-Potential Buyers | Illustrative label for dashboard demonstration |

These labels are not validated customer personas or machine-learning predictions.

## Technology stack

- **Python** — application logic
- **Streamlit** — interactive dashboard
- **Pandas** — CSV loading and tabular data handling

## Repository structure

```text
RealEstate_Buyer_Segmentation/
├── app.py
├── requirements.txt
├── README.md
└── notebooks/
    └── outputs/
        └── final_project_package/
            └── tables/
                ├── final_buyer_segmentation.csv
                ├── final_segment_profile.csv
                └── final_business_recommendations.csv
```

| File | Purpose |
|---|---|
| `app.py` | Loads the prepared CSVs, applies filters, displays summaries, and provides CSV download |
| `requirements.txt` | Lists the pinned Python dependencies |
| `final_buyer_segmentation.csv` | Buyer-level synthetic demo data |
| `final_segment_profile.csv` | Segment-level profile table |
| `final_business_recommendations.csv` | Illustrative recommendations by segment |

The tree above describes the intended public-demo files. Your local working folder may contain additional notebooks, reports, scripts, or outputs that are not tracked in the public repository.

## Run locally

### Requirements

- A Python version compatible with the dependencies listed in `requirements.txt`
- Internet access to install packages

### 1. Clone the repository

```bash
git clone https://github.com/krishna757095-jpg/RealEstate_Buyer_Segmentation.git
cd RealEstate_Buyer_Segmentation
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Start the dashboard

```bash
python -m streamlit run app.py
```

Open the local URL printed in the terminal, usually `http://localhost:8501`.

## Data validation and interpretation

The current app requires the buyer table to contain `client_id`, `cluster`, and `segment_role`. It checks that the buyer table is not empty, client IDs are present and unique, cluster and segment labels are not missing, and each cluster maps to no more than one segment role.

These checks catch selected structural problems. They do not verify every numeric metric, prove that segment labels are statistically meaningful, or establish the validity of the original machine-learning analysis.

The dashboard reads prepared outputs and does not retrain a model or modify the source CSV files.

## Important limitations

This public demo does not, by itself, demonstrate:

- an end-to-end reproducible machine-learning training pipeline;
- an optimal number of clusters;
- cluster stability or performance on unseen data;
- verified real-world business impact; or
- validated property valuations or investment advice.

Those claims require separate evidence, including the original preprocessing workflow, feature definitions, model-training code, evaluation metrics, and appropriate validation.

## Privacy and responsible publication

- Publish only data you have permission to share.
- Do not commit original client records, personally identifiable information, credentials, API keys, passwords, `.env` files, or private backups.
- Review staged files before committing them.
- `.gitignore` helps prevent accidental additions but does not remove sensitive files that were already committed or erase them from Git history.

## Deploy on Streamlit Community Cloud

1. Push the intended public-demo files to GitHub.
2. Create an app in Streamlit Community Cloud and connect this repository.
3. Select branch `main` and main file path `app.py`.
4. Deploy and review the build logs.
5. Open the generated URL in an incognito/private browser window.
6. Test the segment filter, charts, profile table, recommendations, and CSV download.

A successful deployment confirms that the app runs in that environment; it does not independently validate the original machine-learning analysis.

## License

No open-source license is specified in this repository. Unless a license is added, do not assume that reuse, redistribution, or modification is permitted.

## Project status

**Status:** Public demonstration dashboard.

**Scope:** Interactive exploration of synthetic data and prepared CSV outputs. Original model training and scientific validation are not established by this dashboard alone.
