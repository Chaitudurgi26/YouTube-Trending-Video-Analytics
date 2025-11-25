import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from textblob import TextBlob

# ---------------------------
# Load Dataset
# ---------------------------
df = pd.read_csv("youtube_trend.csv")

print("Initial shape:", df.shape)

df.columns = [c.strip() for c in df.columns]

# ---------------------------
# Parse Dates
# ---------------------------
if "publishedAt" in df.columns:
    df["publishedAt"] = pd.to_datetime(df["publishedAt"], errors="coerce")

if "trending_date" in df.columns:
    def parse_td(x):
        x = str(x).strip()
        for fmt in ["%y.%d.%m", "%y-%m-%d", "%Y-%m-%d"]:
            try:
                return pd.to_datetime(x, format=fmt)
            except:
                pass
        try:
            return pd.to_datetime(x)
        except:
            return pd.NaT

    df["trending_date"] = df["trending_date"].apply(parse_td)

# Basic Cleaning
# ---------------------------
if "title" in df.columns:
    df = df[df["title"].notna() & (df["title"].astype(str).str.strip() != "")]

df = df.drop_duplicates()

num_cols = ["views", "likes", "dislikes", "comment_count"]
for col in num_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

df["country"] = df.get("country", "unknown")

# Compute Trending Duration
# ---------------------------
if "trending_date" in df.columns:
    td = (
        df.groupby(["video_id", "country"])["trending_date"]
        .nunique()
        .reset_index()
        .rename(columns={"trending_date": "trending_days"})
    )
    df = df.merge(td, on=["video_id", "country"], how="left")
else:
    df["trending_days"] = np.nan

# Sentiment Analysis
# ---------------------------
def get_sentiment(text):
    tb = TextBlob(str(text))
    return tb.sentiment.polarity, tb.sentiment.subjectivity

df["title_polarity"], df["title_subjectivity"] = zip(*df["title"].apply(get_sentiment))
df["title_sentiment"] = df["title_polarity"].apply(
    lambda x: "positive" if x > 0.05 else ("negative" if x < -0.05 else "neutral")
)

if "tags" in df.columns:
    df["tags_polarity"] = df["tags"].apply(lambda t: TextBlob(str(t)).sentiment.polarity)
    df["tags_sentiment"] = df["tags_polarity"].apply(
        lambda x: "positive" if x > 0.05 else ("negative" if x < -0.05 else "neutral")
    )

# Save Cleaned Data
# ---------------------------
df.to_csv("youtube_trend_cleaned.csv", index=False)
print("Saved cleaned dataset!")

# SQLite Database
# ---------------------------
conn = sqlite3.connect("youtube_trend.db")
df.to_sql("youtube", conn, if_exists="replace", index=False)

print("DB created: youtube_trend.db")

# EDA Plots
# ---------------------------
plt.figure(figsize=(10, 4))
df.groupby("category_id")["views"].mean().sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Top Categories by Avg Views")
plt.savefig("cat_avg_views.png")
plt.close()

plt.figure(figsize=(6, 6))
sample = df.dropna(subset=["views", "likes"]).head(200)
plt.scatter(sample["views"], sample["likes"], alpha=0.5)
plt.xscale("log")
plt.yscale("log")
plt.title("Views vs Likes")
plt.savefig("views_likes.png")
plt.close()

plt.figure(figsize=(6, 4))
df["title_sentiment"].value_counts().plot(kind="bar")
plt.title("Title Sentiment")
plt.savefig("sentiment_dist.png")
plt.close()

print("EDA plots saved!")

conn.close()
