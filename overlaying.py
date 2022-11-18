#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Joel Nteupe 
          
"""

import os
import cv2
import skimage
import rasterio
import solaris as sol
import matplotlib.pyplot as plt
from utils.config import PROJECT_ROOT
from solaris.vector import mask
from rasterio.plot import show
import geopandas as gpd


input_raster = PROJECT_ROOT + "results/Test/inputs/debi_tiguet_image.tif"
geo_raster = (
    PROJECT_ROOT + "results/Test/savedfiles/debi_tiguet_image/debi_tiguet_image.geojson"
)

src = rasterio.open(input_raster)
ref = gpd.read_file(geo_raster)
fig, ax = plt.subplots(figsize=(10, 10))
plt.axis("off")
rasterio.plot.show(src, ax=ax)
# myshp.plot(ax=ax, facecolor='none', edgecolor='red')
ref.plot(categorical=False, legend=False, linewidth=3, ax=ax)
print("Size of source image:".format(src.shape))
plt.show()
