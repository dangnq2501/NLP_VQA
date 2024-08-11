import os
import shutil
import pandas as pd


csv_file_path = '/home/dang/my_projects/vqa_dataset/test.csv'
source_folder = '/home/dang/my_projects/vqa_dataset/test2017'
destination_folder = '/home/dang/my_projects/vqa_dataset/images'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

df = pd.read_csv(csv_file_path)

image_ids = df['img_id'].tolist()

cnt = 0
for image_id in image_ids:
    # Construct the source file path
    image_id = str(image_id)
    image_id = "0" * (12-len(image_id))+image_id
    source_file = os.path.join(source_folder, f"{image_id}.jpg")
    # print(source_file)
    
    destination_file = os.path.join(destination_folder, f"{image_id}.jpg")
    
    if os.path.exists(source_file) and not os.path.exists(destination_file):
        shutil.copy(source_file, destination_file)
    if os.path.exists(destination_file):
        cnt += 1
print(cnt, len(df))

print("Finished copying files.")
