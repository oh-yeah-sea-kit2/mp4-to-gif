import os
import cv2
import numpy as np
import torch
import torchvision.transforms as T
from PIL import Image
from torchvision.models.segmentation import DeepLabV3_ResNet101_Weights


def remove_background(input_image_path, output_image_path):
    # Load the model
    model = torch.hub.load(
        "pytorch/vision",
        "deeplabv3_resnet101",
        pretrained=True,
        weights=DeepLabV3_ResNet101_Weights.DEFAULT,
    )
    model.eval()

    # Load the input image
    input_image = Image.open(input_image_path).convert("RGB")
    input_image = np.array(input_image)

    # Preprocess the input image
    preprocess = T.Compose(
        [
            T.ToTensor(),
            T.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225],
            ),
        ]
    )
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)

    # Apply the model
    with torch.no_grad():
        output = model(input_batch)["out"][0]
    output_predictions = output.argmax(0)

    # Create a binary mask for the person class (label 15)
    mask = output_predictions == 15

    # Apply the mask to the input image
    input_image_with_alpha = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGRA)
    input_image_with_alpha[:, :, 3] = mask.cpu().numpy().astype(np.uint8) * 255

    # Save the output image
    cv2.imwrite(output_image_path, input_image_with_alpha)


def process_images_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".png"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            remove_background(input_path, output_path)
            print(f"Processed: {input_path} -> {output_path}")


def main():
    # weights = DeepLabV3_ResNet101_Weights.DEFAULT
    # 入力画像があるフォルダへのパスを指定してください
    input_folder = "output/frames"
    # 処理後の画像を保存するフォルダへのパスを指定してください
    output_folder = "output/remove_bg_frames2"
    process_images_in_folder(input_folder, output_folder)


if __name__ == "__main__":
    main()
