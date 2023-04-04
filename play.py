import os

IMAGE_TRAIN_DIR = "/workspaces/SuperYOLOH/dataset/VEDAI"
# IMAGE_VAL_DIR = "/dbfs/FileStore/tables/models/receipt-image/segments/large-regions/data/raw/val/"



# remove all of the infrared images from VEDAI/images
for f_name in os.listdir("/workspaces/SuperYOLOH/dataset/VEDAI/images"):
    if "_ir" in f_name:
        os.remove(f"/workspaces/SuperYOLOH/dataset/VEDAI/images/{f_name}")

# remove "_co" from
# loop through all files in the directory
for filename in os.listdir(IMAGE_TRAIN_DIR + "/images"):
    
    # check if the filename contains '_co'
    if '_co' in filename:
        
        # construct the new filename by removing '_co'
        new_filename = filename.replace('_co', '')
        
        # rename the file
        os.rename(os.path.join(IMAGE_TRAIN_DIR + "/images", filename), os.path.join(IMAGE_TRAIN_DIR + "/images", new_filename))


python train.py --cfg models/SRyolo_noFocus_small.yaml --super --train_img_size 1024 --hr_input --data data/SRvedai.yaml --ch 3 --input_mode RGB