import pandas as pd
import statsmodels.api as sm

# Load sentiment results
data = pd.read_csv("../data/sentiment_results.csv")

# Prepare regression variables
X = data[["Is_Assigned_Seating"]]  # Independent variable: Assigned Seating flag
y = data["Sentiment_Numeric"]      # Dependent variable: Sentiment score

# Add constant for regression
X = sm.add_constant(X)

# Fit regression model
model = sm.OLS(y, X).fit()

# Save regression results
with open("../data/regression_results.txt", "w") as f:
    f.write(model.summary().as_text())

print(model.summary())