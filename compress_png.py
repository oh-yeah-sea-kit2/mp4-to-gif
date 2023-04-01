from PIL import Image
import os


def compress_png_image(input_path, output_path, compress_level=9):
    png_image = Image.open(input_path)
    png_image.save(output_path, "PNG", compress_level=compress_level)
    print(f"Compressed: {input_path} -> {output_path}")


def compress_pngs_in_folder(input_folder, output_folder, compress_level=9):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".png"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            compress_png_image(input_path, output_path, compress_level)


def main():
    # 入力画像があるフォルダへのパスを指定してください
    input_folder = "output_pngs"
    # 処理後の画像を保存するフォルダへのパスを指定してください
    output_folder = "output_compressed_pngs"
    # 圧縮レベルを指定してください (0-9)
    compress_level = 9

    compress_pngs_in_folder(input_folder, output_folder, compress_level)


if __name__ == "__main__":
    main()
