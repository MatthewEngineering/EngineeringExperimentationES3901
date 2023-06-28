import io
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = False


def main(buffer):
    print(buffer)
    b = io.BytesIO(buffer)
    print(b)
    image = Image.open(b)
    image.show()

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    print(img_byte_arr)

# pic saved 
import FinalCodebase.image_storage as image_storage
buffer = image_storage.a
main(buffer) 

