from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/SIBGHAT/Desktop/test/qrcode.png")
result = decode(img)

print(result)