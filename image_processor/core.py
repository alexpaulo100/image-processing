import os
from matplotlib.image import imsave
import numpy as np
from image_processor.image_utils import read_image, save_image
from image_processor.processing import resize_image
from image_processor.visualization import plot_image

def main():
    print("Iniciando o processamento da imagem...")

    input_image_path = "image_processor/assets/imag-1.jpg"  
    output_image_path = "image_processor/assets/output/imag-1_resized.jpg"  

    # Ler a imagem
    image = read_image(input_image_path)
    print(f"Imagem lida com sucesso: {input_image_path}")
    print(f"Tipo da imagem: {type(image)}")

    # Verifique se a imagem foi lida corretamente
    if not isinstance(image, np.ndarray):
        raise ValueError("A imagem não foi lida corretamente, verifique a função read_image.")

    # Redimensionar a imagem
    resized_image = resize_image(image, proportion=0.5)
    print("Imagem redimensionada.")
    print(f"Tipo da imagem redimensionada: {type(resized_image)}")

    # Verifique se a imagem redimensionada é um array NumPy
    if not isinstance(resized_image, np.ndarray):
        raise ValueError("A imagem redimensionada não foi gerada corretamente.")

    # Criar o diretório de saída se não existir
    output_dir = os.path.dirname(output_image_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Diretório criado: {output_dir}")

    # Salvar a imagem redimensionada
    try:
        print(f"Salvando imagem em: {output_image_path}")
        save_image(output_image_path, resized_image)
        print(f"Imagem salva: {output_image_path}")
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")

    # Plotar a imagem redimensionada
    try:
        print("Plotando a imagem redimensionada...")
        plot_image(resized_image)
    except Exception as e:
        print(f"Erro ao plotar a imagem: {e}")

    print(f"Image shape: {image.shape}, dtype: {image.dtype}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")


