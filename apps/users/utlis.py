from io import BytesIO
from PIL import Image
from django.core.files import File
from django.conf import settings


def compress_image(image):
    '''
        This Function will compress Image untill it's under the specified size,
        or will raise error when the given image cannot be compressed further.
    '''

    quality = 75       # Default Quality to which Image will be Initally Compressed

    current_size = image.size

    # perform Iteration until fize size is under limit
    while current_size > settings.MAX_IMAGE_UPLOAD or quality == 0:
        if quality == 0:
            raise ValueError("Image could not be compressed")

        image_obj = Image.open(image)
        image_obj = image_obj.convert('RGB')
        image_byte = BytesIO()
        image_obj.save(image_byte, 'JPEG', quality=quality)
        new_image = File(image_byte, name=image.name)
        current_size = new_image.size
        quality -= 5  # Reduce quality by -5 with every Iteration

    return new_image
