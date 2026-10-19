# 📚 Book Price Tracker & Scraper

An automated Python web scraping tool that monitors book prices from [books.toscrape.com](http://books.toscrape.com), checks whether they meet a target threshold defined by the user, and logs the historical data into a CSV file.

---

## ✨ Features

- **Batch Web Scraping**: Extracts titles and prices for all books on the page using `requests` and `BeautifulSoup`.
- **Data Cleaning & Normalization**: Strips currency symbols and encoding artifacts, converting prices directly into numeric `float` values.
- **Dynamic User Threshold**: Prompts the user interactively in the terminal to set their desired target price.
- **Conditional Alert Logic**: Evaluates each book's price against the threshold and prints real-time status alerts.
- **Automated CSV Logging**: Appends timestamped records (`Timestamp`, `Title`, `Price`) to `prices.csv` for historical tracking.

---

### Installation

1. Clone this repository or download the project files:

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎓 Educational Purpose & Disclaimer

This project was built strictly for educational and learning purposes to practice and demonstrate fundamental web scraping, data cleaning, and data logging concepts in Python.

- **Target Website**: The scraper interacts with `books.toscrape.com`, an open sandbox created specifically for developers to learn and test web scraping techniques.
- **Responsible Scraping**: It follows scraping etiquette and best practices without abusing server resources.

---

## 🧠 Key Learnings

Building this project provided hands-on experience with core Python and web scraping concepts:

- **HTTP Requests**: Fetching webpage content, headers, and managing status codes using the `requests` library.
- **HTML Parsing & DOM Traversal**: Navigating DOM trees, targeting CSS classes, and extracting elements using `BeautifulSoup`.
- **Data Cleaning & Type Casting**: Sanitizing raw scraped text, stripping currency signs/encoding artifacts, and converting values into numerical `float` types.
- **File I/O & Persistence**: Formatting and appending timestamped data into structured CSV files (`prices.csv`) for persistent tracking.
