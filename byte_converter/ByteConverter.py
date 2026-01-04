from typing import List


class ByteConverter:
    def __init__(self):
        self.formats = {
            'dec': self._format_decimal,
            'hex': self._format_hex,
            'bin': self._format_binary,
            'oct': self._format_octal
        }

    def _format_decimal(self, value: int) -> str:
        return str(value)

    def _format_hex(self, value: int) -> str:
        return f"0x{value:02X}"

    def _format_binary(self, value: int) -> str:
        return f"0b{value:08b}"

    def _format_octal(self, value: int) -> str:
        return f"0o{value:03o}"

    def convert_bytes(self,
                      bytes_list: List[int],
                      endian: str = 'big',
                      output_format: str = 'dec') -> str:
        """
        Converts list of input bytes to number regarding byte order

        :param bytes_list: List of input bytes
        :param endian: 'big' or 'little'
        :param output_format: 'dec', 'hex', 'bin' or 'oct'
        :return: Result number as a formatted string
        """
        raise Exception("Not Implemented Yet")

    def parse_input(self, input_str: str) -> List[int]:
        """
        Parses input string with bytes

        :param input_str: Input string with bytes
        :return: List of integers
        """
        raise Exception("Not Implemented Yet")