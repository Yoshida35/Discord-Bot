import qrcode

print('What would you want your qr code to say?')
data = str(input())

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red', back_color = 'white')


img.save('C:/Users/josh8/Documents')
#Change to front slash when using python.
#Of stead of C:\Users\josh8\Documents.

#Tutorial 57:00
#https://www.youtube.com/watch?v=SqvVm3QiQVk&t=3192s

#Using Visual Studios but I'm still learing it since it is different to regular python.
