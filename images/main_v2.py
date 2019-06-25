#!/usr/bin/python

# Note to Kagglers: This script will not run directly in Kaggle kernels. You
# need to download it and run it on your local machine.

# Downloads images from the Google Landmarks dataset using multiple threads.
# Images that already exist will not be downloaded again, so the script can
# resume a partially completed download. All images will be saved in the JPG
# format with 90% compression quality.

import sys, os, multiprocessing, urllib2, csv
from PIL import Image
from StringIO import StringIO

data_file = 'train.csv'
out_dir = 'train'

landmarkIdsToDownload = ['9779', '2061', '5554', '6651', '6696', '5376', '2743', '4352', 
                        '13526', '1553', '10900', '8063', '8429', '4987', '12220', '11784',
                        '2949', '12718', '3804', '10184', '7092', '10045', '2338', '12172', '3924', '428', '9029']

def ParseData(data_file):
  csvfile = open(data_file, 'r')
  csvreader = csv.reader(csvfile)
  key_url_list = [line[:3] for line in csvreader]
  return key_url_list[1:]  # Chop off header


def DownloadImage(key_url):
  (key, url, landmarkId) = key_url
  if not landmarkId in landmarkIdsToDownload:
    print('Skipping')
    return
  
  landmarkFolder = os.path.join(out_dir, landmarkId)
  filename = os.path.join(landmarkFolder, '%s.jpg' % key)

  if os.path.exists(filename):
    print('Image %s already exists. Skipping download.' % filename)
    return

  if not os.path.exists(landmarkFolder):
    os.makedirs(landmarkFolder)
  
  try:
    response = urllib2.urlopen(url)
    image_data = response.read()
  except:
    print('Warning: Could not download image %s from %s' % (key, url))
    return

  try:
    pil_image = Image.open(StringIO(image_data))
  except:
    print('Warning: Failed to parse image %s' % key)
    return

  try:
    pil_image_rgb = pil_image.convert('RGB')
  except:
    print('Warning: Failed to convert image %s to RGB' % key)
    return

  try:
    pil_image_rgb.save(filename, format='JPEG', quality=90)
  except:
    print('Warning: Failed to save image %s' % filename)
    return


def Run():
  if not os.path.exists(out_dir):
    os.makedirs(out_dir)

  key_url_list = ParseData(data_file)
  pool = multiprocessing.Pool(processes=64)
  pool.map(DownloadImage, key_url_list)

if __name__ == '__main__':
  Run()