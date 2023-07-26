import tensorflow as tf
import os

# Constants defining the size of the input images
IMG_WIDTH = 64
IMG_HEIGHT = 64
IMG_CHANNELS = 3  # Assuming the images are RGB

def load_image(image_file):
    # Read and decode an image file to a uint8 tensor
    image = tf.io.read_file(image_file)
    image = tf.image.decode_jpeg(image, channels=IMG_CHANNELS)
    
    # Convert the image to float32 tensor
    image = tf.cast(image, tf.float32)
    
    # Normalize the pixel values to the range [-1, 1]
    image = (image / 127.5) - 1
    
    # Resize the image
    image = tf.image.resize(image, [IMG_WIDTH, IMG_HEIGHT])
    
    return image

def load_data():
    # Get a list of all image file paths in the data directory
    image_files = tf.io.gfile.glob("moma_collection/*.jpg")
    
    # Create a dataset from the file paths
    dataset = tf.data.Dataset.from_tensor_slices(image_files)
    
    # Map the load_image function to each file path
    dataset = dataset.map(load_image, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    
    # Shuffle and batch the dataset
    BATCH_SIZE = 32
    dataset = dataset.shuffle(1000).batch(BATCH_SIZE)
    
    return dataset
