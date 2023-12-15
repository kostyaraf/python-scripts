import requests
from PIL import Image
from io import BytesIO
import pandas as pd

# Список URL изображений, массив строк
image_urls = []

def analyze_image(url, index, total):
    try:
        print(f"Processing: {index}/{total}...")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept': 'image/webp,*/*'
        }
        response = requests.get(url, headers=headers)
        size_kb = len(response.content) / 1024  # Размер в килобайтах

        image = Image.open(BytesIO(response.content))
        width, height = image.size  # Ширина и высота изображения
        image_format = image.format

        return {
            'url': url,
            'size_kb': size_kb,
            'format': image_format,
            'width': width,
            'height': height,
            'error': ''
        }
    except Exception as e:
        print(f"Image {index} - error")
        return {
            'url': url,
            'size_kb': '',
            'format': '',
            'width': '',
            'height': '',
            'error': "can't be opened"
        }

total_images = len(image_urls)
results = [analyze_image(url, index + 1, total_images) for index, url in enumerate(image_urls)]

# Преобразование результатов в DataFrame
df = pd.DataFrame(results)

# Сохранение результатов в CSV
# df.to_csv('image_analysis_results.csv', index=False)
# Сохранение результатов в Excel
df.to_excel('image_analysis_results.xlsx', index=False)

print("Анализ завершен, результаты сохранены в 'image_analysis_results.csv'")