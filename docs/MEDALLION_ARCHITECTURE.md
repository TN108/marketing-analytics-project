# Marketing Analytics Medallion Architecture

## Architecture

Raw → Bronze → Silver → Gold → Power BI

## Raw Layer

Table: `marketing_interactions_raw`

Contains 10,000 rows of original synthetic marketing interaction data.

## Bronze Layer

Table: `bronze_marketing_interactions`

Preserves the raw data and adds ingestion metadata:

- `ingestion_timestamp`
- `source_name`
- `load_date`

Validation:

- Raw rows: 10,000
- Bronze rows: 10,000
- Missing metadata values: 0
- Distinct sources: 1

## Silver Layer

Table: `silver_marketing_interactions`

Contains cleaned, validated, and analysis-ready data.

Processing includes:

- Duplicate removal
- Missing-value handling
- Data-type validation
- Marketing funnel validation
- Revenue validation
- Standardized text values
- Derived date columns
- Conversion label
- Discounted unit price

Derived columns:

- `year`
- `month`
- `quarter`
- `converted`
- `discounted_unit_price`

Validation results:

- Rows: 10,000
- Exact duplicates: 0
- Campaigns: 4
- Customers: 999
- Products: 5
- Orders: 169
- Units sold: 336
- Revenue: 3,827,575
- Invalid validation rows: 0

## Gold Layer

Business-level aggregate tables:

- `gold_campaign_metrics`
- `gold_customer_metrics`
- `gold_product_metrics`
- `gold_dashboard_metrics`

Gold totals match the Silver layer:

- Interactions: 10,000
- Orders: 169
- Units sold: 336
- Revenue: 3,827,575
- Ad spend: 664,311.88

KPI validation found:

- Incorrect CTR rows: 0
- Incorrect conversion-rate rows: 0
- Incorrect ROAS rows: 0

## Power BI

Dashboard:

`Marketing Analytics Executive Dashboard`

Dashboard components:

- Total Revenue
- Total Orders
- ROAS
- Conversion Rate
- Revenue by Campaign
- Revenue by Product Category
- Monthly Revenue Trend
- Campaign Performance table
- Region filter
- Device filter