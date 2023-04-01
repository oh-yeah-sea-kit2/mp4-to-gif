from PIL import Image
import os


def extract_frames(gif_path, output_folder):
    # GIFを読み込む
    gif = Image.open(gif_path)

    # フレームごとに処理
    frame_number = 0
    try:
        while True:
            # フレームを保存
            output_path = os.path.join(
                output_folder,
                f"frame_{frame_number:03d}.gif",
            )
            gif.save(output_path, "GIF")
            print(f"Saved frame: {output_path}")

            # 次のフレームに進む
            frame_number += 1
            gif.seek(gif.tell() + 1)
    except EOFError:
        # すべてのフレームを処理したら終了
        pass


def main():
    # 入力GIFへのパスを指定してください
    input_gif_path = "dance.gif"
    # フレームを保存するフォルダへのパスを指定してください
    output_folder = "output_dance_frames"

    # 出力フォルダを作成
    os.makedirs(output_folder, exist_ok=True)

    # GIFをフレームに分割
    extract_frames(input_gif_path, output_folder)


if __name__ == "__main__":
    main()
