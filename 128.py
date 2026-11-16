from PIL import Image

# 1. Компьютердегі бар суретті ашу (сурет пен код бір папкада болуы тиіс)
img = Image.open("fox.jpg")  # "sample.jpg" орнына өз суретіңіздің атын жазыңыз

# 2. Метрика үшін түпнұсқаны 512x512 өлшеміне келтіріп сақтау
img_original = img.resize((512, 512), Image.Resampling.BICUBIC)
img_original.save("original_512.jpg")

# 3. Сапасын нашарлату (128x128 өлшеміне кішірейту)
img_low = img_original.resize((128, 128), Image.Resampling.BICUBIC)
img_low.save("low_res_128.jpg")

print(
    "Дайын! 'low_res_128.jpg' (сапасы нашар) және 'original_512.jpg' (эталон)"
    " сақталды."
)