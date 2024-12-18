import pandas as pd
import statsmodels.api as sm
from datetime import datetime
import os

# Define the absolute path to the data file
data_file_path = "/Users/avanelson/Southwest Sentiment Analysis/southwest-airlines-sentiment-analysis/data/sentiment_results.csv"

# Check if the file exists, and create it if it doesn't
if not os.path.exists(data_file_path):
    # Create a DataFrame with default data or an empty DataFrame
    default_data = pd.DataFrame({
        "Date": pd.to_datetime([]),  # Empty date column
        "Sentiment_Label": []  # Empty sentiment label column
    })
    # Save the default DataFrame to the CSV file
    default_data.to_csv(data_file_path, index=False)
    print(f"Created a new file at {data_file_path} with default data.")

# Load sentiment data
data = pd.read_csv(data_file_path)

# Map sentiment labels to numeric values
sentiment_mapping = {"Positive": 1, "Neutral": 0, "Negative": -1}
data["Sentiment_Numeric"] = data["Sentiment_Label"].map(sentiment_mapping)

# Convert date to numerical format
# Assuming "Date" is in ISO 8601 format, like "2023-12-18 10:00:00"
data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
data = data.dropna(subset=["Date"])  # Drop rows with invalid dates
data["Date_Numeric"] = (data["Date"] - data["Date"].min()).dt.days  # Days since the first date

# Prepare regression variables
X = data["Date_Numeric"]  # Independent variable: Date as numeric
y = data["Sentiment_Numeric"]  # Dependent variable: Sentiment score

# Add constant to X for regression
X = sm.add_constant(X)

# Fit regression model
model = sm.OLS(y, X).fit()

# Ensure the directory exists
output_dir = "../data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save regression summary to a text file
with open(os.path.join(output_dir, "date_sentiment_regression_results.txt"), "w") as f:
    f.write(model.summary().as_text())

# Print summary to console
print(model.summary())

import matplotlib.pyplot as plt
import numpy as np

# Predict values for the regression line
data["Predicted_Sentiment"] = model.predict(X)

# Plot actual sentiment vs. date
plt.figure(figsize=(10, 6))
plt.scatter(data["Date"], data["Sentiment_Numeric"], alpha=0.5, label="Actual Sentiment")
plt.plot(data["Date"], data["Predicted_Sentiment"], color="red", label="Regression Line")
plt.title("Sentiment Over Time")
plt.xlabel("Date")
plt.ylabel("Sentiment Score")
plt.legend()
plt.grid(True)

# Ensure the directory exists
visualization_dir = "../visualizations"
if not os.path.exists(visualization_dir):
    os.makedirs(visualization_dir)

# Save and show the plot
plt.savefig(os.path.join(visualization_dir, "sentiment_over_time.png"))
plt.show()
print("Plot saved to ../visualizations/sentiment_over_time.png")