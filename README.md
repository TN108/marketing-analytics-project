\# Marketing Analytics Project



\## Project objective



This project builds a synthetic marketing dataset for campaign analysis, KPI reporting, and future machine-learning experiments using Databricks, PySpark, Delta Lake, and SQL.



\## Dataset grain



Each row represents one customer's interaction with one product through one marketing campaign on one date.



\## Dataset contents



The dataset includes:



\- customer demographics

\- product information

\- marketing campaigns

\- advertisement impressions

\- clicks and website visits

\- orders and units sold

\- advertising spend

\- revenue



\## Marketing funnel



The dataset follows this customer journey:



Impressions → Clicks → Website visits → Orders → Units sold



\## Main KPIs



\- Click-through rate

\- Click-to-visit rate

\- Conversion rate

\- Return on ad spend

\- Average order value

\- Cost per order



\## Technologies



\- Python

\- PySpark

\- Databricks

\- Delta Lake

\- SQL



\## Current progress



Day 1 completed:



\- designed the dataset schema

\- generated 10,000 unique interactions

\- implemented campaign-specific behaviour

\- validated missing values, duplicates, funnel rules, and revenue

\- saved the dataset as a Delta table

\- calculated overall and campaign-level KPIs



\## Notebook



The Day 1 notebook is available at:



`notebooks/01\_generate\_synthetic\_data.ipynb`

