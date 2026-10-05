import qrcode

img = qrcode.make("https://github.com/MiguelFerreira-CMD")
img.save("qr_github.png")