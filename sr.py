import argparse
from pathlib import Path
from osgeo import gdal

def cli(command_line = None):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        metavar="You should use GH, but if not, type one of these commands:", # https://stackoverflow.com/a/11809651
        dest='command', 
        required=True
        )

    # raster to jpeg command
    raster_convert = subparsers.add_parser('raster2jpeg', help=f'converts {allowed_ext()} to .jpeg')
    raster_convert.add_argument('file_to_convert', help=f'The {allowed_ext()} file to convert')
    raster_convert.add_argument('output_folder', help="The output folder for the .jpeg file")

    # raster to jpeg command w/ progress
    raster_convert = subparsers.add_parser('raster2jpeg2', help=f'converts {allowed_ext()} to .jpeg')
    raster_convert.add_argument('file_to_convert', help=f'The {allowed_ext()} file to convert')
    raster_convert.add_argument('output_folder', help="The output folder for the .jpeg file")

    # a place holder - maybe will expand into something fun
    info = subparsers.add_parser('info', help='Get some info about SiteReader')
    info.add_argument('--author', help="Displays the authors name", action='store_true')
    info.add_argument('--mood', help="The authors current mood", action='store_true')


    args = parser.parse_args(command_line)

    #raster to jpeg command
    if args.command == 'raster2jpeg':
        if not check_raster_file(args.file_to_convert):
            raise argparse.ArgumentTypeError(f"Input doesn't exist or it isn't of type: {allowed_ext()}")
        if not Path(args.output_folder).is_dir:
            raise argparse.ArgumentTypeError("You must provide a valid output directory.")
        
        output = convert_raster_jpg(args.file_to_convert, args.output_folder)
        print(*output)

    #raster to jpeg command with progress
    if args.command == 'raster2jpeg2':
        if not check_raster_file(args.file_to_convert):
            raise argparse.ArgumentTypeError(f"Input doesn't exist or it isn't of type: {allowed_ext()}")
        if not Path(args.output_folder).is_dir:
            raise argparse.ArgumentTypeError("You must provide a valid output directory.")
        
        output = convert_raster_jpg_progress(args.file_to_convert, args.output_folder)
        print(*output)

    # the place-holder
    elif args.command == 'info':
        if args.author:
            print('Thomas')
        if args.mood:
            print("tired...")

# ============================= RASTER ===============================================================

def progress_cb(dfProgress: float, message = None, cb_data = None):
    """Simplifed but hopefully smoother looking callback
    """
    bar_prog = int(dfProgress*20)
    p_bar = "[" + "#"*bar_prog + " "*(20 - bar_prog) + "]" + f" - {int(dfProgress*100)}% done"
    print(p_bar, end="\r")

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

def gdal_setup() -> None:
    """Setup error handling for GDAL & print standard 'do not close message to screen'.
    """

    gdal.UseExceptions() # Enable errors
    print("======DO NOT CLOSE THIS WINDOW. IT WILL AUTOMATICALLY CLOSE.======")

def convert_raster_jpg_progress(path_in: str, path_out: str) -> list[float]:

    # display 'do not close message' handle errors
    gdal_setup()

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


cli()