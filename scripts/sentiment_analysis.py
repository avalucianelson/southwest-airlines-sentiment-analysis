from textblob import TextBlob
import pandas as pd

# Load combined data
data = pd.read_csv("../data/combined_data.csv")

# Perform sentiment analysis
sentiment_mapping = {"Positive": 1, "Neutral": 0, "Negative": -1}

def analyze_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0:
        return 1  # Positive
    elif polarity < 0:
        return -1  # Negative
    else:
        return 0  # Neutral

data["Sentiment_Numeric"] = data["Text"].apply(analyze_sentiment)

# Save the results
data.to_csv("../data/sentiment_results.csv", index=False)
print("Sentiment analysis completed and saved to ../data/sentiment_results.csv")