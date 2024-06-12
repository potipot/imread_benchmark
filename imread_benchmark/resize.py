from pathlib import Path
import fire
from tqdm import tqdm
import cv2


def main(img_dir: str, target_dir: str, target_height: int, target_width: int):
    img_dir = Path(img_dir).expanduser()
    target_dir = Path(target_dir)
    target_dir.mkdir(exist_ok=True)

    for image_path in tqdm(img_dir.glob("*.jpg"), desc="resizing images..."):
        image = cv2.imread(image_path)
        resized_image = cv2.resize(image, (target_width, target_height))
        cv2.imwrite(target_dir / image_path.name, resized_image)

    
if __name__ == "__main__":
    fire.Fire(main)