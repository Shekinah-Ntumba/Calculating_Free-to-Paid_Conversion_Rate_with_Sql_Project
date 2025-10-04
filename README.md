# Calculating_Free-to-Paid_Conversion_Rate_with_Sql_Project
## SQL Interpretation

##  Project Overview

This project analyzes student behavior data to evaluate how users move from registration to engagement, and finally to paid conversion on an online learning platform.

Using SQL queries and data-driven metrics, the project measures key performance indicators (KPIs) such as:

Free-to-paid conversion rate

Registration-to-engagement time

Engagement-to-purchase duration

##  Purpose

The analysis helps to:

Identify strengths in user onboarding and content value

Highlight opportunities to improve conversion rates

Reduce decision-making time between engagement and purchase

Optimize overall user engagement through targeted business strategies


## **Interpretation of Your Corrected Metrics:**

### 1. **Free-to-Paid Conversion Rate: 11%** ✅
**Solid Industry Performance**
- **What this means**: 11% of students who watch lectures convert to paying customers
- **Industry Benchmark**: This is **good performance** (typical range: 2-15%)
- **Interpretation**:
  - Your content effectively demonstrates value to users
  - Healthy monetization of your free user base
  - Room for optimization but fundamentally sound

### 2. **Average Registration-to-Engagement: 3.5 days** ✅
**Good Onboarding Efficiency**
- **What this means**: Students typically start using the platform within 3-4 days of signing up
- **Interpretation**:
  - Reasonable activation timeline
  - Registration process is likely straightforward
  - Opportunity: Could optimize to 1-2 days for better retention

### 3. **Average Engagement-to-Purchase: 26.25 days** ⏳
**Extended Decision-Making Period**
- **What this means**: It takes nearly a month for students to convert after first engagement
- **Interpretation**:
  - Students are carefully evaluating the purchase decision
  - May indicate price sensitivity or need for more compelling offers
  - Significant opportunity to shorten this conversion window

## **Overall Business Assessment:**

**Strengths:**
- 📊 **Solid 11% conversion rate** - indicates good product-market fit
- 🚀 **Reasonable onboarding time** - 3.5 days is acceptable for activation
- 💡 **Clear value proposition** - students who engage see enough value to convert

**Key Opportunities:**
1. **Reduce the 26-day decision cycle** - this is your biggest leverage point
2. **Improve initial engagement speed** from 3.5 to 1-2 days
3. **Increase conversion rate** from 11% to 15-20% through better nurturing

**Actionable Recommendations:**
- **Create urgency**: Limited-time offers for engaged students
- **Improve onboarding**: Get students to first lecture faster
- **Nurturing campaigns**: Target students in the 7-21 day consideration window
- **A/B test pricing**: See if different price points accelerate decisions

## Python Report


# 🎓 Student Journey Data Analysis

## 📘 Project Overview

This project analyzes student behavior data to understand how learners progress from **registration** to **engagement** and finally to **purchase**.
Using Python, the analysis identifies behavioral patterns, measures conversion efficiency, and visualizes key engagement timelines to help improve onboarding and sales performance.

---

## 🧭 Objectives

* Measure how long it takes students to engage after registration.
* Calculate the average time from first engagement to purchase.
* Detect and analyze outliers that may distort performance metrics.
* Visualize engagement and conversion trends.
* Segment students into **quick** vs. **slow** engagers and converters.

---

## 🛠️ Tools and Libraries

| Library        | Purpose                            |
| -------------- | ---------------------------------- |
| **Pandas**     | Data cleaning and manipulation     |
| **NumPy**      | Numerical calculations             |
| **Matplotlib** | Data visualization                 |
| **Seaborn**    | Advanced visualization and styling |
| **SciPy**      | Statistical analysis               |

---

## 📂 Dataset

**Source:**
[student_journey_data.csv](https://raw.githubusercontent.com/Shekinah-Ntumba/Calculating_Free-to-Paid_Conversion_Rate_with_Sql_Project/refs/heads/main/student_journey_data.csv)

**Key Columns:**

* `days_diff_reg_watch` → Days between registration and first lecture watched
* `days_diff_watch_purch` → Days between first lecture watched and first purchase

These metrics help track activation speed and purchase decision time for each student.

---

## 📊 Analysis Performed

1. **Descriptive Statistics** – Mean, median, and mode for engagement and purchase timelines.
2. **Outlier Detection** – IQR method to identify unusual values.
3. **Visualization** – Histograms and box plots to show distributions and patterns.
4. **Behavior Segmentation** – Classifies students into:

   * Quick Engagers (≤1 day)
   * Slow Engagers (>7 days)
   * Quick Converters (≤7 days)
   * Slow Converters (>30 days)

---

## 🔍 Key Insights

* Most students engage within a few days after registering.
* Average time to purchase is around **3–4 weeks**, showing a long decision process.
* Some students convert almost immediately, while others take over a month.
* Outliers exist, indicating varied student behaviors or potential data anomalies.

---

## 💡 Recommendations

* **Accelerate engagement:** Encourage students to start learning within 1–2 days.
* **Shorten decision period:** Offer limited-time discounts or personalized reminders.
* **Investigate outliers:** Determine if delays are behavioral or data-related.
* **A/B test offers:** Experiment with pricing or content bundles to boost conversion rates.

---

## 📈 Visualization Output

The script generates:

* Histograms of registration-to-watch and watch-to-purchase timelines
* Box plots for quick outlier detection
* Summary statistics displayed in the console

Example plots include:

* *Distribution: Registration to First Watch*
* *Distribution: First Watch to Purchase*

---

## 🧩 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/Shekinah-Ntumba/Calculating_Free-to-Paid_Conversion_Rate_with_Sql_Project.git
   ```
2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```
3. Run the script:

   ```bash
   python student_journey_analysis.py
   ```

---

## 🏁 Conclusion

This analysis provides actionable insights into how students engage and convert on a learning platform.
By improving onboarding speed and shortening purchase timelines, educational platforms can significantly enhance **user retention** and **revenue performance**.

---

Would you like me to include a small **“Results Summary Table”** section (e.g., average days, conversion percentages, etc.) for better presentation on GitHub?

