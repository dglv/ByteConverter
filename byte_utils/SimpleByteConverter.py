from typing import List

BASE_2 = 2
BASE_8 = 8
BASE_10 = 10
BASE_16 = 16


class SimpleByteConverter:
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

    def _is_base_2(self, input_str: str) -> bool:
        return input_str.lower().startswith('0b')

    def _is_base_8(self, input_str: str) -> bool:
        return input_str.lower().startswith('0') and len(input_str) > 1

    def _is_base_16(self, input_str: str) -> bool:
        return input_str.lower().startswith('0x')

    def convert_bytes_to_bytes(self,
                               bytes_list: List[int],
                               output_format: str = 'dec') -> str:
        """
        Converts list of input bytes to bytes in desired format

        :param bytes_list: List of input bytes
        :param output_format: 'dec', 'hex', 'bin' or 'oct'
        :return: Result array of bytes as a formatted string
        """
        # Convert bytes to unsigned format
        unsigned_bytes = [b & 0xFF for b in bytes_list]

        formatter = self.formats.get(output_format, self._format_decimal)
        results = []
        for byte in unsigned_bytes:
            results.append(formatter(byte))

        return ", ".join(results)

    def convert_bytes_to_number(self,
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
        # Convert bytes to unsigned format
        unsigned_bytes = [b & 0xFF for b in bytes_list]

        # Convert bytes to number according to desired bytes order
        result = 0
        if endian == 'little':
            for i, byte in enumerate(unsigned_bytes):
                result |= byte << (8 * i)
        elif endian == 'big':
            for i, byte in enumerate(unsigned_bytes):
                result |= byte << (8 * (len(unsigned_bytes) - i - 1))
        else:
            raise ValueError(f"Not supported endian order: {endian}")

        # Format result according to desired output format
        formatter = self.formats.get(output_format, self._format_decimal)
        return formatter(result)

    def parse_input(self, input_str: str) -> List[int]:
        """
        Parses input string with bytes

        :param input_str: Input string with bytes
        :return: List of integers
        """
        input_str = input_str.strip()

        if ',' in input_str:
            parts = input_str.split(',')
        else:
            parts = input_str.split()

        # Convert to numbers
        results = []
        for part in parts:
            part = part.strip()
            if part:  # skip empty strings
                if self._is_base_16(part):
                    base = BASE_16
                elif self._is_base_2(part):
                    base = BASE_2
                elif self._is_base_8(part):
                    base = BASE_8
                else:
                    base = BASE_10

                try:
                    value = int(part, base)
                    results.append(value)
                except ValueError as e:
                    raise ValueError(f"Illegal value: {part}") from e

        return results
