import praw
import pandas as pd
from datetime import datetime

# Set up Reddit API credentials
reddit = praw.Reddit(
    client_id="Ep6yr32IFAXpOMGy9JyYpA",  # Your client ID
    client_secret="jmzsKw7p7iqO0R2Z8OHafqwq3m9RUQ",  # Your secret ID
    user_agent="southwest-analysis-script"  # Choose a descriptive user agent
)

# Define subreddit and search term
subreddit = reddit.subreddit("travel")  # Target subreddit
query = "Southwest Airlines assigned seating"  # Search query

# Fetch posts
posts = subreddit.search(query, limit=100)

# Collect posts in a list
data = []
for post in posts:
    data.append({
        "Date": datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
        "Title": post.title,
        "Text": post.selftext,
        "Score": post.score,
        "Comments": post.num_comments,
        "Link": f"https://www.reddit.com{post.permalink}"
    })

# Convert the list to a DataFrame
df_reddit = pd.DataFrame(data)

# Combine Title and Text into one field
df_reddit["Full_Text"] = df_reddit["Title"] + " " + df_reddit["Text"]

# Save to CSV
df_reddit.to_csv("../data/reddit_southwest.csv", index=False)
print("Reddit data saved to ../data/reddit_southwest.csv")