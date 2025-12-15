from PIL import Image
import os
from datetime import datetime

class ImageHandler:
    def init(self, image_path):
        self.image_path = image_path
        self.image = None
        
    def load_image(self):
        """Загрузка изображения (базовая)"""
        self.image = Image.open(self.image_path)
        print("Изображение загружено")
        return self.image
    
    def scale_to_50_percent(self):
        """Вариант 5: масштабирование до 50%"""
        if self.image:
            width, height = self.image.size
            self.image = self.image.resize((width//2, height//2))
            print("Масштабировано до 50%")
            return self.image
        return None
    
    def save_with_date(self):
        """Вариант 5: сохранение с текущей датой"""
        if self.image:
            name = os.path.basename(self.image_path).split('.')[0]
            date = datetime.now().strftime("%Y%m%d")
            new_name = f"{name}_{date}.jpg"
            self.image.save(new_name)
            print(f"Сохранено как: {new_name}")
            return new_name
        return None
