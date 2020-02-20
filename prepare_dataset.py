import os
import numpy as np
import pandas as pd
import glob
import argparse
import shutil
from PIL import Image

def jpg_to_png(image_path, mask_path, dest_path, style_image_path, style_mask_path, string):
        print(image_path)
        print(mask_path)
        print(dest_path)
        print(style_image_path)
        print(style_mask_path)
        count = 0
        images_path = sorted(glob.glob(image_path + '/' + '*.jpg'))
        masks_path  = sorted(glob.glob(mask_path + '/' + '*.png'))
        os.mkdir(os.path.join(dest_path,'target_images'))
        os.mkdir(os.path.join(dest_path, 'target_masks'))
        os.mkdir(os.path.join(dest_path, 'style_images'))
        os.mkdir(os.path.join(dest_path, 'style_masks'))
        os.mkdir(os.path.join(dest_path, 'output'))
        os.mkdir(os.path.join(dest_path + '/output', string))
        imageNames = []
        for image in images_path:
                imageName = image.split('/')[-1].split(".")[0]
                imageNames.append(imageName)
        for mask in masks_path:
                maskName = mask.split('/')[-1].split(".")[0]
                if maskName in imageNames:
                        print(maskName)
                        image = Image.open(image_path + '/' + maskName + '.jpg')
                        image.save(dest_path + '/target_images'+ '/' + maskName + '.png')
                        shutil.copyfile(mask_path + '/' + maskName + '.png', dest_path + '/target_masks' + '/' + maskName + '.png')
                        shutil.copyfile(style_image_path, dest_path +'/style_images' +'/'+maskName + '.png')
                        shutil.copyfile(style_mask_path, dest_path + '/style_masks' + '/' + maskName + '.png')
                        count+=1
                        if count > 10:
                                break
