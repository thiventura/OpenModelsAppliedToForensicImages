import argparse
import os.path
import numpy as np
from shutil import copyfile
from classify_image import classifyImagenet, classifyNsfw

FLAGS = None

def evaluateImages():
  source_directory = FLAGS.images_dir
  details_directory = FLAGS.details_dir

  listOfFiles = os.listdir(source_directory)
  classifyNsfw (source_directory, details_directory, listOfFiles)

  listOfFiles = os.listdir(source_directory)
  classifyImagenet (source_directory, details_directory, listOfFiles)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument(
      '--images_dir',
      required=True,
      type=str,
      help='Path where the image will be read.'
  )
  parser.add_argument(
      '--details_dir',
      required=True,
      type=str,
      help='Each image will be moved to this folder according its category. The filename will be modified with its score regarding the category.'
  )
  FLAGS = parser.parse_args()

  if (FLAGS.details_dir is not None and not os.path.exists(FLAGS.details_dir)):
    os.makedirs(FLAGS.details_dir)

  evaluateImages()
