#!/usr/bin/env python3
"""
Number converter
"""

import argparse
import sys

from convert_utils import Constants
from convert_utils.SimpleNumberConverter import SimpleNumberConverter


def process_number(converter, args):
    # TODO: dglv@30min implement process_number() function
    pass


def main():
    parser = argparse.ArgumentParser(
        description='Number converter to various formats',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples of usage:
$ python number_converter.py 12345678 --format hex
$ python number_converter.py --file number.txt --format dec
$ python number_converter.py 0xFA121A31 --format bin
$ echo "0b11010011" | python number_converter.py --stdin --format hex
"""
    )

    # Input data group
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        'number',
        nargs='*',
        help='Desired number for processing by convertor (example: 0x12AF321B)'
    )

    input_group.add_argument(
        '--file',
        type=str,
        help='Input file with desired number'
    )

    input_group.add_argument(
        '--stdin',
        action='store_true',
        help='Read desired number from stdin'
    )

    # Parameters for convertion
    parser.add_argument(
        '--format',
        type=str,
        choices=['dec', 'hex', 'bin', 'oct'],
        default='dec',
        help='Output format (dec, hex, bin, oct). Default: dec'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Verbose mode'
    )

    try:
        converter = SimpleNumberConverter()
        args = parser.parse_args()

        process_number(converter, args)
    except Exception as e:
        print(f"Error while processing bytes: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
