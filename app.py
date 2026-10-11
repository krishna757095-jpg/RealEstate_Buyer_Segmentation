
from pathlib import Path

import pandas as pd
import streamlit as st


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent

PACKAGE_TABLES = (
    PROJECT_ROOT
    / "notebooks"
    / "outputs"
    / "final_project_package"
    / "tables"
)

SOURCE_TABLES = PROJECT_ROOT / "notebooks" / "outputs" / "tables"

BUYER_FILE = "final_buyer_segmentation.csv"
PROFILE_FILE = "final_segment_profile.csv"
RECOMMENDATION_FILE = "final_business_recommendations.csv"


st.set_page_config(
    page_title="Real Estate Buyer Intelligence",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def load_csv(path_string):
    return pd.read_csv(path_string)


def locate_tables():
    required = [
        BUYER_FILE,
        PROFILE_FILE,
        RECOMMENDATION_FILE,
    ]

    for folder in (PACKAGE_TABLES, SOURCE_TABLES):
        if all((folder / name).is_file() for name in required):
            return folder

    return None


def format_number(value, decimals=2):
    if pd.isna(value):
        return "N/A"
    return f"{value:,.{decimals}f}"


# --------------------------------------------------
# LOAD EXISTING VALIDATED OUTPUTS
# --------------------------------------------------
st.title("🏠 Real Estate Buyer Intelligence Dashboard")
st.caption(
    "Buyer segmentation, investment profiling and "
    "segment-level business recommendations"
)

table_folder = locate_tables()

if table_folder is None:
    st.error(
        "Required CSV files were not found in either the "
        "final package tables folder or notebooks/outputs/tables."
    )
    st.info(
        "Check the existing project paths. Do not recreate or "
        "overwrite the validated CSV files."
    )
    st.stop()

try:
    buyers = load_csv(str(table_folder / BUYER_FILE))
    profile = load_csv(str(table_folder / PROFILE_FILE))
    recommendations = load_csv(
        str(table_folder / RECOMMENDATION_FILE)
    )
except Exception as exc:
    st.error(f"Unable to load project data: {exc}")
    st.stop()


# --------------------------------------------------
# SCHEMA VALIDATION
# --------------------------------------------------
required_buyer_columns = {
    "client_id",
    "cluster",
    "segment_role",
}

missing = required_buyer_columns - set(buyers.columns)

if missing:
    st.error(
        "Buyer dataset is missing required columns: "
        + ", ".join(sorted(missing))
    )
    st.stop()

if buyers.empty:
    st.error("The buyer segmentation dataset is empty.")
    st.stop()

if buyers["client_id"].isna().any():
    st.error("Buyer dataset contains blank client IDs.")
    st.stop()

if buyers["client_id"].duplicated().any():
    st.error("Duplicate client IDs detected. Dashboard stopped.")
    st.stop()

if buyers["cluster"].isna().any():
    st.error("Missing cluster labels detected.")
    st.stop()

if buyers["segment_role"].isna().any():
    st.error("Missing segment roles detected.")
    st.stop()

cluster_role_counts = (
    buyers.groupby("cluster")["segment_role"].nunique()
)

if (cluster_role_counts > 1).any():
    st.error(
        "A cluster maps to multiple segment roles. "
        "Resolve the mapping before using this dashboard."
    )
    st.stop()


# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("Dashboard Filters")

roles = sorted(buyers["segment_role"].astype(str).unique())

selected_roles = st.sidebar.multiselect(
    "Buyer segment",
    options=roles,
    default=roles,
)

filtered = buyers[
    buyers["segment_role"].astype(str).isin(selected_roles)
].copy()

st.sidebar.caption(f"Data source: {table_folder.relative_to(PROJECT_ROOT)}")


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------
st.subheader("Business Overview")

c1, c2, c3 = st.columns(3)

c1.metric("Total Buyers", f"{len(filtered):,}")
c2.metric(
    "Segments Selected",
    f"{filtered['segment_role'].nunique():,}",
)
c3.metric(
    "Unique Clusters",
    f"{filtered['cluster'].nunique():,}",
)

st.divider()


# --------------------------------------------------
# SEGMENT DISTRIBUTION
# --------------------------------------------------
st.subheader("Buyer Segment Distribution")

segment_counts = (
    filtered["segment_role"]
    .value_counts()
    .rename_axis("Segment")
    .reset_index(name="Buyer Count")
)

left, right = st.columns(2)

with left:
    st.markdown("**Buyers by segment**")
    if not segment_counts.empty:
        st.bar_chart(
            segment_counts.set_index("Segment")["Buyer Count"]
        )
    else:
        st.info("No buyers match the selected filters.")

with right:
    st.markdown("**Segment counts and percentages**")

    if len(filtered) > 0:
        segment_counts["Buyer Percentage"] = (
            segment_counts["Buyer Count"]
            / len(filtered)
            * 100
        ).round(2)

        st.dataframe(
            segment_counts,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Select at least one segment.")


# --------------------------------------------------
# PROFILE AND RECOMMENDATIONS
# --------------------------------------------------
st.divider()
st.subheader("Segment Profiles")

if "segment_role" in profile.columns:
    visible_profile = profile[
        profile["segment_role"].astype(str).isin(selected_roles)
    ].copy()

    st.dataframe(
        visible_profile,
        use_container_width=True,
        hide_index=True,
    )
else:
    st.warning(
        "The profile CSV does not contain segment_role; "
        "its table cannot be filtered safely."
    )
    st.dataframe(profile, use_container_width=True)


st.subheader("Business Recommendations")

if "segment_role" in recommendations.columns:
    visible_recommendations = recommendations[
        recommendations["segment_role"].astype(str).isin(
            selected_roles
        )
    ].copy()

    st.dataframe(
        visible_recommendations,
        use_container_width=True,
        hide_index=True,
    )
else:
    st.warning(
        "The recommendations CSV does not contain segment_role."
    )
    st.dataframe(recommendations, use_container_width=True)


# --------------------------------------------------
# BUYER EXPLORER
# --------------------------------------------------
st.divider()
st.subheader("Buyer Explorer")

preferred_columns = [
    "client_id",
    "segment_role",
    "cluster",
    "country",
    "region",
    "transaction_count",
    "total_investment",
    "average_property_value",
    "days_since_last_transaction",
    "satisfaction_score",
]

display_columns = [
    col for col in preferred_columns if col in filtered.columns
]

if not display_columns:
    display_columns = list(filtered.columns[:10])

st.dataframe(
    filtered[display_columns],
    use_container_width=True,
    hide_index=True,
)

st.download_button(
    label="Download Filtered Buyer Data (CSV)",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="filtered_buyer_segmentation.csv",
    mime="text/csv",
)

st.caption(
    "This dashboard reads the existing project outputs. "
    "It does not retrain the model or modify the source CSV files."
)
