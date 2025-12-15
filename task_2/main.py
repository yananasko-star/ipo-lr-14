from image_lib.image_handler import ImageHandler
from image_lib.image_processor import ImageProcessor

print("=== Задание 2. Вариант 5 ===")

# 1. Загружаем изображение
path = input("Введите путь к изображению: ")
handler = ImageHandler(path)
handler.load_image()

# 2. Масштабируем до 50%
handler.scale_to_50_percent()

# 3. Сохраняем с датой
handler.save_with_date()

# 4. Применяем фильтр Эмбосс
processor = ImageProcessor(handler.image)
processor.apply_emboss()

# 5. Добавляем водяной знак
processor.add_watermark()

# 6. Сохраняем финальный результат
handler.image = processor.image
handler.image.save("final_result.jpg")

print("Готово! Результат в final_result.jpg")
