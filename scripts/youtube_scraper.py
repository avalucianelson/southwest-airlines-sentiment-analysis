import os
from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up YouTube API
api_key = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=api_key)

# Search queries
queries = [
    {"query": "Southwest Airlines assigned seating", "is_assigned_seating": 1},
    {"query": "Southwest Airlines", "is_assigned_seating": 0}
]

data = []
for search in queries:
    query = search["query"]
    is_assigned_seating = search["is_assigned_seating"]

    # Search for videos
    request = youtube.search().list(q=query, part="snippet", maxResults=5)
    response = request.execute()

    # Fetch comments for each video
    for video in response["items"]:
        if "videoId" in video["id"]:  # Check if 'videoId' exists
            video_id = video["id"]["videoId"]
            comment_request = youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=50)
            comment_response = comment_request.execute()

            for item in comment_response["items"]:
                data.append({
                    "Comment": item["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
                    "Is_Assigned_Seating": is_assigned_seating
                })

# Save to DataFrame
df_youtube = pd.DataFrame(data)
df_youtube.to_csv("../data/youtube_comments.csv", index=False)
print("YouTube comments saved to ../data/youtube_comments.csv")