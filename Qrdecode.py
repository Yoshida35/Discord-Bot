from pyzbar.pyzbar import decode

from PIL import Image

FileLocation = input('Where is the QR code located? (Please replace backslash with forward slash!)')
img = Image.open(FileLocation)

result = decode(img)

print(result)

#Tutorial 1:01:00
#https://www.youtube.com/watch?v=SqvVm3QiQVk&t=3192s
