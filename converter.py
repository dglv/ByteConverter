#!/usr/bin/env python3
"""
Byte converter
"""

import argparse
from byte_converter.ByteConverter import ByteConverter


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


def main():
    parser = argparse.ArgumentParser(
        description='Bytes converter to various formats',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples of usage:
$ python converter.py --endian little --format hex -12, 54, 55, 14
$ python converter.py --file bytes.txt --endian big --format dec
$ python converter.py 0xFA 0x12 0x1A 0x31 --endian big --format bin
$ echo "-12, 0, 55, 55" | python converter.py --stdin -endian little
"""
    )

    # Parameters for convertion
    parser.add_argument(
        '--endian',
        type=str,
        choices=['big', 'little'],
        default='big',
        help='Order of bytes (little-endian or big-endian)'
    )

    parser.add_argument(
        '--format',
        type=str,
        choices=['dec', 'hex', 'bin', 'oct'],
        default='dec',
        help='Output format (dec, hex, bin, oct)'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Verbose mode'
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

    args = parser.parse_args()
    converter = ByteConverter()


if __name__ == "__main__":
    main()
