from PIL import Image

filepath = str(input("enter filepath = "))
image = Image.open(filepath)
x = int(input("enter pixel width = "))
y = int(input("enter pixel height = "))
new_image = image.resize((x, y), resample=0)
new_image.show()
