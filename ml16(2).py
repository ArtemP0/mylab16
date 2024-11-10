import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt

with open('keywords.txt', 'r', encoding='utf-8') as f:
    keywords = f.read().split()
with open('web.txt', 'r', encoding='utf-8') as f:
    urls = [line.strip() for line in f if line.strip()]
for keyword in keywords:
    histogram_data = {}
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')
            text = soup.get_text().lower()
            word_count = text.count(keyword.lower())
            histogram_data[url] = word_count
        except requests.RequestException as e:
            print("Помилка")
            histogram_data[url] = 0
    urls_list = list(histogram_data.keys())
    counts = list(histogram_data.values())
    plt.barh(urls_list, counts, color='skyblue')
    plt.xlabel("Кількість появ")
    plt.ylabel("URL сайту")
    plt.title(f"Гістограма появ ключового слова '{keyword}' на сайтах")
    output_filename = f"{keyword}_histogram.png"
    plt.savefig(output_filename)
    print(f"Графічна гістограма збережена у файл ")
    plt.close()
