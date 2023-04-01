import os
from rembg import remove
from PIL import Image
import io  # 追加


def process_image(input_path, output_path):
    with open(input_path, "rb") as img_file:
        output_img_data = remove(img_file.read(), alpha_matting=True)
        output_img = Image.open(io.BytesIO(output_img_data))  # 修正

    output_img.save(output_path, "PNG")


def process_images_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".png"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            process_image(input_path, output_path)
            print(f"Processed: {input_path} -> {output_path}")


def main():
    # 入力画像があるフォルダへのパスを指定してください
    input_folder = "output/frames"
    # 処理後の画像を保存するフォルダへのパスを指定してください
    output_folder = "output/remove_bg_frames"

    process_images_in_folder(input_folder, output_folder)


if __name__ == "__main__":
    main()
