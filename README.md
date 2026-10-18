# 📚 Book Price Tracker & Scraper

An automated Python web scraping tool that monitors book prices from [books.toscrape.com](http://books.toscrape.com/), checks whether they meet a target threshold defined by the user, and logs the historical data into a CSV file.

## ✨ Features

- **Batch Web Scraping:** Extracts titles and prices for all books on the page using `requests` and `BeautifulSoup`.
- **Data Cleaning & Normalization:** Strips currency symbols and encoding artifacts, converting prices directly into numeric `float` values.
- **Dynamic User Threshold:** Prompts the user interactively in the terminal to set their desired target price.
- **Conditional Alert Logic:** Evaluates each book's price against the threshold and prints real-time status alerts.
- **Automated CSV Logging:** Appends timestamped records (`Timestamp`, `Title`, `Price`) to `prices.csv` for historical tracking.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed on your system.

### Installation

1. Clone this repository or download the project files.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
