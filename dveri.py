import requests
from bs4 import BeautifulSoup

# URL страницы с товарами
url = "https://arsdveri.ru/product-category/vhodnye-dveri/?per_row=6&shop_view=grid&per_page=2000"

# Получаем HTML-код страницы
response = requests.get(url)
html = response.content

print('начинаем...')

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Находим все блоки с товарами
products = soup.find_all("div", class_="product-grid-item")

# Создаем пустой список для хранения данных
data = []

# Проходимся по каждому товару и извлекаем необходимые данные
for product in products:
    # Название товара
    title = product.find("h3", class_="wd-entities-title").text.strip()
    
    # Цена товара
    price = product.find("span", class_="woocommerce-Price-amount").text.strip()
    
    # Ссылка на фото товара
    image_url = product.find("img")["src"]
    
    # Добавляем данные в список
    data.append([image_url, title, price])

# Создаем CSV-файл и записываем данные
import csv

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Ссылка на фото", "Название двери", "Цена"])
    writer.writerows(data)
    print('готово')