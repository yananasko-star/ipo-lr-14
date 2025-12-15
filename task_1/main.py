from image_lib.image_handler import ImageHandler
from image_lib.image_processor import ImageProcessor

def main():
    print("=== Лабораторная работа №14. Задание 1 ===")
    
    # Запрашиваем путь к изображению
    image_path = input("Введите путь к изображению: ").strip()
    
    # Создаем обработчик изображений
    handler = ImageHandler(image_path)
    
    # Загружаем изображение
    image = handler.load_image()
    if not image:
        return
    
    # Изменяем размер
    new_width = int(input("Введите новую ширину: "))
    new_height = int(input("Введите новую высоту: "))
    handler.resize_image(new_width, new_height)
    
    # Сохраняем промежуточный результат
    handler.save_image("resized_image.jpg")
    
    # Передаем изображение процессору
    processor = ImageProcessor(handler.get_image_for_processing())
    
    # Применяем фильтр
    filter_name = input("Введите фильтр (BLUR, EMBOSS, SHARPEN и др.): ").upper()
    processor.apply_filter(filter_name)
    
    # Добавляем текст
    text = input("Введите текст для добавления на изображение: ")
    processor.add_text(text, position=(20, 20))
    
    # Сохраняем результат
    output_path = input("Введите путь для сохранения результата (например: result.jpg): ")
    handler.image = processor.get_processed_image()
    handler.save_image(output_path)
    
    print("Обработка завершена!")

if name == "main":
    main()
