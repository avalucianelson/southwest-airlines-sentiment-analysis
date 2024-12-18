import pandas as pd

# Load sentiment results
data = pd.read_csv("../data/sentiment_results.csv")

# Summarize sentiment by platform
sentiment_summary = data.groupby(["Platform", "Sentiment_Label"]).size().unstack(fill_value=0)

# Save summary to CSV
sentiment_summary.to_csv("../data/sentiment_summary.csv")
print("Sentiment summary saved to ../data/sentiment_summary.csv")

# Print summary
print(sentiment_summary)
