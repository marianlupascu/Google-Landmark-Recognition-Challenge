# Presupunem ca in acelasi folder cu script-ul avem directoarele test/ si train/ si fisierele .scv
import os
import pandas as pd

folder = 'train/'
#filenames = glob.glob(folder + '*.jpg')
#nrFiles = len(filenames)

df = pd.read_csv('train.csv',delimiter=',')
nrLines = df.shape[0]
print('Grouping', nrLines, 'files')
for index, row in df.iterrows():
    print('File {0} out of {1} : {2:.4f}%'.format(index, nrLines, (float(index + 1) / nrLines) * 100))
    # Daca e nevoie creem folder-ul asociat acestui landarmk
    landmarkFolder = folder + str(row['landmark_id']) + '/'
    if not os.path.exists(landmarkFolder):
        os.makedirs(landmarkFolder)

    # Citim imaginea si o mutam in folder-ul asociat
    imgFilename = folder + str(row['id']) + '.jpg' # toate au fost salvate cu extensia .jpg

    current = imgFilename # unde se afla poza cu tot cu nume si extensie
    new = landmarkFolder + str(row['id']) + '.jpg' # unde mut poza, cu tot cu nume si extensie

    # Verific mai intai ca poza sa existe
    if os.path.exists(current):
        os.rename(current, new)