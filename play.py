import os

IMAGE_TRAIN_DIR = "/workspaces/SuperYOLOH/dataset/VEDAI"
# IMAGE_VAL_DIR = "/dbfs/FileStore/tables/models/receipt-image/segments/large-regions/data/raw/val/"



for directory in [IMAGE_TRAIN_DIR, IMAGE_VAL_DIR]:
    with open(os.path.join(directory, "image_files.txt"), mode="w") as f:
        f.writelines([os.path.join(directory, "images", image_file) for image_file in os.listdir(directory, "images")])
