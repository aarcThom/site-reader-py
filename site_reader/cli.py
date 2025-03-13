import argparse
from pathlib import Path
from site_reader.raster import convert_raster_jpg, check_raster_file, allowed_ext, convert_raster_jpg_progress

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