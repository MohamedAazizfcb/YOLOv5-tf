import os
import numpy

width = [0.50, 0.75, 1.0, 1.25]
depth = [0.33, 0.67, 1.0, 1.33]

versions = ['s', 'm', 'l', 'x']
data_dir = os.path.join('..', 'Dataset')

threshold = 0.3
max_boxes = 150
image_dir = 'images'
label_dir = 'labels'

num_epochs = 300
batch_size = 32
image_size = 640
class_dict = {}

version = 's'
anchors = numpy.array([[8., 9.],    [16., 24.],   [28., 58.],
                       [41., 25.],  [58., 125.],  [71., 52.],
                       [129., 97.], [163., 218.], [384., 347.]], numpy.float32)
