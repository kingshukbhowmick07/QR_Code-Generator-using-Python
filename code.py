import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)

#providing the url of the webpage to be redirected__
qr.add_data("https://www.score7.io/tournaments/cemptk1npz/overview")
qr.make(fit=True)

#image description of the qr-code__
img=qr.make_image(fill_color="black",back_color="grey")

#image to be saved in the name of__
img.save("wscube_web2.png")
