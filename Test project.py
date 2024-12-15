import qrcode

data = ''

img = qrcode.make(data)
img.save('save.png')