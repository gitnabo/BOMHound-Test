# BOMHound

Local-first prototype for collecting and reviewing supplier compliance documentation from BOM spreadsheets.

## Setup

```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Run

```powershell
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Test Data

The test BOM is located at `data/test_bom.xlsx` with 3 sample parts.
