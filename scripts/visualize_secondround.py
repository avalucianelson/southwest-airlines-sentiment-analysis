import pandas as pd
import matplotlib.pyplot as plt
import os

# Load sentiment results
data = pd.read_csv("../data/sentiment_results.csv")

# Calculate average sentiment by topic
avg_sentiment = data.groupby("Is_Assigned_Seating")["Sentiment_Numeric"].mean()
avg_sentiment.index = ["General Southwest", "Assigned Seating"]

# Plot average sentiment
plt.figure(figsize=(8, 5))
avg_sentiment.plot(kind="bar", color=["blue", "orange"], alpha=0.7)
plt.title("Average Sentiment: Assigned Seating vs. General Southwest")
plt.ylabel("Average Sentiment Score")
plt.xlabel("Topic")
plt.xticks(rotation=0)
plt.tight_layout()

# Save and display the plot
output_dir = "../visualizations"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f"{output_dir}/assigned_vs_general_sentiment.png")
plt.show()
print("Visualization saved to ../visualizations/assigned_vs_general_sentiment.png")