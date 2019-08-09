from PIL import Image
from PIL import ImageOps
img = Image.open("Webp.net-resizeimage (2).jpg").convert("L")
img = ImageOps.invert(img)
img.save("Webp.net-resizeimage (2).jpg")
