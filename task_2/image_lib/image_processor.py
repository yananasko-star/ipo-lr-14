from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def init(self, image):
        self.image = image
    
    # Вариант 5: фильтр Эмбосс
    def apply_emboss(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.EMBOSS)
            print("Применен фильтр Эмбосс")
            return self.image
        return None
    
    # Вариант 5: водяной знак
    def add_watermark(self):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            
            try:
                font = ImageFont.truetype("arial.ttf", 30)
            except:
                font = ImageFont.load_default()
            
            text = "Вариант 5"
            width, height = self.image.size
            
            # Правый нижний угол
            position = (width - 150, height - 50)
            
            # Белый текст
            draw.text(position, text, fill=(255, 255, 255), font=font)
            
            print("Добавлен водяной знак")
            return self.image
        return None
