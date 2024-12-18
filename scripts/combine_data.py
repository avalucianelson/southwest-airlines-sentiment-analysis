import pandas as pd

# Load datasets
reddit_data = pd.read_csv("../data/reddit_southwest.csv")
youtube_data = pd.read_csv("../data/youtube_comments.csv")
news_data = pd.read_csv("../data/news_articles.csv")

# Standardize column names
reddit_data = reddit_data[["Date", "Full_Text", "Is_Assigned_Seating"]].rename(columns={"Full_Text": "Text"})
youtube_data = youtube_data.rename(columns={"Comment": "Text"})
news_data = news_data.rename(columns={"Title": "Text"})

# Combine all datasets
all_data = pd.concat([reddit_data, youtube_data, news_data], ignore_index=True)

# Save combined data
all_data.to_csv("../data/combined_data.csv", index=False)
print("Combined dataset saved to ../data/combined_data.csv")