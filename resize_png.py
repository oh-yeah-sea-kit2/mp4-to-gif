from PIL import Image
import os


def resize_png_image(input_path, output_path, scale_factor=0.5):
    png_image = Image.open(input_path)
    new_size = (
        int(png_image.width * scale_factor),
        int(png_image.height * scale_factor),
    )
    resized_image = png_image.resize(new_size, Image.ANTIALIAS)
    resized_image.save(output_path, "PNG")
    print(f"Resized: {input_path} -> {output_path}")


def resize_pngs_in_folder(input_folder, output_folder, scale_factor=0.5):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".png"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            resize_png_image(input_path, output_path, scale_factor)


def main():
    # 入力画像があるフォルダへのパスを指定してください
    input_folder = "output_pngs"
    # 処理後の画像を保存するフォルダへのパスを指定してください
    output_folder = "output_resized_pngs"
    # 縮小したいスケールファクターを指定してください
    scale_factor = 0.25

    resize_pngs_in_folder(input_folder, output_folder, scale_factor)


if __name__ == "__main__":
    main()
