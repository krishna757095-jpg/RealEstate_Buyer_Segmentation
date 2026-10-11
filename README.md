Real Estate Buyer Intelligence Dashboard
An interactive Streamlit dashboard for exploring real-estate buyer segments, segment-level summaries, and illustrative business recommendations.
[IMPORTANT]
Public-demo notice: This repository is a demonstration built with synthetic data. Its segment labels are illustrative and are not predictions from a trained or validated machine-learning model. Do not use this demo to make real customer, lending, valuation, or investment decisions. It does not reproduce or validate the results of the original private-data analysis.

Project at a glance
- Application: Python + Streamlit
- Data handling: Pandas
- Interface: Interactive browser-based dashboard
- Public data: Synthetic demo records only
- Purpose: Demonstrate how buyer segments and aggregate summaries can be explored in a dashboard
Dashboard features
- Filter demo buyer records by segment
- Review headline counts and segment distribution
- Explore segment profile summaries
- Read illustrative recommendations for each demo segment
- Inspect buyer-level demo records
- Download all columns for the currently filtered buyer records as a CSV file
Demo segments
Segment label	Interpretation in this demo
Developing Buyers	Illustrative segment used to demonstrate summaries
High-Value Buyers	Illustrative segment used to demonstrate investment-oriented summaries
Growth-Potential Buyers	Illustrative segment used to demonstrate potential-focused summaries


These names are demonstration labels. They should not be interpreted as validated customer personas or model predictions.
Repository contents
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
File	Description
app.py	Streamlit dashboard application
requirements.txt	Python dependencies required by the app
final_buyer_segmentation.csv	Synthetic buyer-level demo table
final_segment_profile.csv	Segment-level summary table for the demo
final_business_recommendations.csv	Illustrative recommendations by demo segment


This describes the intended public-demo files. Other files in a local working directory may not be tracked or published in this GitHub repository.
Run the app locally
Requirements
- Python version compatible with the packages pinned in requirements.txt
- Git, if cloning the repository
- Internet access to install Python dependencies
1. Clone the repository
git clone https://github.com/krishna757095-jpg/RealEstate_Buyer_Segmentation.git
cd RealEstate_Buyer_Segmentation
2. Create a virtual environment
Windows PowerShell:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
4. Start the dashboard
python -m streamlit run app.py
Open the local URL printed in the terminal, commonly http://localhost:8501.
Data and metric interpretation
The dashboard reads three prepared CSV outputs. In the current app.py, the required buyer fields are client_id, cluster, and segment_role. The app checks that these fields exist, that buyer IDs are present and unique, that cluster and segment labels are not missing, and that each cluster maps to only one segment role. These checks catch some structural problems; they do not, by themselves, establish that every metric is correct or that the original model is statistically valid.
Before relying on any metric, confirm its definition in the code and verify it against the data. In particular, distinguish totals from averages and ensure ratios use the intended numerator and denominator. Do not infer market-wide conclusions from synthetic demonstration records.
Validation scope and limitations
A successful app launch confirms only that the application starts in that environment. It does not independently establish:
- that the original machine-learning pipeline can be reproduced end to end;
- that the number of clusters is statistically optimal;
- that the clusters are stable or meaningful on unseen data;
- that recommendations improve business outcomes; or
- that the dashboard's outputs are suitable for real-world financial or property decisions.
For a complete ML project review, the preprocessing workflow, feature definitions, model-training code, cluster-selection rationale, evaluation metrics, and reproducibility steps must be checked separately.
Privacy and responsible publication
- Do not publish original client records or personally identifiable information.
- Never commit passwords, API keys, access tokens, .env files, or private backups.
- Review files before staging them with Git. .gitignore helps prevent accidental additions, but it does not remove files already committed or erase them from Git history.
- Use only data that you have permission to publish.
Deploy on Streamlit Community Cloud
1. Push the intended public-demo files to GitHub.
2. In Streamlit Community Cloud, create a new app connected to this repository.
3. Select branch main and main file path app.py.
4. Deploy and review the build logs.
5. Open the generated app URL in a private/incognito browser window.
6. Test the filters, summaries, tables, and CSV download.
A public URL means the app is accessible under its current sharing settings; it does not certify the scientific validity of the original analysis.
License
No open-source license is specified here. Unless a license is added, do not assume that reuse, redistribution, or modification is permitted.
Project status
Status: Public demonstration dashboard.
Scope: Interactive exploration of synthetic demo data. Original model training and scientific validation are not established by this dashboard alone.
