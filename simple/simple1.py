import rasterio
from rasterio.plot import show
from matplotlib import pyplot

from rasterio.plot import show_hist


# contains only 3 out of 13 Sentinel-2 bands:
# Blue (band 1), Green (band 2), and Red (band 3).
dataset = rasterio.open('geotiff/sample.tif')

print(f"TIFF metadata: {dataset.meta}")
print(f"TIFF bounds: {dataset.bounds}")
print(f"TIFF wkt: {dataset.crs.to_wkt()}")

fig, (axr, axg, axb) = pyplot.subplots(1,3, figsize=(21,7))
show((dataset, 1), ax=axr, cmap='Reds', title='red channel')
show((dataset, 2), ax=axg, cmap='Greens', title='green channel')
show((dataset, 3), ax=axb, cmap='Blues', title='blue channel')

show_hist(
    dataset, bins=50, lw=0.0, stacked=False, alpha=0.3,
    histtype='stepfilled', title="Histogram")


pyplot.show()