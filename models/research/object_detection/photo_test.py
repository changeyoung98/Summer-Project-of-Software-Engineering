import matplotlib
matplotlib.use('Agg')
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tensorflow as tf
import time
import csv
from PIL import Image
from argparse import ArgumentParser


# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

from utils import label_map_util
from utils import visualization_utils as vis_util


parser = ArgumentParser(description='photo test.')
parser.add_argument(
    '--path', required=True,
    help='Path to the image file.')

# What model to download.
MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

# extract the ssd_mobilenet
start = time.clock()
NUM_CLASSES = 90
IMAGE_SIZE = (128, 256)
opener = urllib.request.URLopener()
# opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
# tar_file = tarfile.open(MODEL_FILE)
# for file in tar_file.getmembers():
#   file_name = os.path.basename(file.name)
#   if 'frozen_inference_graph.pb' in file_name:
#     tar_file.extract(file, os.getcwd())
end = time.clock()
print('load the model', (end - start))

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,use_display_name=True)
category_index = label_map_util.create_category_index(categories)


def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)


def main():
    args = parser.parse_args()
    query_csv = open('E://triplet-reid/data/query.csv', 'w', newline='')
    query_writer = csv.writer(query_csv)
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            writer = tf.summary.FileWriter("logs/", sess.graph)
            sess.run(tf.global_variables_initializer())
            image= Image.open(args.path)
            image_np = load_image_into_numpy_array(image)
            # the array based representation of the image will be used later in order to prepare the
            # result image with boxes and labels on it.
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            # Actual detection.
            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                 feed_dict={image_tensor: image_np_expanded})
            # Visualization of the results of a detection.
            image_tmp, items = vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=6)
            width, height = image.size
            for box, color in items:
                ymin, xmin, ymax, xmax = box
                (left, right, top, bottom) = (xmin * width, xmax * width,
                                              ymin * height, ymax * height)
                print("left: ", left)
                print("right: ", right)
                print("top: ", top)
                print("bottom: ", bottom)
                region = (left, top, right, bottom)
                cropImg = image.crop(region)
                cropImg = cropImg.resize(IMAGE_SIZE, Image.ANTIALIAS)
                cropImg.save("e://triplet-reid/reid-test/query/camera1_query1.jpg")
                present_time = time.clock()
                name_str = "query/camera1_query1.jpg"
                query_writer.writerow([int(present_time), name_str])
                query_writer.writerow([int(present_time), name_str])
    query_csv.close()
    os.system('cd /d e://triplet-reid &&'
              ' python embed.py'
              ' --experiment_root experiments/my_experiment'
              ' --dataset data/query.csv --filename query.h5'
              ' --flip_augment --aggregator mean'
              ' --checkpoint checkpoint-25000 --quiet')


if __name__ == '__main__':
    main()