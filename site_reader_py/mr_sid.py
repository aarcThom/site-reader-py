from osgeo import gdal

def test_sid():
    # open the .sid file
    dataset = gdal.Open('C:/Users/rober/source/repos/aarcThom/site-reader-py/test_data/ecw-sid/BCVANC15_I11.sid')

    # see https://gis.stackexchange.com/a/201320
    ulx, xres, xskew, uly, yskew, yres  = dataset.GetGeoTransform()
    lrx = ulx + (dataset.RasterXSize * xres)
    lry = uly + (dataset.RasterYSize * yres)

    return f'top left pt = [{ulx}, {uly}]'