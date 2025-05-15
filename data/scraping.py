import pandas as pd
import requests
# from bs4 import BeautifulSoup

def scrape_laptops():
    """Scrape sample laptop data (replace with actual source)"""
    data = [
        {"name": "Laptop A", "price": 28450, "specs": "8GB RAM, 256GB SSD, Intel i3"},
        {"name": "Laptop B", "price": 26650, "specs": "16GB RAM, 512GB SSD, AMD Ryzen 5"},
          {"name": "Laptop c", "price": 24450, "specs": "8GB RAM, 256GB SSD, Intel i3"},
        {"name": "Laptop d", "price": 21650, "specs": "16GB RAM, 512GB SSD, AMD Ryzen 5"},
          {"name": "Laptop e", "price": 22450, "specs": "8GB RAM, 256GB SSD, Intel i3"},
        {"name": "Laptop f", "price": 23650, "specs": "16GB RAM, 512GB SSD, AMD Ryzen 5"},
          {"name": "Laptop g", "price": 19450, "specs": "8GB RAM, 256GB SSD, Intel i3"},
        {"name": "Laptop h", "price": 17650, "specs": "16GB RAM, 512GB SSD, AMD Ryzen 5"},
          {"name": "Laptop i", "price": 450, "specs": "8GB RAM, 256GB SSD, Intel i3"},
        {"name": "Laptop j", "price": 13650, "specs": "16GB RAM, 512GB SSD, AMD Ryzen 5"},
          {"name": "Laptop k", "price": 14450, "specs": "8GB RAM, 256GB SSD, Intel i3"},
        {"name": "Laptop l", "price": 16650, "specs": "16GB RAM, 512GB SSD, AMD Ryzen 5"},
          {"name": "Laptop m", "price": 12550, "specs": "8GB RAM, 256GB SSD, Intel i3"},
        {"name": "Laptop n", "price": 65500, "specs": "16GB RAM, 512GB SSD, AMD Ryzen 5"},
          {"name": "Laptop o", "price": 45000, "specs": "8GB RAM, 256GB SSD, Intel i3"},
        {"name": "Laptop p", "price": 65000, "specs": "16GB RAM, 512GB SSD, AMD Ryzen 5"},
    ]
    df = pd.DataFrame(data)
    df.to_csv("data/laptops.csv", index=False)

if __name__ == "__main__":
    scrape_laptops()