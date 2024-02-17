from osgeo import gdal
from pathlib import Path
from utility import progress_cb

def allowed_ext(get_list=False) -> str:
    # update this list as you add more extension converters
    allowed_extensions = ['.ecw', '.sid']
    return allowed_extensions if get_list else ', '.join(allowed_extensions)

def check_raster_file(file_in: str) -> bool:
    """Checks if a raster file is in the proper extension and exists

    Args:
        file_in (str): the file path

    Returns:
        bool: True if proper extension and exists
    """
    in_file = Path(file_in)
    return in_file.is_file() and in_file.suffix in allowed_ext(get_list=True)


def convert_raster_jpg(path_in: str, path_out: str) -> list[float]:
    """Converts raster formats such as MrSid and ECW to jpeg to be placed in Rhino.
        Saves jpeg in designated location. Returns corners of image for Rhino Placement.
        
    Args:
        path_in (str): path for file to convert
        path_out (str): folder path for output

    Returns:
        list[float]: upper left X, upper left Y, lower right X, lower right Y
    """

    file_path = Path(path_in)
    dir_path = Path(path_out).joinpath(f'{file_path.stem}.jpg').as_posix()
    file_path = file_path.as_posix()

    dataset = gdal.Open(file_path)

    # Getting the upper left and lower right points of the image
    up_left_x, xres, xskew, up_left_y, yskew, yres  = dataset.GetGeoTransform()
    low_right_x = up_left_x + (dataset.RasterXSize * xres)
    low_right_y = up_left_y + (dataset.RasterYSize * yres)


    scale = '-scale min_val max_val'
    options_list = [
    '-ot Byte',
    '-of JPEG',
    scale
    ]

    options_string = " ".join(options_list)
    gdal.Translate(dir_path, dataset, options=options_string)

    return [up_left_x, up_left_y, low_right_x, low_right_y]

def convert_raster_jpg_progress(path_in: str, path_out: str) -> list[float]:
    file_path = Path(path_in)
    dir_path = Path(path_out).joinpath(f'{file_path.stem}.jpg').as_posix()
    file_path = file_path.as_posix()

    dataset = gdal.Open(file_path)

    # Getting the upper left and lower right points of the image
    up_left_x, xres, xskew, up_left_y, yskew, yres  = dataset.GetGeoTransform()
    low_right_x = up_left_x + (dataset.RasterXSize * xres)
    low_right_y = up_left_y + (dataset.RasterYSize * yres)


    scale = '-scale min_val max_val'
    options_list = [
    '-ot Byte',
    '-of JPEG',
    scale
    ]

    options_string = " ".join(options_list)
    gdal.Translate(dir_path, dataset, options=options_string, callback=progress_cb)

    return [up_left_x, up_left_y, low_right_x, low_right_y]