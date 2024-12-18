import pandas as pd
import matplotlib.pyplot as plt

# Load sentiment data
df_reddit = pd.read_csv("../data/reddit_southwest.csv")
df_youtube = pd.read_csv("../data/youtube_comments.csv")
df_news = pd.read_csv("../data/news_articles.csv")

# Combine data
all_data = pd.concat([df_reddit["Sentiment_Label"], df_youtube["Sentiment_Label"], df_news["Sentiment_Label"]])
sentiment_counts = all_data.value_counts()

# Plot sentiment distribution
sentiment_counts.plot(kind="bar", title="Sentiment Distribution Across Platforms", xlabel="Sentiment", ylabel="Count")
plt.savefig("../visualizations/sentiment_distribution.png")
plt.show()