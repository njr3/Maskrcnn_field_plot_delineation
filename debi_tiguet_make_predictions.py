"""

@author: Joel Nteupe - Manobi Africa
          
"""

import cv2
import json
import os
import PIL
import numpy as np
from datetime import datetime
from skimage import io, color
import matplotlib.pyplot as plt
from numpy import asarray
from numpy import savetxt
from osgeo import gdal
import skimage
import geopandas as gpd
import rasterio
from rasterio import features
import rasterio as rio
from rasterio.merge import merge
from rasterio import windows
from shapely.geometry import shape
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import skimage.io as io
import matplotlib.image as mpimg
from tkinter import Tcl
import tensorflow as tf
from PIL import Image
import numpy

# Set this to True to see more logs details
os.environ["AUTOGRAPH_VERBOSITY"] = "5"
tf.autograph.set_verbosity(3, False)
tf.cast
from patchify import patchify, unpatchify
import warnings

warnings.filterwarnings("ignore")
from utils.config import CustomConfig
from IPython import get_ipython

# get_ipython().system('nvidia-smi')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = BASE_DIR + "/"
print(PROJECT_ROOT)

##########################################################################################################################
##########################################################################################################################
#                                Introduction & Set up working directory                                                         #
##########################################################################################################################
##########################################################################################################################

"""
Steps:
    
1. Prepare the training/Validation data set
 For this case, Get satelite imagery of your area of interest. Slice the images into 1024*1024 patches then split them
 into the training and validation folders. 
2. Annotate your images generated using the https://www.makesense.ai/ platform. Save the images in coco format. 
3. Save the .json file in the respective folders after creating it. 
4. Install and download the M-RCNN module from github.
5. Use the script below accrodingly
"""
##########################################################################################################################
#                                      Model setup                                                                     #
##########################################################################################################################
"""
#Use MRCNN for version 2.X tensorflow
#!git clone https://github.com/BupyeongHealer/Mask_RCNN_tf_2.x.git for tf 2.x  #Steven
#installtensorflow 2.3.0 and keras 2.4
#!pip install tensorflow==2.3.0
#!pip install keras==2.4
#!pip install --upgrade h5py==2.10.0
"""

# Get the project root directory
project_path = PROJECT_ROOT
RCNN_ROOT = os.path.abspath(project_path + "Mask_RCNN")
os.chdir(RCNN_ROOT)
print("Printing the current project root dir".format(os.getcwd()))

# Import Mask RCNN
from Mask_RCNN.mrcnn import utils
import Mask_RCNN.mrcnn.model as modellib
from Mask_RCNN.mrcnn import visualize
from Mask_RCNN.mrcnn.model import log
from PIL import Image, ImageDraw

with open("mrcnn/model.py") as f:
    model_file = f.read()

with open("mrcnn/model.py", "w") as f:
    model_file = model_file.replace(
        "self.keras_model = self.build(mode=mode, config=config)",
        "self.keras_model = self.build(mode=mode, config=config)\n        self.keras_model.metrics_tensors = []",
    )
    f.write(model_file)

"""
Set up logging and pre-trained model paths
This will default to sub-directories in your mask_rcnn_dir, but if you want them somewhere else, updated it here.

It will also download the pre-trained coco model.
"""

# Directory to save logs and trained model
MODEL_DIR = os.path.join(RCNN_ROOT, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(RCNN_ROOT, "mask_rcnn_coco.h5")
# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

#######################################################################################################################
#                                  Make Predictions                                                                      #
#######################################################################################################################

class_number = 1

config = CustomConfig(class_number)
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
model.load_weights(PROJECT_ROOT + "saved_model/mask_rcnn_object_0015.h5", by_name=True)

# Apply a trained model on large image
print(PROJECT_ROOT)
img = cv2.imread(PROJECT_ROOT + "samples/roi/MaliDec2016/Couche_gamma.shp")  # BGR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
patch_size = 1024
print(img.shape)



