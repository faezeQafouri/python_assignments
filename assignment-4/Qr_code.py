
import qrcode
from PIL import Image

text= input("Enter what you want to convert in QR code: ")
Qr= qrcode.make(text)
# Qr.add_text(text)
# qr = qrcode.QRCode(version = 1,
#                    box_size = 10,
#                    border = 5)

# img = Qr.make_image(fill_color = 'red',
#                     back_color = 'white')
 

Qr.save('QRcode-Assignment4.jpg')

 

 
