from PIL import Image
import os


def convert_gif_to_png(gif_path, png_path):
    gif_image = Image.open(gif_path)
    # RGBAモードに変換
    rgba_image = gif_image.convert("RGBA")
    rgba_image.save(png_path)
    print(f"Converted: {gif_path} -> {png_path}")


def convert_gifs_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".gif"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(
                output_folder, os.path.splitext(file_name)[0] + ".png"
            )
            convert_gif_to_png(input_path, output_path)


def main():
    # 入力画像があるフォルダへのパスを指定してください
    input_folder = "output_dance_frames"
    # 処理後の画像を保存するフォルダへのパスを指定してください
    output_folder = "output_pngs"

    convert_gifs_in_folder(input_folder, output_folder)


if __name__ == "__main__":
    main()
