from PIL import Image
import numpy as np

def determine_flag(image_path):
    image = Image.open(image_path).convert("RGB")

    width, height = image.size
    crop_box = (width // 4, height // 4, 3 * width // 4, 3 * height // 4)
    cropped_image = image.crop(crop_box)

    cropped_image = cropped_image.resize((100, 100))

    top_half = cropped_image.crop((0, 0, 100, 50))

    def average_rgb(img):
        pixels = np.array(img)
        r, g, b = pixels[:, :, 0], pixels[:, :, 1], pixels[:, :, 2]
        return (r.mean(), g.mean(), b.mean())

    top_avg = average_rgb(top_half)

    if top_avg[0] > 150 and top_avg[1] < 100 and top_avg[2] < 100:
        return "Indonesia Flag"
    else:
        return "Poland Flag"

if __name__ == "__main__":
    image_path = input("Enter path:")
    result = determine_flag(image_path)
    print(f"{result}")