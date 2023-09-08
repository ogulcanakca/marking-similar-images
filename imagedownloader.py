import os
import requests
import openpyxl
from io import BytesIO
from PIL import Image

folderPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Trendyol Resimler')
current_directory = folderPath
xlsx_files = [os.path.join(current_directory, file) for file in os.listdir(current_directory) if file.endswith(".xlsx")]

def is_image(url):
    response = requests.head(url)
    content_type = response.headers["content-type"]
    return content_type.startswith("image")

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200 and is_image(url):
        image = Image.open(BytesIO(response.content))
        if image.mode == "RGBA":
            image = image.convert("RGB")
        return image
    else:
        print(f"Resim indirme hatası! URL: {url}")
        return None

def delete_after_jpg(input_string):
    index = input_string.find("jpg")
    while index != -1:
        input_string = input_string[:index]
        index = input_string.find("jpg")
    return input_string

def creating_image(image_url):
    image = download_image(image_url)
    print(f"{folder_name} klasörüne {image_url} hedefinden indiriliyor...")
    if image:
        if(not os.path.exists(folder_name)):
            os.makedirs(folder_name, exist_ok=True)
        result = delete_after_jpg(row[name_column])
        image.save(os.path.join(folder_name, f"{result}.jpg"))

for file_path in xlsx_files:
    url_column = 4 
    name_column = 1
    dosyaIsımleri = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    folder_name = os.path.splitext(file_path)[0]

    if(os.path.exists(folder_name)):
        for item in os.listdir(folder_name):
            dosyaIsımleri.append(item.replace(".",""))
    for row in sheet.iter_rows(values_only=True):
        image_url = row[url_column]
        if image_url and isinstance(image_url, str):
            if(not os.path.exists(folder_name)):
                creating_image(image_url)
            else:   
                if row[1] not in dosyaIsımleri:
                    creating_image(image_url)