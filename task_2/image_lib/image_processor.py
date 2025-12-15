from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def init(self, image):
        self.image = image
    
    def apply_emboss(self):
        """Вариант 5: фильтр Эмбосс"""
        if self.image:
            self.image = self.image.filter(ImageFilter.EMBOSS)
            print("Применен фильтр Эмбосс")
            return self.image
        return None
    
    def add_watermark(self):
        """Вариант 5: водяной знак 'Вариант 5'"""
        if self.image:
            # Создаем объект для рисования
            draw = ImageDraw.Draw(self.image)
            
            # Используем стандартный шрифт
            try:
                font = ImageFont.truetype("arial.ttf", 30)
            except:
                font = ImageFont.load_default()
            
            # Текст и позиция (правый нижний угол)
            text = "Вариант 5"
            width, height = self.image.size
            text_width = 100  # приблизительная ширина текста
            
            # Позиция с отступом 10 пикселей
            position = (width - text_width - 10, height - 40)
            
            # Добавляем текст белого цвета
            draw.text(position, text, fill=(255, 255, 255), font=font)
            
            print("Добавлен водяной знак")
            return self.image
        return None
