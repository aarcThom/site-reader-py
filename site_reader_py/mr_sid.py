from osgeo import gdal

def test_sid():
    # open the .sid file
    dataset = gdal.Open('C:/Users/rober/source/repos/aarcThom/site-reader-py/test_data/ecw-sid/BCVANC15_I11.sid')

    # see https://gis.stackexchange.com/a/201320
    ulx, xres, xskew, uly, yskew, yres  = dataset.GetGeoTransform()
    lrx = ulx + (dataset.RasterXSize * xres)
    lry = uly + (dataset.RasterYSize * yres)


    scale = '-scale min_val max_val'
    options_list = [
    '-ot Byte',
    '-of JPEG',
    scale
    ]

    options_string = " ".join(options_list)
    gdal.Translate('test.jpg', dataset, options=options_string)

    return f'top left pt = [{ulx}, {uly}]'