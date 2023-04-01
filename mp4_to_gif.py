from moviepy.editor import VideoFileClip


def mp4_to_gif(input_video_path, output_gif_path):
    clip = VideoFileClip(input_video_path)
    clip.write_gif(output_gif_path)


def main():
    input_video_path = "VID_119840625_131719_113.mp4"
    output_gif_path = "output/output.gif"
    # MP4動画をGIF動画に変換
    mp4_to_gif(input_video_path, output_gif_path)


if __name__ == "__main__":
    main()
