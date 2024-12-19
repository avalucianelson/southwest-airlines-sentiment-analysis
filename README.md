# ✈️ Southwest Airlines Sentiment Analysis

This project aims to analyze sentiment trends related to Southwest Airlines, focusing on recent operational changes such as assigned seating. By leveraging sentiment analysis across various platforms, I provide insights into customer perceptions and their impact on brand equity.


## 📈 Project Overview

The analysis explores the sentiment surrounding Southwest Airlines, particularly focusing on the introduction of assigned seating. The project utilizes data from Reddit, YouTube, and NewsAPI to assess public sentiment and its implications for brand equity and operational strategy.

### Goals of the Analysis

- **Enterprise Complexity**: Examine the relationship between operational changes and brand strategy, using sentiment analysis as evidence.
- **Brand Equity**: Analyze customer sentiment to assess brand equity, focusing on the new assigned seating policy.
- **Regression Analysis**: Use regression to evaluate sentiment differences between discussions on assigned seating and general Southwest topics.

## 🛠️ Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/avalucianelson/southwest-airlines-sentiment-analysis.git
   cd southwest-airlines-sentiment-analysis
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

To run the sentiment analysis script, use the following command:

   ```bash
   python scripts/sentiment_over_time_last_year.py
   ```

Ensure that the necessary data files are in place as described in the [Data](#data) section.

## 📊 Data

The data used in this project should be placed in the `data` directory. The primary data file is `sentiment_results.csv`, which contains sentiment scores and related information.

## 📜 Scripts

- `sentiment_over_time_last_year.py`: Analyzes sentiment trends over the past year and generates visualizations.
- `newsapi_scraper.py`: Collects news articles related to Southwest Airlines.
- `reddit_scraper.py`: Gathers Reddit posts and comments about Southwest Airlines.
- `visualization.py`: Visualizes sentiment distribution across platforms.

## 📈 Results

The results of the analysis, including visualizations, are stored in the `visualizations` directory. Key insights and trends are documented in the `results` folder.


