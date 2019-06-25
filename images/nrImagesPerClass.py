# Presupunem ca in acelasi folder cu script-ul avem directoarele test/ si train/ si fisierele .scv
import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import shutil

# folder = 'train\\'
# landmarks = glob.glob(folder + '*\\')
# nrLandmarks = len(landmarks)
nrPicByLandmark = []
# ind = 0
# for landmark in landmarks:
#     ind = ind + 1
#     pictures = glob.glob(landmark + '*.jpg')
#     nrPictures = len(pictures)
#     landmarkName = landmark.replace(folder, '').replace('\\', '')
#     print('Landmark', ind, 'out of', nrLandmarks, 'with landmark id', landmarkName)
#     nrPicByLandmark.append([landmarkName, nrPictures])

# Sortam descrescator
def key(elem):
    return elem[1]

# print('Sorting landmarks')
# nrPicByLandmark.sort(key=key, reverse=True)

# # print('Deleting landmarks from 1001 to the end')
# # ind = 0
# # nrClassessToKeep = 1000
# # for stat in nrPicByLandmark:
# #     ind = ind + 1
# #     landmarkId = str(stat[0])
# #     if ind <= nrClassessToKeep:
# #         print(str(ind) + '. Skipping landmark id ' + landmarkId + ' nr images ' + str(stat[1]))
# #         continue
    
# #     print(str(ind) + '. Deleting landmark id ' + landmarkId + ' nr images ' + str(stat[1]))
# #     shutil.rmtree(folder + landmarkId + '\\')

# Write to file
# print('Writing statistics to file')
# with open("statistics.txt", 'w+') as f:
#     f.write('Statistics\n\n')
#     ind = 0
#     for stat in nrPicByLandmark:
#         ind = ind + 1
#         print('Writing statistic', ind, 'out of', nrLandmarks)
#         f.write(str(ind) + '. Number of images : ' + str(stat[1]) + ' landmark id : ' + str(stat[0]) + '\n')

# Write to file
print('Writing statistics to file')
with open("statistics (1).txt", 'r+') as f:
    content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 

for c in content:
    numbers = [int(s) for s in c.split(' ') if s.isdigit()]
    print(numbers)
    nrPicByLandmark.append([numbers[1], numbers[0]])

print('Sorting landmarks')
nrPicByLandmark.sort(key=key, reverse=True)

# Create plot
labels = []
vals = []
nrBins = 50
for i in range(nrBins):
    labels.append(nrPicByLandmark[i][0])
    vals.append(nrPicByLandmark[i][1])

ind = np.arange(nrBins)
plt.bar(ind, vals)
plt.xlabel('Landmark in decreasing order')
plt.ylabel('Number of images')
plt.xticks(ind, labels, fontsize=5, rotation=30)
plt.title('Top 50 landmarks by number of images')
plt.show()