import argparse
import sys
import os.path
from shutil import move
import numpy as np
import gc
import tensorflow as tf
from id_to_category import getCategoryImagenet
from read_image import read_image_for_nsfw, read_image_for_imagenet
from load_model import loadGraphNsfw, loadGraphImagenet

IMAGENET_N = 3

# Prediction with Imagenet
def predictionImagenet(image_path):
  image = read_image_for_imagenet(image_path)
  input_operation = 'DecodeJpeg/contents:0'
  with tf.Session() as sess:
    try:
      output_operation = sess.graph.get_tensor_by_name("softmax:0")
      predictions = sess.run(output_operation, {input_operation: image})
      return np.squeeze(predictions)
    except Exception as e:
      print (e)
  return None

# Prediction with NSFW
def predictionNsfw(graph, image_path):
  input_operation = graph.get_operation_by_name("import/input")
  output_operation = graph.get_operation_by_name("import/predictions")

  with tf.Session(graph=graph) as sess:
    try:
      image = read_image_for_nsfw(image_path)
      results = sess.run(output_operation.outputs[0],{input_operation.outputs[0]: image})
      return np.squeeze(results)
    except Exception as e:
      print (e)
  return None


def moveImage (source, dest, fileName):
  if not os.path.exists( dest ):
    os.mkdir( dest )
  move( source, os.path.join(dest, fileName) )


def classify (model, sourceDirectory, detailsDirectory, listOfFiles, graph=None):
  count = 0

  for imageFile in listOfFiles:
    count += 1
    print (model, count, imageFile)    
    imageFullPath = os.path.join(sourceDirectory, imageFile)

    if os.path.getsize(imageFullPath) <= 10000:
      print ("small size")
      folder = os.path.join( detailsDirectory, "pequeno" )
      moveImage (imageFullPath, folder, imageFile)
      continue

    if (model == "nsfw"):
      predictions = predictionNsfw (graph, imageFullPath)
      if predictions is None:
        # Corrupted image
        print ("error")
        folder = os.path.join( detailsDirectory, "erro" )
        moveImage (imageFullPath, folder, imageFile)
      else:
        if predictions[1] > 0.8:
          # pornography
          print ("Pornography")
          folder = os.path.join( detailsDirectory, "pornografia" )
          score = ( "%.2f" % (predictions[1]*100) ).zfill(6)
          moveImage (imageFullPath, folder, score + "_" + imageFile)
    else:
      predictions = predictionImagenet (imageFullPath)
      if predictions is None:
        # Corrupted image
        print ("error")
        folder = os.path.join( detailsDirectory, "erro" )
        moveImage (imageFullPath, folder, imageFile)
      else:
        classified = False
        top_k = predictions.argsort()[-IMAGENET_N:][::-1]
        for node_id in top_k:
          category = getCategoryImagenet ( str(node_id) )
          if category:
            # Imagenet category
            folder = os.path.join( detailsDirectory, category )
            score = ( "%.2f" % (predictions[node_id]*100) ).zfill(6)
            moveImage (imageFullPath, folder, score + "_" + imageFile)
            classified = True
            print ("Selected as category ", category)
            break
        if not classified:
          # Not in NSFW or Imagenet
          # It goes to "other" folder
          print ("Other folder")
          folder = os.path.join( detailsDirectory, "outro" )
          moveImage (imageFullPath, folder, imageFile)

    if count % 100 == 0:
      # Reload graph because memory issues 
      # And call garbage collector
      if (model == "nsfw"):
        graph = loadGraphNsfw()
      gc.collect()           


# Classify with NSFW model
def classifyNsfw (sourceDirectory, detailsDirectory, listOfFiles):
  print ('Classifying with NSFW')
  graph = loadGraphNsfw()
  classify ("nsfw", sourceDirectory, detailsDirectory, listOfFiles, graph)

# Classify with Imagenet model
def classifyImagenet (sourceDirectory, detailsDirectory, listOfFiles):
  print ('Classifying with Imagenet')
  loadGraphImagenet()
  classify ("imagenet", sourceDirectory, detailsDirectory, listOfFiles)
