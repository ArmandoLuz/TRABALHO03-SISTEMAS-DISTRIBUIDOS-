from PIL import Image, ImageOps
import os
from server.settings import settings
from server.repositories.image_repository import image_repository


# Aplicar filtros
def apply_invert_filter(image):
    return ImageOps.invert(image.convert("RGB"))

def apply_grayscale_filter(image):
    return ImageOps.grayscale(image)

def apply_pixelate_filter(image):
    small = image.resize((image.width // 10, image.height // 10), resample=Image.NEAREST)
    return small.resize(image.size, resample=Image.NEAREST)

def get_filters():
    return {
        "invert": apply_invert_filter,
        "grayscale": apply_grayscale_filter,
        "pixelate": apply_pixelate_filter
    }

def apply_filter(image, filter_type):
    try:
        filters = get_filters()
        return filters[filter_type](image)
    except KeyError:
        raise Exception("Filtro inválido.")


def save_file(file):
    filename = file.filename
    filepath = os.path.join(settings.PROCESSED_PATH, filename)
    file.save(filepath)
    print(f"Imagem salva em {filepath}")

def processing_image(file_image, filter_type):
    #save_file(file_image)

    image = Image.open(file_image)
    processed_image = apply_filter(image, filter_type)

    processed_filename = f"processed_{file_image.filename}"
    processed_filepath = os.path.join(settings.PROCESSED_PATH, processed_filename)
    processed_image.save(processed_filepath)

    image_repository(filename=file_image.filename, filter_type=filter_type, filepath=processed_filepath,)

    return processed_filepath
