# Presupunem ca in acelasi folder cu script-ul avem directoarele test/ si train/ si fisierele .scv
import os
import pandas as pd
import glob

folder = 'resized\\'
foldertrain = 'train\\'
foldertest = 'test\\'
foldervalidation = 'val\\'
landmarks = glob.glob(folder + '*\\')
nrLandmarks = len(landmarks)
ind = 0

if not os.path.exists(foldertrain):
    os.makedirs(foldertrain)
if not os.path.exists(foldervalidation):
    os.makedirs(foldervalidation)
if not os.path.exists(foldertest):
    os.makedirs(foldertest)

for landmark in landmarks:
    ind = ind + 1
    pictures = glob.glob(landmark + '*.jpg')
    nrPictures = len(pictures)
    landmarkFolder = landmark.replace(folder, '').replace('\\', '')
    print(landmarkFolder)
    
    intPict = 0 

    if not os.path.exists(foldertrain + landmarkFolder):
        os.makedirs(foldertrain + landmarkFolder)
    if not os.path.exists(foldervalidation + landmarkFolder):
        os.makedirs(foldervalidation + landmarkFolder)
    if not os.path.exists(foldertest + landmarkFolder):
        os.makedirs(foldertest + landmarkFolder)

    for picture in pictures:
        intPict = intPict + 1
        if intPict <= nrPictures * 0.7:
            pictureName = picture.replace(landmark, '').replace('\\', '')
            current = picture
            new =  foldertrain + landmarkFolder + '\\'+ pictureName
            if os.path.exists(current):
                os.rename(current, new)
        else:
            if intPict <= nrPictures * 0.85:
                pictureName = picture.replace(landmark, '').replace('\\', '')
                current = picture
                new =  foldervalidation + landmarkFolder + '\\'+ pictureName
                if os.path.exists(current):
                    os.rename(current, new)
            else:
                pictureName = picture.replace(landmark, '').replace('\\', '')
                current = picture
                new =  foldertest + landmarkFolder + '\\'+ pictureName
                if os.path.exists(current):
                    os.rename(current, new)