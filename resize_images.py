from PIL import Image
import os
import glob

def resize_to_youtube_ratio(image_path):
    try:
        img = Image.open(image_path)
        # standard youtube ratio is 16:9. Let's make them 1280x720
        # If the image is square (e.g., 1024x1024), we crop the center 1024x576, then resize to 1280x720
        width, height = img.size
        
        target_ratio = 16.0 / 9.0
        current_ratio = width / height
        
        if current_ratio > target_ratio:
            # Image is wider than 16:9, crop width
            new_width = int(height * target_ratio)
            left = (width - new_width) / 2
            top = 0
            right = left + new_width
            bottom = height
        else:
            # Image is taller than 16:9, crop height
            new_height = int(width / target_ratio)
            left = 0
            top = (height - new_height) / 2
            right = width
            bottom = top + new_height
            
        img_cropped = img.crop((left, top, right, bottom))
        img_resized = img_cropped.resize((1280, 720), Image.Resampling.LANCZOS)
        
        img_resized.save(image_path)
        print(f"Resized {image_path} to 1280x720")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

if __name__ == '__main__':
    img_dir = r"c:\Users\Comp\silverbowl\img\blog"
    images = glob.glob(os.path.join(img_dir, "*.png"))
    for img_path in images:
        resize_to_youtube_ratio(img_path)
