from pathlib import Path

import pandas as pd


# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"


# --------------------------------------------------
# LOAD PREPARED DATA
# --------------------------------------------------

def load_campaign_metrics():
    """
    Load prepared campaign-level Gold metrics.
    """

    path = DATA_DIR / "campaign_metrics.csv"

    if not path.exists():
        raise FileNotFoundError(
            f"Campaign metrics file not found: {path}"
        )

    return pd.read_csv(path)


def load_customer_segments():
    """
    Load customer-level RFM + K-Means segmentation results.
    """

    path = DATA_DIR / "customer_segments.csv"

    if not path.exists():
        raise FileNotFoundError(
            f"Customer segments file not found: {path}"
        )

    return pd.read_csv(path)


def load_model_metrics():
    """
    Load final conversion-model evaluation metrics.

    Supports a few possible filenames used during the project.
    """

    possible_files = [
        DATA_DIR / "conversion_model_metrics.csv",
        DATA_DIR / "conversion_metrics.csv",
        DATA_DIR / "customer_segmentation.csv",
    ]

    for path in possible_files:
        if path.exists():
            return pd.read_csv(path)

    raise FileNotFoundError(
        "Conversion model metrics file was not found in "
        f"{DATA_DIR}"
    )


# --------------------------------------------------
# CUSTOMER SEGMENT SUMMARY
# --------------------------------------------------

def get_segment_summary():
    """
    Convert 155 customer-level rows into a compact
    one-row-per-segment summary.

    This reduces token usage and prevents customer IDs
    from being sent to the LLM.
    """

    df = load_customer_segments()

    summary = (
        df.groupby("segment_name")
        .agg(
            customer_count=("customer_id", "count"),
            avg_recency=("recency", "mean"),
            avg_frequency=("frequency", "mean"),
            avg_monetary=("monetary", "mean"),
            recommended_action=("recommended_action", "first"),
        )
        .reset_index()
    )

    # Keep LLM context compact and readable
    summary["avg_recency"] = summary["avg_recency"].round(2)
    summary["avg_frequency"] = summary["avg_frequency"].round(2)
    summary["avg_monetary"] = summary["avg_monetary"].round(2)

    return summary


# --------------------------------------------------
# COMPLETE ANALYTICS CONTEXT
# --------------------------------------------------

def build_analytics_context():
    """
    Build the full trusted analytics context.

    This is useful when the application needs the complete
    summarized project context.
    """

    campaigns = load_campaign_metrics()
    segments = get_segment_summary()
    model_metrics = load_model_metrics()

    overall_kpis = {
        "total_revenue": float(
            campaigns["total_revenue"].sum()
        ),
        "total_orders": int(
            campaigns["total_orders"].sum()
        ),
        "total_ad_spend": float(
            campaigns["total_ad_spend"].sum()
        ),
    }

    # Overall ROAS
    if overall_kpis["total_ad_spend"] > 0:
        overall_kpis["overall_roas"] = round(
            overall_kpis["total_revenue"]
            / overall_kpis["total_ad_spend"],
            2,
        )

    campaign_performance = campaigns.to_dict(
        orient="records"
    )

    customer_segments = segments.to_dict(
        orient="records"
    )

    # conversion metrics CSV is stored as:
    # metric,value
    model_performance = dict(
        zip(
            model_metrics["metric"],
            model_metrics["value"],
        )
    )

    analytics_context = {
        "overall_kpis": overall_kpis,

        "campaign_performance": campaign_performance,

        "rfm_definition": {
            "recency": (
                "How recently a customer made a purchase."
            ),
            "frequency": (
                "How often a customer made purchases."
            ),
            "monetary": (
                "How much value a customer generated "
                "through purchases."
            ),
        },

        "customer_segments": customer_segments,

        "model_performance": model_performance,

        "data_limitations": [
            "The project uses synthetic marketing data.",
            "The conversion target is highly imbalanced.",
            (
                "Model predictions should support marketing "
                "decisions rather than automatically trigger "
                "customer contact."
            ),
        ],
    }

    return analytics_context


# --------------------------------------------------
# RAG ROUTING KEYWORDS
# --------------------------------------------------

campaign_keywords = [
    "roas",
    "ad spend",
    "marketing channel",
    "ctr",
    "click",
    "orders",
    "campaign performance",
    "campaign revenue",
    "campaign generated",
    "highest revenue",
    "best campaign",
    "marketing budget",
    "budget allocation",
]


segment_keywords = [
    "segment",
    "customer segment",
    "rfm",
    "recency",
    "frequency",
    "monetary",
    "at-risk",
    "at risk",
    "loyal",
    "retention",
    "high-value",
    "high value",
    "low-value",
    "low value",
    "cluster",
    "customer group",
]


model_keywords = [
    "model",
    "conversion model",
    "precision",
    "recall",
    "accuracy",
    "f1",
    "roc",
    "auc",
    "pr auc",
    "threshold",
    "prediction",
    "classifier",
    "false positive",
    "false negative",
    "true positive",
    "true negative",
]


# --------------------------------------------------
# RETRIEVE ONLY RELEVANT CONTEXT
# --------------------------------------------------

def retrieve_relevant_context(question: str):
    """
    Retrieve only the analytics sections relevant
    to the user's question.

    This prevents the complete dataset from being
    sent to the LLM for every query.
    """

    question = question.lower().strip()

    context = {
        "data_limitations": [
            "The project uses synthetic marketing data."
        ]
    }

    matched = False

    # --------------------------------------------------
    # CAMPAIGN QUESTIONS
    # --------------------------------------------------

    if any(
        keyword in question
        for keyword in campaign_keywords
    ):
        campaigns = load_campaign_metrics()

        context["campaign_performance"] = (
            campaigns.to_dict(
                orient="records"
            )
        )

        matched = True

    # --------------------------------------------------
    # CUSTOMER SEGMENT / RFM QUESTIONS
    # --------------------------------------------------

    if any(
        keyword in question
        for keyword in segment_keywords
    ):
        segments = get_segment_summary()

        # Explicit definition so the LLM does not
        # rely on external knowledge when explaining RFM.
        context["rfm_definition"] = {
            "recency": (
                "How recently a customer made a purchase."
            ),
            "frequency": (
                "How often a customer made purchases."
            ),
            "monetary": (
                "How much value a customer generated "
                "through purchases."
            ),
        }

        context["customer_segments"] = (
            segments.to_dict(
                orient="records"
            )
        )

        matched = True

    # --------------------------------------------------
    # CONVERSION MODEL QUESTIONS
    # --------------------------------------------------

    if any(
        keyword in question
        for keyword in model_keywords
    ):
        model_metrics = load_model_metrics()

        context["model_performance"] = dict(
            zip(
                model_metrics["metric"],
                model_metrics["value"],
            )
        )

        # Additional trusted limitation for model questions
        context["model_limitation"] = (
            "The conversion target is highly imbalanced, "
            "so accuracy should not be interpreted alone."
        )

        matched = True

    # --------------------------------------------------
    # NOTHING RELEVANT FOUND
    # --------------------------------------------------

    if not matched:
        context["message"] = (
            "No relevant analytics context was found "
            "for this question."
        )

    return context


# --------------------------------------------------
# LOCAL TEST
# --------------------------------------------------

if __name__ == "__main__":

    test_questions = [
        "Which campaign has the highest ROAS?",
        "Which customer segment should receive a retention campaign?",
        "What is RFM?",
        "How well does the conversion model perform?",
        "What is the weather today?",
    ]

    for question in test_questions:

        print("\n-------------------------")
        print("Question:", question)

        context = retrieve_relevant_context(
            question
        )

        print("Retrieved sections:")
        print(list(context.keys()))