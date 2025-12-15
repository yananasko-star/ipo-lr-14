from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def init(self, image):
        """Инициализация с изображением из ImageHandler"""
        self.image = image
        
    def apply_filter(self, filter_name):
        """Применение фильтра к изображению"""
        if self.image:
            filters = {
                'BLUR': ImageFilter.BLUR,
                'CONTOUR': ImageFilter.CONTOUR,
                'DETAIL': ImageFilter.DETAIL,
                'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
                'EMBOSS': ImageFilter.EMBOSS,
                'SHARPEN': ImageFilter.SHARPEN,
                'SMOOTH': ImageFilter.SMOOTH
            }
            
            if filter_name in filters:
                filtered_img = self.image.filter(filters[filter_name])
                self.image = filtered_img
                print(f"Применен фильтр: {filter_name}")
                return self.image
            else:
                print(f"Фильтр {filter_name} не найден")
                return None
        else:
            print("Нет изображения для обработки")
            return None
    
    def add_text(self, text, position=(10, 10), color=(255, 0, 0), font_size=20):
        """Добавление текста на изображение"""
        if self.image:
            try:
                # Создаем объект для рисования
                draw = ImageDraw.Draw(self.image)
                
                # Пытаемся загрузить шрифт, иначе используем стандартный
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()
                
                # Добавляем текст
                draw.text(position, text, fill=color, font=font)
                print(f"Добавлен текст: {text}")
                return self.image
            except Exception as e:
                print(f"Ошибка добавления текста: {e}")
                return None
        else:
            print("Нет изображения для обработки")
            return None
    
    def rotate_image(self, angle):
        """Поворот изображения на заданный угол"""
        if self.image:
            rotated_img = self.image.rotate(angle, expand=True)
            self.image = rotated_img
            print(f"Изображение повернуто на {angle} градусов")
            return self.image
        else:
            print("Нет изображения для обработки")
            return None
    
    def get_processed_image(self):
        """Возвращает обработанное изображение"""
        return self.image
