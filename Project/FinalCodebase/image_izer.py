import io
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = False


# basically noise from clicking the button once
#buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9\xd9')

# new from the image 
# buffer = bytearray(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x04\x00\x00\x00\x01\x08\x02\x00\x00\x00v^\x98\x9a\x00\x00\x00\x11IDATx\x9cc```\xf8\xff\xff?\x84\x04\x00\x1d\xef\x05\xfb`/\x1e'\x00\x00\x00\x00IEND\xaeB`\x82")

# pic just taken 
import image_storage
buffer = image_storage.b

# import image_izer
#buffer = bytearray(image_izer.a)


print(buffer)
b = io.BytesIO(buffer)
print(b)
image = Image.open(b)

# image = Image.open('.//..//circuit.jpg')

image.show()

# Interpret the buffer as a JPEG image
#image = Image.open("..\dcode-image.png")


img_byte_arr = io.BytesIO()
image.save(img_byte_arr, format='JPEG')
img_byte_arr = img_byte_arr.getvalue()

print(img_byte_arr)



# Process the image as needed (e.g., save it, dixlay it, etc.)
#image.save("image.jpg")  # Example: Save the image as a JPEG file