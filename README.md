# Real Estate Buyer Intelligence Dashboard

A Streamlit dashboard demonstrating buyer segmentation and investment profiling for real estate market intelligence.

## Public demo data

The CSV files included in this public repository are **synthetic demonstration data**. They are not the original client records and must not be interpreted as the original project's empirical findings.

The original buyer-level dataset is excluded from this public repository because it contains personal and investment-related information.

## Features

- Buyer segment distribution
- Segment profiles and business recommendations
- Segment filtering and buyer explorer
- Downloadable filtered demo data

## Project files

- `app.py` — Streamlit dashboard
- `requirements.txt` — Python dependencies
- `notebooks/outputs/final_project_package/tables/` — synthetic demo CSV files

## Run locally on Windows

1. Install Python.
2. Open PowerShell in the project root.
3. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the dashboard:

   ```powershell
   python -m streamlit run app.py
   ```

6. Open the local URL shown in the terminal.

## Data privacy

Do not add original client records, personal identifiers, credentials, `.env` files, virtual environments, or private backups to a public repository.

## Limitations

This public version uses synthetic data to demonstrate dashboard functionality. Its displayed counts, investment figures, and recommendations are illustrative and are not validated real-world findings or financial advice.
