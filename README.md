<div align="center">

# 📊 Marketing Analytics AI Copilot

**An end-to-end marketing analytics MVP — from raw data to a secure, grounded AI Copilot.**

Data Engineering • SQL Analytics • Power BI • Machine Learning • Customer Segmentation • Secure GenAI • Streamlit

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Databricks](https://img.shields.io/badge/Databricks-Medallion-FF3621?logo=databricks&logoColor=white)](https://www.databricks.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Reporting-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Groq](https://img.shields.io/badge/Groq-LLM%20Inference-black?logo=groq&logoColor=white)](https://groq.com/)
[![Eval Score](https://img.shields.io/badge/Eval%20Score-100%25%20(25%2F25)-2ea44f)](#-evaluation)
[![License](https://img.shields.io/badge/License-MIT-informational)](#)
[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://marketing-analytics-ai-copilot.streamlit.app/)

**🔗 [Try the live app →](https://marketing-analytics-ai-copilot.streamlit.app/)**

</div>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Architecture](#-architecture)
- [Medallion Data Architecture](#-medallion-data-architecture)
- [Campaign Performance](#-campaign-performance)
- [Conversion Prediction](#-conversion-prediction)
- [Customer Segmentation](#-customer-segmentation)
- [AI Marketing Copilot](#-ai-marketing-copilot)
- [Security](#-security)
- [Evaluation](#-evaluation)
- [Streamlit Application](#-streamlit-application)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Environment Variables](#-environment-variables)
- [Running the Project](#-running-the-project)
- [Power BI](#-power-bi)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Technology Stack](#-technology-stack)
- [Final Result](#-final-result)
- [Deployment](#-deployment)

---

## 🧭 Project Overview

This project demonstrates a **complete marketing analytics workflow** — from raw synthetic interaction data to business recommendations delivered through an AI-powered Streamlit application.

<table>
<tr>
<td width="50%" valign="top">

**🏗️ Data & Infrastructure**
- Databricks Medallion Architecture
- SQL analytics
- Power BI executive reporting

**🤖 Machine Learning**
- Logistic Regression for conversion prediction
- RFM + K-Means customer segmentation

</td>
<td width="50%" valign="top">

**🔒 Generative AI & Security**
- Structured RAG
- Groq-hosted LLM inference
- Prompt-injection protection
- Data-leakage controls
- Automated RAG and security evaluation

**🖥️ Delivery**
- Interactive Streamlit deployment

</td>
</tr>
</table>

---

## ❓ Business Problem

Marketing teams need to answer questions such as:

| # | Question |
|---|---|
| 1 | Which campaign produces the highest ROAS? |
| 2 | Which campaign generates the most orders? |
| 3 | Which customer segment should receive a retention campaign? |
| 4 | How well does the conversion model perform? |
| 5 | Why is accuracy misleading for an imbalanced conversion problem? |
| 6 | Where should marketing attention be focused? |

> This project converts raw marketing interactions into **trusted analytical outputs**, exposed through dashboards and a grounded AI Copilot.

---

## 🏛️ Architecture

```text
                      Synthetic Marketing Data
                                ↓
                              Raw
                                ↓
                            Bronze
                                ↓
                            Silver
                                ↓
                             Gold
                                ↓
         ┌──────────────────────┼──────────────────────┐
         ↓                      ↓                      ↓
      Power BI            Conversion              RFM + K-Means
                           Prediction               Segmentation
         └──────────────────────┴──────────────────────┘
                                ↓
                  Structured Analytics Context
                                ↓
                  Relevant Context Retrieval
                                ↓
                       Security Layer
                                ↓
                         Groq LLM
                                ↓
                   AI Marketing Copilot
                                ↓
                  Streamlit Application
```

---

## 🥉🥈🥇 Medallion Data Architecture

The data engineering workflow follows the Medallion Architecture:

<div align="center">

**`Raw`  →  `Bronze`  →  `Silver`  →  `Gold`**

</div>

| Layer | Description |
|---|---|
| 🟤 **Raw** | Original synthetic marketing interaction data |
| 🥉 **Bronze** | Adds ingestion metadata while preserving source records |
| 🥈 **Silver** | Cleans and transforms data into analysis-ready form — date features, conversion indicators, discounted prices, standardized campaign/customer attributes |
| 🥇 **Gold** | Business-ready analytical tables used by Power BI and the AI application — campaign metrics, customer metrics, product metrics, conversion-model results, segmentation results |

---

## 📈 Campaign Performance

| Campaign | Channel | Orders | Revenue | Ad Spend | ROAS |
|---|---|---:|---:|---:|---:|
| CMP001 | 📧 Email | 50 | 1,287,175 | 139,907.97 | **9.20** 🏆 |
| CMP002 | 📱 Social Media | 36 | 723,275 | 180,748.81 | 4.00 |
| CMP003 | 🔍 Search | **74** 🏆 | 1,533,500 | 247,788.11 | 6.19 |
| CMP004 | 🖼️ Display | 9 | 283,625 | 95,866.99 | 2.96 ⚠️ |

**Key findings**
- ✅ Email has the highest ROAS
- ✅ Search generates the most orders
- ⚠️ Display has the lowest ROAS

### 🎯 Executive KPIs

| Metric | Value |
|---|---:|
| Total Revenue | **$3,827,575** |
| Total Orders | **169** |
| Total Ad Spend | **$664,311.88** |
| Overall ROAS | **≈ 5.76** |

---

## 🔮 Conversion Prediction

A **Logistic Regression** model was used to predict customer conversion.

| Metric | Value |
|---|---:|
| Accuracy | 0.9740 |
| Precision | 0.1786 |
| Recall | 0.1471 |
| F1 Score | 0.1613 |
| ROC-AUC | 0.7374 |
| PR-AUC | 0.0727 |
| Threshold | 0.05 |
| True Positives | 5 |
| False Positives | 23 |
| False Negatives | 29 |
| True Negatives | 1,943 |

> ⚠️ **The conversion target is highly imbalanced.** Accuracy alone is misleading — the model should be treated as **decision support**, not an automatic customer-targeting system.

---

## 🧩 Customer Segmentation

RFM features were used with **K-Means clustering**.

| Signal | Meaning |
|---|---|
| 🕒 **Recency** | How recently a customer purchased |
| 🔁 **Frequency** | How often a customer purchased |
| 💰 **Monetary** | How much value the customer generated |

The selected clustering solution uses **four customer segments**:

| Segment | Customers | Avg Recency | Avg Frequency | Avg Monetary |
|---|---:|---:|---:|---:|
| 🔴 At-Risk Customers | 51 | 287.22 | 1.00 | 10,862.75 |
| 🟣 High-Value One-Time Customers | 28 | 138.93 | 1.00 | 85,982.14 |
| 🟢 Loyal Customers | 13 | 149.54 | 2.08 | 38,057.69 |
| 🔵 Recent Low-Value Customers | 63 | 110.19 | 1.00 | 5,894.05 |

**Recommended actions**

| Segment | Recommendation |
|---|---|
| 🔴 At-Risk Customers | Re-engagement discounts, reminders, win-back offers |
| 🟣 High-Value One-Time Customers | VIP offers, second-purchase incentives |
| 🟢 Loyal Customers | Loyalty rewards, referral campaigns |
| 🔵 Recent Low-Value Customers | Welcome offers, low-cost automated campaigns |

---

## 🤖 AI Marketing Copilot

The project uses a **structured RAG architecture**. Instead of embedding the full 10,000-row dataset, the Copilot retrieves only compact, trusted analytics relevant to each question.

```text
                    User Question
                          ↓
                   Input Validation
                          ↓
               Secret Request Detection
                          ↓
             Regex Prompt-Injection Detection
                          ↓
                  Groq Prompt Guard
                          ↓
              Relevant Context Retrieval
                          ↓
              Sensitive-Data Filtering
                          ↓
        Deterministic Metric Lookup  /  LLM
                          ↓
              Output Leakage Validation
                          ↓
                    Final Answer
```

**Models used**

| Purpose | Model |
|---|---|
| Main generation | `qwen/qwen3.8-27b` (via Groq API) |
| Prompt-injection detection | `meta-llama/llama-prompt-guard-2-22m` |

### 💡 Why Structured RAG?

Traditional vector RAG was unnecessary — the project primarily uses **structured analytics** rather than large collections of unstructured documents.

| Question type | Retrieved context |
|---|---|
| ROAS question | Campaign metrics |
| Retention question | Customer segment summary |
| Model question | Conversion metrics |

This reduces: **token usage** · **latency** · **data exposure** · **hallucination risk**

---

## 🔐 Security

The Copilot implements several layered defenses:

| Layer | What it does |
|---|---|
| ✅ **Input Validation** | Rejects empty or invalid user input |
| 🚫 **Secret Request Detection** | Blocks requests for API keys, environment variables, `.env` contents, credentials, access tokens |
| 🛡️ **Prompt Injection Detection** | Local regex rules catch obvious attacks (e.g. *"Ignore previous instructions..."*) |
| 🧠 **Groq Prompt Guard** | Dedicated security model adds a second detection layer |
| 🔗 **Indirect Prompt Injection Protection** | Retrieved analytics are treated as **data**, never as instructions |
| 🕵️ **Sensitive Data Filtering** | Customer-level identifiers are stripped; 155 customer records are aggregated into 4 segment summaries before reaching the LLM |
| 🚧 **Output Leakage Validation** | Responses are scanned and blocked if they contain API keys, internal prompts, or environment info |

---

## ✅ Evaluation

The Copilot was tested against a **25-question evaluation suite** covering correctness, RAG retrieval, out-of-scope handling, prompt injection, secret extraction, security false positives, grounded metric retrieval, and latency.

| Evaluation Category | Result |
|---|---:|
| Correctness | 10 / 10 |
| Out-of-Scope Handling | 3 / 3 |
| Security | 9 / 9 |
| Security False Positives | 3 / 3 |
| **Overall** | **25 / 25** ✅ |

<div align="center">

### 🏆 Overall Score: 100%

| Average Latency | Slowest Response |
|:---:|:---:|
| 0.55 s | 1.35 s |

</div>

> No evaluation cases failed in the final test suite.

---

## 🖥️ Streamlit Application

🔗 **Live app:** [marketing-analytics-ai-copilot.streamlit.app](https://marketing-analytics-ai-copilot.streamlit.app/)

The Streamlit application contains:

- 📊 Executive KPI overview
- 📈 Campaign-performance analysis
- 🧩 Customer segmentation
- 🔮 Conversion-model results
- 🤖 Secure AI Marketing Copilot

```bash
python -m streamlit run app/streamlit_app.py
```

---

## 📂 Project Structure

```text
marketing-analytics-project/
│
├── app/
│   ├── analytics_context.py
│   ├── copilot.py
│   ├── security.py
│   ├── evaluate.py
│   ├── eval_dataset.py
│   ├── run_full_eval.py
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── campaign_metrics.csv
│       ├── customer_segments.csv
│       └── conversion_model_metrics.csv
│
├── docs/
│   ├── GENAI_COPILOT.md
│   ├── ARCHITECTURE.md
│   └── MEDALLION_ARCHITECTURE.md
│
├── notebooks/
├── powerbi/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone <repository-url>
cd marketing-analytics-project

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate it (Windows)
.\.venv\Scripts\Activate.ps1

# 4. Install dependencies
python -m pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

> ⚠️ **Never commit `.env` to version control.**

---

## 🔑 Environment Variables

**`.env.example`**
```env
GROQ_API_KEY=your_groq_api_key_here
```

**`.gitignore`**
```gitignore
.env
*.env
!.env.example
.venv/
.streamlit/secrets.toml
__pycache__/
*.pyc
```

---

## ▶️ Running the Project

| Task | Command |
|---|---|
| Run the evaluation suite | `python app/run_full_eval.py` |
| Launch the Streamlit app | `python -m streamlit run app/streamlit_app.py` |

---

## 📊 Power BI

Power BI is used as the **executive visualization layer**. The AI Copilot does **not** scrape Power BI charts — both Power BI and the Copilot read from the same prepared **Gold** analytics outputs as the single source of truth.

---

## ⚠️ Limitations

- The marketing dataset is synthetic
- Business recommendations have not been validated in a real production campaign
- Conversion events are highly imbalanced
- The AI system is restricted to the supplied analytics context
- Prompt-injection protection reduces risk but does not guarantee complete security against every future attack
- Current deployment relies on external Groq API availability and rate limits

---

## 🚀 Future Improvements

- [ ] Direct Databricks SQL integration
- [ ] Power BI semantic-model integration
- [ ] Authentication and user roles
- [ ] Persistent Copilot chat history
- [ ] Automated monitoring and evaluation
- [ ] More comprehensive adversarial security tests
- [ ] Real marketing datasets
- [ ] Experiment tracking
- [ ] Production model monitoring
- [ ] Tool calling for verified analytical calculations

---

## 🛠️ Technology Stack

<div align="center">

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![PySpark](https://img.shields.io/badge/-PySpark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/-Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)
![SQL](https://img.shields.io/badge/-SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/-Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/-Groq-black?style=flat-square&logo=groq&logoColor=white)
![Git](https://img.shields.io/badge/-Git%2FGitHub-181717?style=flat-square&logo=github&logoColor=white)

</div>

- Python · Pandas · PySpark · Databricks · SQL
- Power BI · Scikit-learn · K-Means
- Streamlit · Groq · Qwen · Llama Prompt Guard
- Git / GitHub

---

## 🏁 Final Result

```text
Data Engineering
      ↓
   Analytics
      ↓
Business Intelligence
      ↓
Machine Learning
      ↓
Customer Segmentation
      ↓
Secure Generative AI
      ↓
Interactive Streamlit MVP
```

> The result is a **grounded, security-aware AI Marketing Copilot** built on trusted analytical outputs.

---

## ☁️ Deployment

The simplest deployment option is **Streamlit Community Cloud**.

### 1. Push your code to GitHub

Before pushing, confirm `.env` is **not** tracked:

```bash
git status --short --untracked-files=all
```

Then commit and push as usual.

### 2. Connect the repository

Go to **Streamlit Community Cloud** → connect your GitHub repository → set the entrypoint to:

```
app/streamlit_app.py
```

### 3. Add secrets

Since `.env` must never be deployed, add the real Groq key under **Streamlit App Secrets**:

```toml
GROQ_API_KEY = "your_real_key"
```

### 4. Make the key loader environment-aware

Your current `copilot.py` loads:

```python
os.getenv("GROQ_API_KEY")
```

Update it to support **both** local `.env` and deployed Streamlit secrets:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

if not api_key:
    raise ValueError("GROQ_API_KEY is missing.")
```

| Environment | Source |
|---|---|
| 💻 Local | `.env` → `GROQ_API_KEY` |
| ☁️ Deployed | Streamlit Secrets → `GROQ_API_KEY` |

### 5. Confirm `requirements.txt`

```
streamlit
pandas
python-dotenv
groq
```

### 6. Deployment flow

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Repository: marketing-analytics-project
       ↓
Main file: app/streamlit_app.py
       ↓
Advanced Settings → Secrets
       ↓
GROQ_API_KEY = "..."
       ↓
🚀 Deploy
```

---

<div align="center">

Made with 📊 data, 🤖 machine learning, and a healthy respect for prompt injection.

</div>
