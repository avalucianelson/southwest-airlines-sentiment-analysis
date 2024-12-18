import os
from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up YouTube API
api_key = os.getenv("YOUTUBE_API_KEY")  # My API key
youtube = build("youtube", "v3", developerKey=api_key)

# Search for videos
request = youtube.search().list(q="Southwest Airlines assigned seating", part="snippet", maxResults=5)
response = request.execute()

# Fetch comments for each video
comments = []
for video in response["items"]:
    video_id = video["id"]["videoId"]
    comment_request = youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=50)
    comment_response = comment_request.execute()

    for item in comment_response["items"]:
        comments.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"])

# Save to DataFrame
df_youtube = pd.DataFrame(comments, columns=["Comment"])
df_youtube.to_csv("../data/youtube_comments.csv", index=False)
print("YouTube comments saved to data/youtube_comments.csv")