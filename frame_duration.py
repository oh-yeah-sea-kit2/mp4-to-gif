from PIL import Image


def get_frame_durations(gif_path):
    with Image.open(gif_path) as gif:
        durations = []
        for frame in range(0, gif.n_frames):
            gif.seek(frame)
            duration = gif.info.get("duration", 0)
            durations.append(duration)
    return durations


def main():
    gif_path = "output/output.gif"  # 入力GIFファイルへのパスを指定してください

    frame_durations = get_frame_durations(gif_path)
    print(f"フレーム間の時間: {frame_durations}")


if __name__ == "__main__":
    main()
