import requests
import pandas as pd
import os
from datetime import date, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up NewsAPI credentials
api_key = os.getenv("NEWSAPI_KEY")

# Search queries
queries = [
    {"query": "Southwest Airlines assigned seating", "is_assigned_seating": 1},
    {"query": "Southwest Airlines", "is_assigned_seating": 0}
]

data = []
for search in queries:
    query = search["query"]
    is_assigned_seating = search["is_assigned_seating"]

    # Set date range
    today = date.today()
    last_month = today - timedelta(days=30)
    url = f"https://newsapi.org/v2/everything?q={query}&from={last_month}&to={today}&sortBy=relevance&apiKey={api_key}"

    # Fetch articles
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()["articles"]

        # Parse articles
        for article in articles:
            data.append({
                "Source": article["source"]["name"],
                "Title": article["title"],
                "Description": article["description"],
                "PublishedAt": article["publishedAt"],
                "URL": article["url"],
                "Is_Assigned_Seating": is_assigned_seating
            })
    else:
        print(f"Failed to fetch articles for query '{query}'. Status Code: {response.status_code}")

# Save to CSV
df_news = pd.DataFrame(data)
df_news.to_csv("../data/news_articles.csv", index=False)
print("News articles saved to ../data/news_articles.csv")