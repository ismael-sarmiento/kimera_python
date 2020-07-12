""" This module contains different implementations for python loader """


class RawLoader:
    """ Raw - Loader """

    @staticmethod
    def print_console(*args, **kwargs):
        """
            print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
            file:  a file-like object (stream); defaults to the current sys.stdout.
            sep:   string inserted between values, default a space.
            end:   string appended after the last value, default a newline.
            flush: whether to forcibly flush the stream.
        """
        print(*args, **kwargs)
        return True
