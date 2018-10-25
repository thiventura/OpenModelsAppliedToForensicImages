import tensorflow as tf

NSFW_MODEL = '../models/nsfw.pb'
IMAGENET_MODEL = '../models/inception_v2.pb'

# Load graph for NSFW
def loadGraphNsfw(): 
  graph = tf.Graph()
  graph_def = tf.GraphDef()
  with open(NSFW_MODEL, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)
  return graph

# Load graph for Imagenet
def loadGraphImagenet():
  with tf.gfile.FastGFile(IMAGENET_MODEL, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')
