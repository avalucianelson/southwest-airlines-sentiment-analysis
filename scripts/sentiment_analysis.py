from textblob import TextBlob
import pandas as pd

# Load combined data
data = pd.read_csv("../data/combined_data.csv")

# Perform sentiment analysis
data["Sentiment"] = data["Text"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
data["Sentiment_Label"] = data["Sentiment"].apply(lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral"))

# Save results
data.to_csv("../data/sentiment_results.csv", index=False)
print("Sentiment analysis completed. Results saved to ../data/sentiment_results.csv")
