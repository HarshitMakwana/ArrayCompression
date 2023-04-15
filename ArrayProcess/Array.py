class Array:
    def __init__(self,array=None):
        self.array = array
    
    def compress(self):
        """
        The compress function returns a tuple containing the compressed version of an array and the maximum
        value in the array.
        :return: The function `compress` is returning a tuple containing two values:
        1. The compressed value of the array, which is calculated by summing up the product of each element
        in the array with (max_value + 1) raised to the power of its index.
        2. The maximum value in the array.
        """
        max_value =max(self.array)
        return sum(val* (max_value + 1)**i for i, val in enumerate(self.array)),max_value
    
    @staticmethod
    def decompress(value, size,max_value):
        """
        This is a static method in Python that takes in a value, size, and max_value, and returns an array
        of decompressed values.
        
        :param value: The compressed value that needs to be decompressed
        :param size: The size parameter is an integer that represents the number of elements in the
        compressed array
        :param max_value: The maximum value that can be represented in the compressed format. This is used
        to determine the number of bits needed to represent each value in the compressed format
        :return: The function `decompress` returns an array of integers obtained by decompressing the input
        `value` using the given `size` and `max_value` parameters.
        """
        # encoding,max_value = encoding
        array = []
        for _ in range(size-1,-1,-1):
            array.append(value % (max_value + 1))
            value //= (max_value + 1)
        return array
    
# The Array8bit class can compress and decompress an array of 8-bit integers.
class Array8bit:
    def __init__(self,array=None):
        self.array = array
    
    def compress(self):
        """
        This function compresses an array of bytes into a single integer using big-endian byte order.
        :return: The method `compress` is returning an integer value obtained by concatenating all the
        bytes in the `self.array` list and converting them to an integer using the `int.from_bytes()`
        method. The byte order used for the conversion is big-endian.
        """
        return int.from_bytes(b"".join(bytes([x] for x in self.array)),byteorder="big")
    
    @staticmethod
    def decompress(value, size):
        """
        This is a static method in Python that takes a value and size as input and returns a list of bytes
        representing the decompressed value.
        
        :param value: The compressed value that needs to be decompressed. It is expected to be an integer
        :param size: The size parameter is an integer that represents the number of bytes that the value
        should be decompressed into. The decompressed value will be returned as a list of integers, where
        each integer represents a byte in the decompressed value
        :return: A list of bytes obtained from decompressing the input value using the specified size and
        byte order.
        """
        return list(value.to_bytes(size, byteorder="big"))