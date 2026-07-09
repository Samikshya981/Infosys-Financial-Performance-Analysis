# Infosys Financial Performance & Cost Efficiency Analysis (FY23 - FY26)

## 📌 1. Project Overview (What is this project about?)
When a large company grows and makes more money, it often starts wasting money on unnecessary office costs, extra hiring, or overhead bills. This is called "operational bloat." 

This project answers one central question: **As Infosys grew its revenue over the last 4 years, did it manage its expenses smartly to protect its profit margins, or did it get sloppy?**

To find the answer, I built a complete data pipeline that pulls live stock data, cleans it, calculates key financial health checks, and presents them on a professional interactive dashboard.

---

## 🛠️ 2. The Data Pipeline (How I built it)
Instead of just downloading a static, pre-cleaned Excel file from Kaggle like most beginners do, I built an automated pipeline from scratch:

1. **Extraction (Python + API):** I wrote a Python script using the `yfinance` library to call an API (an automated internet waiter) to fetch raw, live corporate filings directly from Yahoo Finance.
2. **Data Cleaning (Pandas):** The raw internet data was messy and horizontal. I used the `pandas` library to flip the data into clean vertical rows, filter out columns I didn't need, and handle a hidden bug where the year 2022 was completely empty (Null).
3. **Data Modeling (Power BI + DAX):** I imported the clean dataset into Power BI. Instead of doing math manually, I wrote **DAX formulas** (dynamic math functions) to calculate critical financial percentages automatically on the screen.

---

## 📈 3. The Core Formulas Used (DAX)
To keep the dashboard dynamic, I engineered these three primary calculations:

*   **Gross Margin %** (Production Efficiency):
    ```dax
    Gross Margin % = DIVIDE(SUM('infosys_powerbi_master'[Gross Profit]), SUM('infosys_powerbi_master'[Total Revenue]), 0) * 100
    ```
*   **Net Profit Margin %** (Pure Profitability):
    ```dax
    Net Profit Margin % = DIVIDE(SUM('infosys_powerbi_master'[Net Income]), SUM('infosys_powerbi_master'[Total Revenue]), 0) * 100
    ```
*   **Current Ratio** (Short-term Bill Paying Cushion):
    ```dax
    Current Ratio = DIVIDE(SUM('infosys_powerbi_master'[Current Assets]), SUM('infosys_powerbi_master'[Current Liabilities]), 0)
    ```
*   **Latest Revenue Growth** (Single Target KPI Card):
    Calculates the exact growth performance of the most recent fiscal year compared to the prior period by dynamically locating the maximum calendar year.
    ```dax
    Latest Revenue Growth = 
    VAR LatestYear = MAXX(ALLSELECTED('infosys_powerbi_master'), 'infosys_powerbi_master'[Year])
    VAR CurrentRevenue = CALCULATE(SUM('infosys_powerbi_master'[Total Revenue]), 'infosys_powerbi_master'[Year] = LatestYear)
    VAR PreviousRevenue = CALCULATE(SUM('infosys_powerbi_master'[Total Revenue]), FILTER(ALL('infosys_powerbi_master'[Year]), 'infosys_powerbi_master'[Year] = LatestYear - 1))
    RETURN
    DIVIDE(CurrentRevenue - PreviousRevenue, PreviousRevenue)
    ```

*   **Year-over-Year Revenue Growth %** (Time-Intelligence Trend Loop):
    Calculates a rolling year-over-year growth trajectory by dynamically shifting the evaluation context back by 12 months for each row.
    ```dax
    Previous Year Revenue = 
    VAR CurrentYear = MAX('infosys_powerbi_master'[Year])
    RETURN
    CALCULATE(SUM('infosys_powerbi_master'[Total Revenue]), FILTER(ALL('infosys_powerbi_master'[Year]), 'infosys_powerbi_master'[Year] = CurrentYear - 1))

    Revenue Growth % = 
    VAR CurrentRevenue = SUM('infosys_powerbi_master'[Total Revenue])
    VAR PreviousRevenue = [Previous Year Revenue]
    RETURN
    DIVIDE(CurrentRevenue - PreviousRevenue, PreviousRevenue)
    ```
---

## 📊 4. Dashboard View

![Final Dashboard Preview](/financial%20analysis.jpg)

---

## 🔍 5. Real Business Insights (The Story the Data Tells)

After building the charts and looking at the numbers, here are the 3 major discoveries I made about Infosys:

### 1. Elite Cost Control (Parallel Margins)
Infosys's total revenue grew steadily from 18.2bn to 20.2bn (an 11% jump). Usually, rapid growth makes a company inefficient. However, the charts show that the Gross Margin held tightly between **30.10% and 30.46%**, while the Net Profit Margin remained steady between **16.37% and 17.06%** over all 4 years. Because these lines run perfectly flat and parallel, it proves management exercised extreme discipline—every time they made a new dollar, their costs did not shoot up unexpectedly.

### 2. Massive Cash Cushion (Liquidity Safety)
In business, a company is considered safe if its **Current Ratio** is between 1.5 and 2.0 (meaning it has enough short-term cash to cover its short-term bills). Infosys tracked between **1.81 and 2.31**. This proves they have a huge cash buffer and are at zero risk of running out of money to pay daily bills.

### 3. Bulletproof Capital Structure (Low Debt Risk)
Looking at the Debt vs. Equity chart, the bank loan slice is practically invisible (a tiny ratio of **0.10**). This tells us that Infosys does not rely on risky bank loans or corporate debt to stay alive. They fund their entire operation out of their own cash savings and shareholder investments, making them financially indestructible.

---

## 🚀 6. Key Technical Skills Demonstrated
*   **Backend Automation:** Python, `yfinance` API integration, and `pandas` data reshaping.
*   **Data Quality Assurance:** Identifying and filtering out incomplete/null calendar data arrays.
*   **Business Intelligence & UI Design:** Dynamic DAX programming and professional dark-mode dashboard design principles in Power BI.
