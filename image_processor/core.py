# core.py
import os
from image_processor.image_utils import read_image, save_image
from image_processor.processing import resize_image
from image_processor.visualization import plot_image

def main():
    input_image_path = "assets/imag-1.jpg"  # Caminho da imagem de entrada
    output_image_path = "assets/output/imag-1_resized.jpg"  # Caminho para salvar a imagem redimensionada

    # Ler a imagem
    image = read_image(input_image_path)

    # Redimensionar a imagem
    resized_image = resize_image(image, proportion=0.5)

    # Criar o diretório de saída se não existir
    output_dir = os.path.dirname(output_image_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Salvar a imagem redimensionada
    save_image(resized_image, output_image_path)

    # Plotar a imagem redimensionada
    plot_image(resized_image)

if __name__ == "__main__":
    main()
