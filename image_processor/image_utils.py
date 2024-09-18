from skimage.io import imread, imsave
import numpy as np
def read_image(path, is_gray=False):
    return imread(path, as_gray=is_gray)




def save_image(path, image):
    print(f"Tipo do caminho: {type(path)}")  # Deveria ser <class 'str'>
    print(f"Tipo da imagem: {type(image)}")  # Deveria ser <class 'numpy.ndarray'>

    if image.dtype == np.float64 or image.dtype == np.float32:
        image = (image * 255).astype(np.uint8)
    
    imsave(path, image)
