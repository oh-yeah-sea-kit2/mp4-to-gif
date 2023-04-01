import os
from PIL import Image


def extract_frames(gif_path, output_dir):
    frame_number = 0

    with Image.open(gif_path) as gif:
        os.makedirs(output_dir, exist_ok=True)

        while True:
            try:
                gif.seek(frame_number)
                current_frame = gif.copy()
                output_path = os.path.join(
                    output_dir,
                    f"frame{frame_number:03d}.png",
                )
                current_frame.save(output_path, "PNG")
                frame_number += 1

            except EOFError:
                break

    print(f"{frame_number} frames extracted to {output_dir}")


def main():
    # 入力GIFファイルへのパスを指定してください
    input_gif_path = "output/output.gif"
    # 分解したフレームを保存するディレクトリへのパスを指定してください
    output_directory = "output/frames"

    extract_frames(input_gif_path, output_directory)


if __name__ == "__main__":
    main()
