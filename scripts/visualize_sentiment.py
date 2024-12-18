import pandas as pd
import matplotlib.pyplot as plt
import os

# Load sentiment summary
sentiment_summary = pd.read_csv("../data/sentiment_summary.csv", index_col=0)

# Ensure the directory exists
os.makedirs("../visualizations", exist_ok=True)

# Define colors for each sentiment
colors = ['red', 'yellow', 'green']  # Assuming the order is negative, neutral, positive

# Plot sentiment distribution per platform with specified colors
ax = sentiment_summary.plot(kind="bar", figsize=(10, 6), stacked=True, color=colors)
plt.title("Sentiment Distribution by Platform")
plt.xlabel("Platform")
plt.ylabel("Number of Mentions")
plt.xticks(rotation=0)
plt.legend(title="Sentiment")
plt.tight_layout()

# Add percentage annotations
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    
    # Get the platform name from the x position
    platform_index = int(x + width / 2)
    platform_name = sentiment_summary.index[platform_index]
    
    # Get the total for the current platform
    total = sentiment_summary.loc[platform_name].sum()
    
    # Calculate the percentage
    percentage = f'{height / total * 100:.1f}%'
    
    # Annotate the bar with the percentage
    ax.annotate(percentage, (x + width / 2, y + height / 2), ha='center', va='center')

# Save the plot
plt.savefig("../visualizations/sentiment_distribution.png")
plt.show()
print("Visualization saved to ../visualizations/sentiment_distribution.png")