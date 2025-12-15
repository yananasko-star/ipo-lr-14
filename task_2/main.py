from image_lib.image_handler import ImageHandler
from image_lib.image_processor import ImageProcessor

def main():
    print("=== Задание 2. Вариант 5 ===")
    
    # 1. Загружаем
    path = input("Введите путь к изображению: ")
    handler = ImageHandler(path)
    handler.load_image()
    
    # 2. Масштабируем 50%
    handler.scale_to_50_percent()
    
    # 3. Сохраняем с датой
    handler.save_with_date()
    
    # 4. Фильтр Эмбосс
    processor = ImageProcessor(handler.image)
    processor.apply_emboss()
    
    # 5. Водяной знак
    processor.add_watermark()
    
    # 6. Финальное сохранение
    handler.image.save("final_variant5.jpg")
    print("Готово! Файл: final_variant5.jpg")

if name == "main":
    main()
