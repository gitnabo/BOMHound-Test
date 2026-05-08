"""BOMHound - BOM Compliance Tracking Web UI."""

import streamlit as st
from pathlib import Path

from bom_reader import load_bom, validate_bom

BOM_FILE_PATH = Path(__file__).parent / "data" / "test_bom.xlsx"

st.set_page_config(
    page_title="BOMHound",
    page_icon="📋",
    layout="wide"
)

st.title("BOMHound - BOM Compliance Tracker")
st.markdown("View and track supplier compliance documentation status.")

try:
    df = load_bom(str(BOM_FILE_PATH))
    is_valid, message = validate_bom(df)

    if not is_valid:
        st.warning(message)

    st.subheader(f"BOM: {BOM_FILE_PATH.name}")
    st.caption(f"Loaded {len(df)} rows")

    st.dataframe(df, use_container_width=True, hide_index=True)

except FileNotFoundError as e:
    st.error(f"File not found: {e}")
except Exception as e:
    st.error(f"Error loading BOM: {e}")
