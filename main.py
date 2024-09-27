from PIL import Image

img = Image.open('image.webp')

width, height = img.size
print(f"Image size: {width}X{height}")


mode = img.mode
print(f"Image format: {mode}")
