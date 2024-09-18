def resize_image(image, target_size):
    from skimage.transform import resize

    resized_image = resize(image, target_size, anti_aliasing=True)
    return resized_image
