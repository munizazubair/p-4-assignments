import qrcode

data = "hello world"
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
qr_img = qr.make_image(fill_color="blue", back_color="white")

qr_img.save("C:/Users/SIBGHAT/Desktop/test/qrcode.png")
