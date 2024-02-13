import argparse
from pathlib import Path
from raster import convert_raster_jpg

def cli(command_line = None):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        metavar="You should use GH, but if not, type one of these commands:", # https://stackoverflow.com/a/11809651
        dest='command', 
        required=True
        )

    # raster to jpeg command
    raster_convert = subparsers.add_parser('raster2jpeg', help='converts .ecw / .mrSid to .jpeg')
    raster_convert.add_argument('file_to_convert', help='The .ecw / .MrSid file to convert')
    raster_convert.add_argument('output_folder', help="The output folder for the .jpeg file")

    # a place holder - maybe will expand into something fun
    info = subparsers.add_parser('info', help='Get some info about SiteReader')
    info.add_argument('--author', help="Displays the authors name", action='store_true')
    info.add_argument('--mood', help="The authors current mood", action='store_true')


    args = parser.parse_args(command_line)

    #raster to jpeg command
    if args.command == 'raster2jpeg':
        in_file = Path(args.file_to_convert)
        out_path = Path(args.output_folder)
        print (in_file.is_file(), out_path.is_dir())

    # the place-holder
    elif args.command == 'info':
        if args.author:
            print('Thomas')
        if args.mood:
            print("tired...")