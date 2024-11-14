import os
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
import random

input_folder = "."
output_folder = "augmented_photos"

os.makedirs(output_folder, exist_ok=True)

def augment_image(image):
    # Görüntüyü RGB moduna dönüştürme
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # Resmi döndür (0 ile 20 derece arasında)
    angle = random.uniform(0, 20) 
    augmented_image = image.rotate(angle)

    # Parlaklık değiştirme
    brightness_enhancer = ImageEnhance.Brightness(augmented_image)
    brightness_factor = random.uniform(0.7, 1.3) 
    augmented_image = brightness_enhancer.enhance(brightness_factor)

    # Kontrast değiştirme
    contrast_enhancer = ImageEnhance.Contrast(augmented_image)
    contrast_factor = random.uniform(0.7, 1.3)  
    augmented_image = contrast_enhancer.enhance(contrast_factor)

    # %10 olasılıkla bulanıklık ekleme
    if random.random() < 0.1:  
        augmented_image = augmented_image.filter(ImageFilter.GaussianBlur(radius=2))

    # Rastgele şekil çizme
    draw = ImageDraw.Draw(augmented_image)
    shape_type = random.choice(['line', 'rectangle', 'circle'])
    
    # Şekil konumu ve boyutu rastgele, ama fotoğraf boyutunu geçmeme şartı var
    width, height = augmented_image.size
    x1, y1 = random.randint(0, width), random.randint(0, height)
    x2, y2 = random.randint(0, width), random.randint(0, height)

    # Koordinatları sıralama (rectangle çizimi için x1 <= x2 ve y1 <= y2 olma şartı var)
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    if shape_type == 'line':
        draw.line([x1, y1, x2, y2], fill=random.choice(["red", "green", "blue", "yellow"]), width=3)
    elif shape_type == 'rectangle':
        draw.rectangle([x1, y1, x2, y2], outline=random.choice(["red", "green", "blue", "yellow"]), width=3)
    elif shape_type == 'circle':
        radius = random.randint(10, 50)
        draw.ellipse([x1, y1, x1 + radius, y1 + radius], outline=random.choice(["red", "green", "blue", "yellow"]), width=3)

    return augmented_image

# Dosyaları okuma ve veri artırımı uygulama
counter = 1  

for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):  
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        for i in range(10):  # Her fotoğraf için 10 adet çoğaltma yap
            new_filename = f"neutral{counter}.png"
            output_path = os.path.join(output_folder, new_filename)

            # Veri artırımı uygulayıp kaydetme
            augmented_image = augment_image(image)
            augmented_image.save(output_path)

            print(f"{new_filename} kaydedildi.")
            counter += 1  
