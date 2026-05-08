"""BOM Reader module for loading and validating Excel BOM files."""

import pandas as pd
from pathlib import Path

REQUIRED_COLUMNS = [
    "BOM Line",
    "Internal Part Number",
    "Description",
    "Manufacturer / Vendor",
    "Vendor Part Number",
    "Vendor Contact Name",
    "Vendor Contact Email",
    "Compliance Required",
    "Current Status",
]


def load_bom(file_path: str) -> pd.DataFrame:
    """Load a BOM Excel file and return as DataFrame."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"BOM file not found: {file_path}")
    if path.suffix.lower() != ".xlsx":
        raise ValueError(f"Expected .xlsx file, got: {path.suffix}")

    return pd.read_excel(file_path, engine="openpyxl")


def validate_bom(df: pd.DataFrame) -> tuple[bool, str]:
    """Validate that required columns exist in the BOM."""
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        return False, f"Missing required columns: {missing}"
    return True, "BOM is valid"
