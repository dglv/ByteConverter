#!/usr/bin/env python3
"""
Byte converter
"""

import argparse
import sys

from byte_utils.SimpleByteConverter import SimpleByteConverter


def read_from_file(filepath: str) -> str:
    """
    Reads bytes from file

    :param filepath: File path
    :return: bytes as string
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except Exception as e:
        raise Exception(f"Error while reading from file: {filepath} with exception: {e}")


def process_bytes(converter, args):
    if args.stdin:
        input_data = sys.stdin.read().strip()
        bytes_list = converter.parse_input(input_data)
    elif args.file:
        input_data = read_from_file(args.file)
        bytes_list = converter.parse_input(input_data)
    else:
        input_data = ' '.join(args.bytes)
        bytes_list = converter.parse_input(input_data)

    if not bytes_list:
        raise ValueError("Missing bytes for converting")

    if args.mode == '2bytes':
        result = converter.convert_bytes_to_bytes(bytes_list, args.format)
    elif args.mode == '2number':
        result = converter.convert_bytes_to_number(bytes_list, args.endian, args.format)
    else:
        raise ValueError(f"Not supported convertion mode: {args.mode}")

    if args.verbose:
        print(f"Input bytes: {bytes_list}")
        print(f"Input order of bytes: {args.endian}-endian")
        print(f"Output format: {args.format}")

    print(f"{result}")


def main():
    parser = argparse.ArgumentParser(
        description='Bytes converter to various formats',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples of usage:
$ python byte_converter.py --endian little --format hex -12, 54, 55, 14
$ python byte_converter.py --file bytes.txt --endian big --format dec
$ python byte_converter.py 0xFA 0x12 0x1A 0x31 --endian big --format bin --mode 2bytes
$ echo "-12, 0, 55, 55" | python byte_converter.py --stdin -endian little
$ python byte_converter.py 0xFA 0x12 0x1A --format bin --mode 2bytes | python byte_converter.py --stdin --format dec
"""
    )

    # Input data group
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        'bytes',
        nargs='*',
        help='Bytes for processing by convertor (example: -1, 45, 11, -127)'
    )

    input_group.add_argument(
        '--file',
        type=str,
        help='Input file with bytes'
    )

    input_group.add_argument(
        '--stdin',
        action='store_true',
        help='Read bytes from stdin'
    )

    # Parameters for convertion
    parser.add_argument(
        '--endian',
        type=str,
        choices=['big', 'little'],
        default='big',
        help='Order of bytes (little-endian or big-endian). Default: big'
    )

    parser.add_argument(
        '--format',
        type=str,
        choices=['dec', 'hex', 'bin', 'oct'],
        default='dec',
        help='Output format (dec, hex, bin, oct). Default: dec'
    )

    parser.add_argument(
        '--mode',
        type=str,
        choices=['2bytes', '2number'],
        default='2bytes',
        help='Convert bytes to bytes in desired format (2bytes) or bytes to a single number in the format (2number). '
             'Default: 2bytes'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Verbose mode'
    )

    try:
        converter = SimpleByteConverter()
        args = parser.parse_args()

        process_bytes(converter, args)
    except Exception as e:
        print(f"Error while processing bytes: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
