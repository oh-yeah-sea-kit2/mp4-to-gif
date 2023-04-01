# パッケージをインポートする
import os
from PIL import Image

input = "output/remove_bg_frames/"
output = "output/frames_gif/"


def convert_png_to_gif(input_path, output_path):
    img_png = Image.open(input_path)
    # RGBAに変換する
    img_png = img_png.convert("RGBA")
    # RGBAのalpha（透過）を取得する
    alpha = img_png.getchannel("A")
    # alphaのマスクを取得する
    mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
    # gifへ変換するために減色する
    img_gif = img_png.quantize(colors=256)
    # gifにマスクを貼り付ける
    img_gif.paste(im=255, mask=mask)
    # 透過gifをエクスポートする
    img_gif.save(output_path, transparency=255)


for file_name in os.listdir(input):
    if not file_name.lower().endswith(".png"):
        continue
    input_path = os.path.join(input, file_name)
    # 拡張子を覗いたファイル名を取得
    _file_name = os.path.splitext(os.path.basename(file_name))[0]
    output_path = os.path.join(output, f"{_file_name}.gif")
    print(output_path)
    convert_png_to_gif(input_path, output_path)
