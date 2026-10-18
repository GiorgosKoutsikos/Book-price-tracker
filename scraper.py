import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/"

def track_price():

    #Stores the response(HTML code, headers, status)
    response  = requests.get(url)

    print("Status code:", response.status_code)

    #Converts it into a structured "tree" of objects, so that we can search through it.
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_ = "product_pod")
    print(f"We found {len(books)} ")

    target_price = float(input("Give me your ideal price: "))

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("prices.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for book in books:
            title = book.find("h3").find("a")["title"]
            raw_book = book.find("p", class_ = "price_color").text
            raw_price = raw_book.replace("£", "").replace("Â", "")
            price = float(raw_price)

            if price <= target_price:
                    print(f"Bargain! Book price dropped: {price}. Name: {title}")
            else:
                    print(f"Price still high: {price}")

            writer.writerow([now, title, price])


if __name__ == "__main__":
    track_price()
