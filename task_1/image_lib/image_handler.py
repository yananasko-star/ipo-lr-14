from PIL import Image
import os

class ImageHandler:
    def init(self, image_path):
        """Инициализация с путем к изображению"""
        self.image_path = image_path
        self.image = None
        
    def load_image(self):
        """Загрузка изображения"""
        try:
            self.image = Image.open(self.image_path)
            print(f"Изображение загружено: {self.image_path}")
            print(f"Размер: {self.image.size}, Формат: {self.image.format}")
            return self.image
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return None
    
    def save_image(self, output_path, format=None):
        """Сохранение изображения"""
        if self.image:
            try:
                self.image.save(output_path, format=format)
                print(f"Изображение сохранено: {output_path}")
                return True
            except Exception as e:
                print(f"Ошибка сохранения: {e}")
                return False
        else:
            print("Нет изображения для сохранения")
            return False
    
    def resize_image(self, width, height):
        """Изменение размера изображения"""
        if self.image:
            resized_img = self.image.resize((width, height))
            self.image = resized_img
            print(f"Размер изменен на: {width}x{height}")
            return self.image
        else:
            print("Сначала загрузите изображение")
            return None
    
    def convert_format(self, new_format):
        """Изменение формата изображения (например, 'JPEG', 'PNG')"""
        if self.image:
            self.image = self.image.convert('RGB')
            print(f"Формат изменен на: {new_format}")
            return self.image
        else:
            print("Сначала загрузите изображение")
            return None
    
    def get_image_for_processing(self):
        """Передача изображения в ImageProcessor"""
        return self.image
