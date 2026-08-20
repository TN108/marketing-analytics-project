\# Data Dictionary



\## Row grain



Each row represents one customer's interaction with one product through one marketing campaign on one date.



| Column | Type | Description |

|---|---|---|

| interaction\_date | Date | Date of the interaction |

| customer\_id | String | Unique customer identifier |

| customer\_age | Integer | Customer age |

| customer\_gender | String | Customer gender category |

| customer\_region | String | Customer region |

| product\_id | String | Unique product identifier |

| product\_category | String | Product category |

| unit\_price | Double | Original price of one product unit |

| campaign\_id | String | Unique campaign identifier |

| marketing\_channel | String | Marketing channel used by the campaign |

| device\_type | String | Device used by the customer |

| discount\_percent | Double | Discount applied as a percentage |

| impressions | Integer | Number of times the advertisement was displayed |

| clicks | Integer | Whether the customer clicked the advertisement |

| website\_visits | Integer | Whether the click became a website visit |

| orders | Integer | Whether the customer placed an order |

| units\_sold | Integer | Number of product units purchased |

| ad\_spend | Double | Advertising cost allocated to the interaction |

| revenue | Double | Revenue after discount |



\## Unique interaction key



The following combination must be unique:



`interaction\_date + customer\_id + product\_id + campaign\_id`



\## Funnel rules



\- `clicks <= impressions`

\- `website\_visits <= clicks`

\- `orders <= website\_visits`

\- `units\_sold >= orders`



\## Revenue rule



`revenue = units\_sold × unit\_price × (1 - discount\_percent / 100)`

