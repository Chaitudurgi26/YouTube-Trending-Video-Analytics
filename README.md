
# 📊 YouTube Trending Video Analysis

A complete end-to-end data analysis project using **Python, SQL, Sentiment Analysis, and Exploratory Data Analysis (EDA)** to understand what makes YouTube videos trend.

---

## 📁 Project Overview

This project performs:

* Data loading & cleaning
* Date parsing
* Sentiment analysis on titles & tags
* Trending duration calculation
* Engagement metric calculations
* SQL-based analytical insights
* Visual EDA charts
* Clean dataset & SQLite DB export

---

## 🛠️ Tech Stack

| Component | Technology                          |
| --------- | ----------------------------------- |
| Language  | Python 3                            |
| Database  | SQLite                              |
| Libraries | Pandas, NumPy, Matplotlib, TextBlob |
| Output    | CSV, PNG charts, SQL DB             |

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install pandas numpy matplotlib textblob
python -m textblob.download_corpora
```

### 2. Run script

```bash
python youtube_analysis.py
```

This will generate:

* Cleaned CSV
* SQLite database
* Three visual charts

---

## 🧹 Data Cleaning Steps

* Standardized column names
* Converted dates (published & trending)
* Removed duplicates
* Cleaned missing values
* Converted numeric columns
* Added **sentiment polarity & subjectivity**
* Added **trending_days** feature

---

## 🧪 SQL Analytical Questions (in `queries.sql`)

1. Rank categories by average views
2. Top 10 channels with most trending videos
3. Likes-to-views ratio per category
4. Videos with maximum trending duration
5. Extreme engagement cases (high like/comment ratios)

---

## 📊 Visual Outputs (EDA)

Generated PNGs include:

* **Category-wise Average Views**
* **Views vs Likes (log scale)**
* **Sentiment Distribution of Titles**

---

## 📘 Future Enhancements

* Tableau/PowerBI dashboard
* Advanced NLP keyword analysis
* Predictive “trend probability” model
* Streamlit web dashboard



## ✨ Author

**Krishna Chaitanya**
Data Analyst | Python Developer
