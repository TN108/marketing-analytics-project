import streamlit as st
import pandas as pd

from analytics_context import (
    load_campaign_metrics,
    get_segment_summary,
    load_model_metrics,
)

from copilot import ask_copilot


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Marketing Analytics AI Copilot",
    page_icon="📊",
    layout="wide",
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_app_data():

    campaigns = load_campaign_metrics()
    segments = get_segment_summary()
    model_metrics = load_model_metrics()

    return campaigns, segments, model_metrics


campaigns, segments, model_metrics = load_app_data()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("Marketing Analytics AI Copilot")

st.caption(
    "End-to-end marketing analytics MVP combining "
    "data engineering, machine learning, customer segmentation, "
    "Generative AI, and Streamlit."
)


# --------------------------------------------------
# EXECUTIVE KPI OVERVIEW
# --------------------------------------------------

st.header("Executive KPI Overview")

total_revenue = campaigns["total_revenue"].sum()
total_orders = campaigns["total_orders"].sum()
total_ad_spend = campaigns["total_ad_spend"].sum()

overall_roas = (
    total_revenue / total_ad_spend
    if total_ad_spend > 0
    else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"{total_revenue:,.0f}"
)

col2.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col3.metric(
    "Total Ad Spend",
    f"{total_ad_spend:,.2f}"
)

col4.metric(
    "Overall ROAS",
    f"{overall_roas:.2f}"
)


# --------------------------------------------------
# CAMPAIGN ANALYSIS
# --------------------------------------------------

st.header("Campaign Performance")

campaign_display = campaigns[
    [
        "campaign_id",
        "marketing_channel",
        "total_orders",
        "total_revenue",
        "total_ad_spend",
        "ctr_percent",
        "conversion_rate_percent",
        "roas",
    ]
].copy()

st.dataframe(
    campaign_display,
    use_container_width=True,
    hide_index=True,
)

st.subheader("ROAS by Marketing Channel")

roas_chart = campaigns.set_index(
    "marketing_channel"
)["roas"]

st.bar_chart(roas_chart)


# --------------------------------------------------
# CUSTOMER SEGMENTATION
# --------------------------------------------------

st.header("Customer Segmentation")

st.dataframe(
    segments,
    use_container_width=True,
    hide_index=True,
)

st.subheader("Customers by Segment")

segment_chart = segments.set_index(
    "segment_name"
)["customer_count"]

st.bar_chart(segment_chart)


# --------------------------------------------------
# CONVERSION MODEL
# --------------------------------------------------

st.header("Conversion Model Performance")

metrics_dict = dict(
    zip(
        model_metrics["metric"],
        model_metrics["value"]
    )
)

m1, m2, m3, m4 = st.columns(4)

m1.metric(
    "Accuracy",
    f"{metrics_dict.get('accuracy', 0):.4f}"
)

m2.metric(
    "Precision",
    f"{metrics_dict.get('precision', 0):.4f}"
)

m3.metric(
    "Recall",
    f"{metrics_dict.get('recall', 0):.4f}"
)

m4.metric(
    "F1 Score",
    f"{metrics_dict.get('f1_score', 0):.4f}"
)

m5, m6, m7 = st.columns(3)

m5.metric(
    "ROC AUC",
    f"{metrics_dict.get('roc_auc', 0):.4f}"
)

m6.metric(
    "PR AUC",
    f"{metrics_dict.get('pr_auc', 0):.4f}"
)

m7.metric(
    "Threshold",
    f"{metrics_dict.get('threshold', 0):.2f}"
)

st.info(
    "Accuracy should not be interpreted alone because "
    "the conversion target is highly imbalanced."
)


# --------------------------------------------------
# AI COPILOT
# --------------------------------------------------

st.header("AI Marketing Copilot")

st.write(
    "Ask questions about campaign performance, "
    "customer segments, or conversion-model results."
)

example_question = st.selectbox(
    "Example questions",
    [
        "",
        "Which campaign has the highest ROAS?",
        "Which campaign generated the most orders?",
        "Which customer segment should receive a retention campaign?",
        "How well does the conversion model perform?",
        "Where should the marketing budget be allocated?",
    ],
)

question = st.text_area(
    "Ask the Copilot",
    value=example_question,
    placeholder="Example: Which campaign has the highest ROAS?",
    height=100,
)


if st.button(
    "Ask Copilot",
    type="primary"
):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Analyzing trusted marketing analytics..."
        ):

            try:

                answer = ask_copilot(question)

                st.subheader("Copilot Response")

                st.markdown(answer)

            except Exception:

                st.error(
                    "The Copilot could not complete the request. "
                    "Check the API configuration and try again."
                )


# --------------------------------------------------
# LIMITATIONS
# --------------------------------------------------

st.divider()

st.caption(
    "Limitation: This project uses synthetic marketing data. "
    "AI recommendations should be treated as decision support, "
    "not automated business decisions."
)