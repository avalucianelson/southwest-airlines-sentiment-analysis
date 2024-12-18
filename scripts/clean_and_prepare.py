import pandas as pd

# Load datasets
reddit_data = pd.read_csv("../data/reddit_southwest.csv")
youtube_data = pd.read_csv("../data/youtube_comments.csv")
news_data = pd.read_csv("../data/news_articles.csv")

# Clean Reddit data
reddit_data = reddit_data[["Date", "Full_Text"]].rename(columns={"Full_Text": "Text"})
reddit_data["Platform"] = "Reddit"

# Clean YouTube data
youtube_data = youtube_data.rename(columns={"Comment": "Text"})
youtube_data["Platform"] = "YouTube"

# Clean NewsAPI data
news_data["Text"] = news_data["Title"] + " " + news_data["Description"]
news_data = news_data[["PublishedAt", "Text"]].rename(columns={"PublishedAt": "Date"})
news_data["Platform"] = "News"

# Combine all datasets
all_data = pd.concat([reddit_data, youtube_data, news_data], ignore_index=True)

# Save cleaned data
all_data.to_csv("../data/combined_data.csv", index=False)
print("Combined dataset saved to ../data/combined_data.csv")