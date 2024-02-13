import argparse
from raster import convert_raster_jpg, check_raster_file, allowed_extensions

def main(command_line = None):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        metavar="You should use GH, but if not, type one of these commands:", # https://stackoverflow.com/a/11809651
        dest='command', 
        required=True
        )

    # raster to jpeg command
    raster_convert = subparsers.add_parser('raster2jpeg', help=f'converts {', '.join(allowed_extensions)} to .jpeg')
    raster_convert.add_argument('file_to_convert', help=f'The {', '.join(allowed_extensions)} file to convert')
    raster_convert.add_argument('output_folder', help="The output folder for the .jpeg file")

    # a place holder - maybe will expand into something fun
    info = subparsers.add_parser('info', help='Get some info about SiteReader')
    info.add_argument('--author', help="Displays the authors name", action='store_true')
    info.add_argument('--mood', help="The authors current mood", action='store_true')


    args = parser.parse_args(command_line)

    #raster to jpeg command
    if args.command == 'raster2jpeg':
        if not check_raster_file(args.file_to_convert):
            raise argparse.ArgumentTypeError(f"Input doesn't exist or it isn't of type: {', '.join(allowed_extensions)}")

    # the place-holder
    elif args.command == 'info':
        if args.author:
            print('Thomas')
        if args.mood:
            print("tired...")