# mp4 -> gif -> 人物切り抜き

## 導入

### MacOS

```sh
brew install ffmpeg
```

| 説明 | ファイル名 |
|----------|----------|
| PNG圧縮 | compress_png.py |
| PNGリサイズ | resize_png.py |
| mp4をgif画像に | mp4_to_gif.py|
| GIF画像をつなげて動画に | create_gif_movie.py |
| GIF画像をつなげて動画に | create_gif_movie2.py |
| GIF画像をPNG画像に | convert_gif_to_png.py |
| PNG画像をGIF画像に | convert_png_to_gif.py |
| フレーム間の時間を取得 | frame_duration.py |
| GIF動画をGIF画像に分ける | gif_movie_to_image.py |
| GIF動画をGIF画像に分ける | extract_frames.py |
| 背景透過(rembg) | remove_background.py |
| 背景透過(DeepLabV3) | remove_background2.py |

## memo

いろいろやったけど背景透過はunscrren proつこうたほうが早い
https://www.unscreen.com/

細かい微調整はGIF動画を画像にして、一枚ずつ編集して最後にくっつけるのがベターっぽい
