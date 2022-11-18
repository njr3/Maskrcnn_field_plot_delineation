
import matplotlib.pyplot as plt
from matplotlib import pyplot
import rasterio
import matplotlib.pyplot as plt
import skimage.io as io
from rasterio.plot import show
from utils.config import PROJECT_ROOT

# Load original Image
src = rasterio.open(PROJECT_ROOT + "samples/roi/debi_tiguet_image.tif")
# Load the predicted Image

src1 = rasterio.open(
    PROJECT_ROOT + "results/Test/georeferenced/gray_debi_tiguet_image.tif"
)
fig, (axr, axg) = plt.subplots(1, 2, figsize=(21, 7))
show(src, ax=axr, title="Original Image")
show(src1, ax=axg, title="Predicted Raster")
pyplot.show()
