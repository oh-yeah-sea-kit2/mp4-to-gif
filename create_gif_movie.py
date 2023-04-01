import os
from PIL import Image


def create_gif_from_images(input_folder, output_gif_path, duration=100):
    image_files = []
    for f in os.listdir(input_folder):
        if f.lower().endswith(".png"):
            image_files.append(f)
    image_files.sort()

    images = []
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)
        images.append(image)

    images[0].save(
        output_gif_path,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0,
    )
    print(f"GIFアニメーションが作成されました: {output_gif_path}")


def main():
    # 入力画像があるフォルダへのパスを指定してください
    input_folder = "output/remove_bg_frames"
    # 出力するGIFファイルへのパスを指定してください
    output_gif_path = "output/remove_bg_output.gif"
    frame_duration = 30  # フレーム間の時間をミリ秒単位で指定してください

    create_gif_from_images(
        input_folder,
        output_gif_path,
        duration=frame_duration,
    )


if __name__ == "__main__":
    main()
