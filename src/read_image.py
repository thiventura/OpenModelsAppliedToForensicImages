import tensorflow as tf

def read_image_for_imagenet(file_name):
  return tf.gfile.FastGFile(file_name, 'rb').read()


def read_image_for_nsfw(file_name):
  data = tf.read_file(file_name)

  image = tf.image.decode_jpeg(data, channels=3, fancy_upscaling=True, dct_method="INTEGER_FAST")
  image = tf.image.convert_image_dtype(image, tf.float32, saturate=True)
  image = tf.image.resize_images(image, (256, 256), method=tf.image.ResizeMethod.BILINEAR, align_corners=True)
  image = tf.image.convert_image_dtype(image, tf.uint8, saturate=True)
  image = tf.image.encode_jpeg(image, format='', quality=75, progressive=False, optimize_size=False, chroma_downsampling=True, density_unit=None, x_density=None, y_density=None, xmp_metadata=None)
  image = tf.image.decode_jpeg(image, channels=3, fancy_upscaling=False, dct_method="INTEGER_ACCURATE")
  image = tf.cast(image, dtype=tf.float32)
  image = tf.image.crop_to_bounding_box(image, 16, 16, 224, 224)
  image = tf.reverse(image, axis=[2])
  image -= [104, 117, 123]
  image = tf.expand_dims(image, axis=0)

  with tf.Session() as sess:
    return sess.run(image)
