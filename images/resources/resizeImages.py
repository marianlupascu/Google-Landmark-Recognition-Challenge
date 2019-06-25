# Presupunem ca in acelasi folder cu script-ul avem directoarele test/ si train/ si fisierele .scv
import os
import pandas as pd
import glob
import numpy as np
import shutil
from shutil import copyfile
from PIL import Image

folder1 = 'original\\'
folder2 = 'resized\\'
landmarks1 = glob.glob(folder1 + '*\\')
nrLandmarks1 = len(landmarks1)
size = 600, 600

ind = 0
for landmark1 in landmarks1:
    ind = ind + 1
    pictures1 = glob.glob(landmark1 + '*.jpg')
    nrPictures1 = len(pictures1)
    print(landmark1)
    
    ind2 = 0
    for picture1 in pictures1:
        ind2 = ind2 + 1
        if ind2 % 100 == 0:
            print(str(ind2 * 100 / nrPictures1) + '%')
        landmarks2 = folder2 + landmark1.replace(folder1, '').replace('\\', '') + '/'
        if not os.path.exists(landmarks2):
            os.makedirs(landmarks2)
        imgFilename = picture1.replace(folder1, folder2)
        current = picture1 # unde se afla poza cu tot cu nume si extensie
        try:
            im1 = Image.open(current)
            im1.thumbnail(size, Image.ANTIALIAS)
            im1.save(imgFilename, "JPEG")
        except:
            None