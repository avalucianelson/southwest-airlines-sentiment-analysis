import os
import praw
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),  # Your client ID
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),  # Your secret ID
    user_agent="southwest-analysis-script"  # Choose a descriptive user agent
)

# Search queries
queries = [
    {"query": "Southwest Airlines assigned seating", "is_assigned_seating": 1},
    {"query": "Southwest Airlines", "is_assigned_seating": 0}
]

data = []
for search in queries:
    query = search["query"]
    is_assigned_seating = search["is_assigned_seating"]
    subreddit = reddit.subreddit("all")  # Search across all subreddits
    posts = subreddit.search(query, limit=100)

    # Collect posts
    for post in posts:
        data.append({
            "Date": datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
            "Title": post.title,
            "Text": post.selftext,
            "Score": post.score,
            "Comments": post.num_comments,
            "Link": f"https://www.reddit.com{post.permalink}",
            "Is_Assigned_Seating": is_assigned_seating
        })

# Convert the list to a DataFrame
df_reddit = pd.DataFrame(data)

# Combine Title and Text into one field
df_reddit["Full_Text"] = df_reddit["Title"] + " " + df_reddit["Text"]

# Ensure the data directory exists
output_dir = "../data"
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Save to CSV
df_reddit.to_csv(os.path.join(output_dir, "reddit_southwest.csv"), index=False)
print("Reddit data saved to ../data/reddit_southwest.csv")