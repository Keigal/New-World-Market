import pytesseract as tess
from PIL import Image

img = Image.open('cache/buy-orders/green_wood.png')

newsize = (3840, 2160)

img = img.resize(newsize)

print(img.size)

img.show()

text = tess.image_to_string(img)

print(text)


