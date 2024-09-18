import numpy as np
from skimage.io import imread, imsave


def read_image(path, is_gray=False):
    return imread(path, as_gray=is_gray)


def save_image(path, image):
    if image.dtype == np.float64 or image.dtype == np.float32:
        image = (image * 255).astype(np.uint8)

    imsave(path, image)
