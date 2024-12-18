import requests
import pandas as pd

# NewsAPI credentials
api_key = "738641510e34433fa3cc3e94246653e7"  # Replace with your NewsAPI key
query = "Southwest Airlines assigned seating"
from_date = "2024-11-18"  # Adjust this date as needed
url = f"https://newsapi.org/v2/everything?q={query}&from={from_date}&sortBy=relevance&apiKey={api_key}"

# Fetch articles from NewsAPI
response = requests.get(url)
if response.status_code == 200:
    articles = response.json()["articles"]

    # Parse articles into a list
    data = []
    for article in articles:
        data.append({
            "Source": article["source"]["name"],
            "Author": article["author"],
            "Title": article["title"],
            "Description": article["description"],
            "PublishedAt": article["publishedAt"],
            "URL": article["url"]
        })

    # Save articles to a DataFrame
    df_news = pd.DataFrame(data)

    # Save to CSV
    df_news.to_csv("../data/news_articles.csv", index=False)
    print("News articles saved to ../data/news_articles.csv")
else:
    print(f"Failed to fetch articles. Status Code: {response.status_code}")
    print("Response content:", response.content)